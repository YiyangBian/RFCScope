import os
import json
import argparse
from tqdm import tqdm
from datetime import datetime
import tiktoken
from dotenv import load_dotenv
from openai import OpenAI
from retrieval.references import __find_section, __get_flat_sections_list
from retrieval.rfc_retriever import get_structured_rfc, get_rfc_title, __split_identifier_for_comparison
from main.analyze_section_dependencies import build_dependency_dict
from main.generate_corpus import get_rfc_structured_contents

load_dotenv()
OpenAIClient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize tokenizer
encoding = tiktoken.encoding_for_model("o3-mini")

# Retry budget for API calls
RETRY_BUDGET = 3

# Token limit for direct analysis
TOKEN_LIMIT = 175000

# base path for this script
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# System prompt for analysis
# `error_type` should be "inconsistencies" or "underspecifications"
# `instructions` should be a list of instructions for the error type
# `errata_examples` should contain examples of errata reports in the error type
SYSTEM_PROMPT = """You are an expert in networking and have over 20 years of experience in writing RFC (Request for Comments) documents related to Internet protocol standards. Today you will be analysing excerpts from RFC documents and discovering any {error_type} in them. You will report these {error_type} in the form of errata reports, which we will submit to the IETF portal to help improve the quality of the RFC documents. You MUST follow all the steps given below to complete this task.

1. Scan the provided text carefully and identify several concepts. Concepts can be entities, processes, relationships, constraints, etc. present in the text. Think deeply about each concept as you try to discover {error_type} concept-by-concept. Do not miss anything in the text, not even diagrams, tables, or examples.

2. For each concept, identify whether there are any {error_type} in the text.
{instructions}

3. Write an errata report for all the {error_type} you find. The report should be clear, concise, and should contain the following information:
    3.1. The RFC number and title where the issue was found.
    3.2. Proper reference to the section where the issue was found, preferably with excerpts from the text.
    3.3. A detailed explanation of the issue, including why it belongs to {error_type}. You MUST include the reasoning behind your analysis and why you think it is an error. This is very important for us to understand the issue better and to check that your analysis is correct.
    3.4. You NEED NOT provide a solution to the issue. Your job is to identify and report the issue only.

Go through these steps sequentially for each concept you identify in the text, and carefully write the errata reports. Here are some examples of errata reports for your reference:

{errata_examples}"""

# System prompt for evaluation
# `error_type` should be "inconsistencies" or "underspecifications"
# `evaluation_checklist` and `reasoning_instruction` are specific to the error type
EVALUATION_PROMPT = """You are a professor and researcher in the field of networking, with over 50 years of experience in working with RFC (Request for Comments) documents related to Internet protocol standards. You asked your PhD student to analyze some RFC documents and generate errata reports for any {error_type} in them. Now that the student has submitted the reports, you need to evaluate them and decide whether they are good enough to be submitted to the IETF portal. You know from experience that this student reports mostly invalid or irrelevant errata.

Your job is to critically evaluate each report and possibly reject most of them unless they are unquestionably valid. You care deeply about precision, credibility, and technical rigor. You are a respected expert in the field and you understand that reporting any invalid or irrelevant errata will severely hurt your position. Closely follow the instructions given below to evaluate the report.

1. Slowly and step-by-step, repeat the instructions given to the student and check if your findings match those of the student. If there are any {error_type} that the student has missed, you will add it to the report.

2. Follow the below checklist to decide whether to accept or reject a report. Mention your thoughts on each of the points below in your evaluation. **Remember that you will be extremely conservative and your default behavior will be to REJECT.**
{evaluation_checklist}

3. {reasoning_instruction}

Once you have evaluated the report, you please provide a well-formatted version of the errata reports that you will submit to the IETF portal. Of course, you will do this only for the reports that meet your strict evaluation."""


def get_section_content(rfc_number, section_id, dependency_dict, deep_dependency=True):
    """
    Get the content of a section and its dependencies. If `deep_dependency` is True,
    include dependencies of the children sections as well.
    
    Args:
        rfc_number (str): RFC number
        section_id (str): Section ID
        dependency_dict (dict): Dictionary of dependencies
        deep_dependency (bool): Whether to include deep dependencies
        
    Returns:
        str: text content
    """
    # collect all dependencies
    # (including those in subsections, if deep_dependency is True)
    dependencies = []
    for r, s in dependency_dict:
        if r == rfc_number:
            if deep_dependency and s.startswith(section_id):
                dependencies.extend(dependency_dict[(r, s)])
            elif not deep_dependency and s == section_id:
                dependencies.extend(dependency_dict[(r, s)])

    # organize the dependencies by RFC
    deps = {}
    external_deps = []
    for dep_type, dep_tag, dep_value in dependencies:
        if dep_type == "RFC":
            dep_rfc = dep_tag
            dep_section = dep_value

            if dep_rfc not in deps:
                deps[dep_rfc] = []
            deps[dep_rfc].append(dep_section)
        
        if dep_type == "EXTERNAL":
            external_deps.append((dep_tag, dep_value))

    # ignore dependencies that are also in the same RFC
    deps.pop(rfc_number, None)

    for dep_rfc, dep_sections in deps.items():
        sections_to_remove = set()

        # remove sections whose parent is also in deps
        for i, dep_section in enumerate(dep_sections):
            if any(dep_section.startswith(parent_section) for parent_section in dep_sections if parent_section != dep_section):
                sections_to_remove.add(i)

        # remove duplicates
        for i, dep_section in enumerate(dep_sections):
            if dep_section in dep_sections[:i]:
                sections_to_remove.add(i)

        deps[dep_rfc] = [dep_sections[i] for i in range(len(dep_sections)) if i not in sections_to_remove]

        # sort the sections by their identifiers
        deps[dep_rfc].sort(key=__split_identifier_for_comparison)

    # collect the texts
    texts = []

    def get_text(sections):
        for section_id in sections:
            section_title = sections[section_id]["title"]
            section_content = sections[section_id]["content"]
            section_heading_level = section_id.count('.') + 2

            texts.append(f"{'#' * section_heading_level} {section_id}. {section_title}\n\n")
            texts.append(section_content)
            texts.append("\n\n")

            get_text(sections[section_id]["children"])

    # Get all dependency texts
    for dep_rfc, dep_sections in deps.items():
        dep_rfc_contents = get_structured_rfc(dep_rfc)
        dep_rfc_title = get_rfc_title(dep_rfc)

        texts.append(f"# Referenced Sections from RFC {dep_rfc}: {dep_rfc_title}\n\n")
        texts.append("The following sections were referenced. Remaining sections are not included.\n\n")

        dep_contents_sections = {
            dep_section: __find_section(dep_rfc_contents, dep_section)
            for dep_section in dep_sections
        }           

        get_text(dep_contents_sections)

    # now also get any external references
    for title, summary in external_deps:
        if summary:
            texts.append(f"# Summary of reference from {title}\n\n")
            texts.append(summary)
            texts.append("\n\n")

    return "".join(texts)


def get_rfc_content(rfc_number):
    """
    Get the full content of an RFC.
    
    Args:
        rfc_number (str): RFC number
        
    Returns:
        str: text content
    """
    rfc_contents = get_structured_rfc(rfc_number)
    rfc_title = get_rfc_title(rfc_number)
    sections_list = __get_flat_sections_list(rfc_contents)

    texts = []

    # include RFC title
    texts.append(f"# RFC {rfc_number}: {rfc_title}\n\n")

    for section in sections_list:
        section_title = section["title"]
        section_content = section["content"]
        section_heading_level = section["identifier"].count('.') + 2
        
        texts.append(f"{'#' * section_heading_level} {section['identifier']}. {section_title}\n\n")
        texts.append(section_content)
        texts.append("\n\n")

    return "".join(texts)


def create_prompt(rfc_number, section_id, dependency_dict, deep_dependency=True):
    """
    Create a prompt combining RFC content and section dependencies. If the
    `deep_dependency` flag is set to True, include dependencies of the children
    sections as well.
    
    Args:
        rfc_number (str): RFC number
        section_id (str): Section ID
        dependency_dict (dict): Dictionary of dependencies
        deep_dependency (bool): Whether to include deep dependencies
        
    Returns:
        str: Formatted prompt
    """
    rfc_content = get_rfc_content(rfc_number)
    dependency_content = get_section_content(rfc_number, section_id, dependency_dict, deep_dependency)

    prompt = f"Let us analyze section {section_id} of RFC {rfc_number}. All references made by section {section_id} have also been included below.\n\n" + rfc_content + "\n---\n" + dependency_content

    return prompt

def get_output_from_openai(prompt, system_prompt, task):
    """
    Generate results for `task` using OpenAI API.
    
    Args:
        prompt (str): Input prompt for 
        system_prompt (str): System prompt for `task`
        task (str): Short description of the task (for logging purposes)

    Returns:
        str: Generated output
    """
    for retry_count in range(RETRY_BUDGET):
        try:
            completion = OpenAIClient.chat.completions.create(
                model="o3-mini",
                messages=[
                    {
                        "role": "developer",
                        "content": [
                            {
                                "type": "text",
                                "text": system_prompt
                            }
                        ]
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ],
                response_format={
                    "type": "text"
                },
                reasoning_effort="high"
            )
            return completion.choices[0].message.content
        except Exception as e:
            if retry_count == RETRY_BUDGET - 1:
                tqdm.write(f"Failed to perform {task} due to error: {e}")
                return ""
            tqdm.write(f"Retrying due to error: {e}")


def get_output_from_model(prompt, system_prompt, task):
    """
    Generate results for `task` using the selected model.
    
    Args:
        prompt (str): Input prompt for 
        system_prompt (str): System prompt for `task`
        task (str): Short description of the task (for logging purposes)
        
    Returns:
        str: Generated output
    """
    return get_output_from_openai(prompt, system_prompt, task)


def get_and_save_analysis(prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, section_id):
    """
    Generate and save analysis, prompt, and evaluation.
    
    If the file already exists and is not empty, skip the analysis.
    """
    output_filename = os.path.join(output_dir, f"rfc{rfc_number}", f"section{section_id}_analysis.md")
    prompt_filename = os.path.join(output_dir, f"rfc{rfc_number}", f"section{section_id}_prompt.md")
    evaluation_filename = os.path.join(output_dir, f"rfc{rfc_number}", f"section{section_id}_evaluation.md")

    with open(prompt_filename, "w", encoding="utf-8") as f:
        f.write(prompt)

    # generate analysis if it doesn't already exist
    if os.path.exists(output_filename) and os.path.getsize(output_filename) > 0:
        analysis = open(output_filename, encoding="utf-8").read()
    else:
        analysis = get_output_from_model(prompt, system_prompt, "analysis")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(analysis)

    # generate evaluation if it doesn't already exist
    if not os.path.exists(evaluation_filename) or os.path.getsize(evaluation_filename) == 0:
        evaluation_prompt = "\n".join([
            f"You provided the following instructions to your student:\n\n```\n{system_prompt}\n```\n",
            f"The student produced the following analysis:\n\n{analysis}\n",
            f"The relevant RFC text provided to the student was:\n\n{prompt}\n",
        ])
        evaluation = get_output_from_model(evaluation_prompt, evaluation_system_prompt, "evaluation")
        
        with open(evaluation_filename, "w", encoding="utf-8") as f:
            f.write(evaluation)


def process_rfc(rfc_number, dependency_dict, system_prompt, evaluation_system_prompt, output_dir):
    """
    Process an RFC according to the hierarchical section analysis algorithm.
    
    Args:
        rfc_number (str): RFC number
        dependency_dict (dict): Dictionary of dependencies
        system_prompt (str): System prompt for analysis
        evaluation_system_prompt (str): System prompt for evaluation
        output_dir (str): Output directory
    """
    rfc_flat_sections = __get_flat_sections_list(get_rfc_structured_contents(rfc_number))
    
    # Get all level-1 sections
    level1_sections = [s for s in rfc_flat_sections if s["identifier"].count('.') == 0]
    
    os.makedirs(os.path.join(output_dir, f"rfc{rfc_number}"), exist_ok=True)
    
    for section in tqdm(level1_sections, desc=f"Processing RFC {rfc_number} Level-1 sections"):
        section_id = section["identifier"]
        prompt = create_prompt(rfc_number, section_id, dependency_dict)
        prompt_tokens = len(encoding.encode(prompt))
        
        # Get level-2 subsections of this section
        level2_subsections = section["children"]
        
        # If no subsections or token count is under the limit, analyze this section directly
        if not level2_subsections or prompt_tokens < TOKEN_LIMIT:
            get_and_save_analysis(prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, section_id)
        else:
            # Process level-2 subsections
            
            # first process the "zero" subsection
            prompt = create_prompt(rfc_number, section_id, dependency_dict, deep_dependency=False)
            get_and_save_analysis(prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, section_id)
            
            subsections = [s for s in rfc_flat_sections if s["identifier"] in level2_subsections]
            for subsection in tqdm(subsections, desc=f"Processing RFC {rfc_number} Section {section_id} subsections"):
                subsection_id = subsection["identifier"]
                prompt = create_prompt(rfc_number, subsection_id, dependency_dict)
                prompt_tokens = len(encoding.encode(prompt))
                
                # Get sub-subsections
                level3_subsubsections = subsection["children"]
                
                # If no sub-subsections or token count is under the limit, analyze this subsection
                if not level3_subsubsections or prompt_tokens < TOKEN_LIMIT:
                    get_and_save_analysis(prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, subsection_id)
                else:
                    # Process level-3 sections

                    # first process the "zero" subsubsection
                    prompt = create_prompt(rfc_number, subsection_id, dependency_dict, deep_dependency=False)
                    get_and_save_analysis(prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, subsection_id)
                    
                    subsubsections = [s for s in rfc_flat_sections if s["identifier"] in level3_subsubsections]
                    for subsubsection in tqdm(subsubsections, desc=f"Processing RFC {rfc_number} Section {subsection_id} subsubsections"):
                        subsubsection_id = subsubsection["identifier"]
                        prompt = create_prompt(rfc_number, subsubsection_id, dependency_dict)
                        prompt_tokens = len(encoding.encode(prompt))

                        get_and_save_analysis(prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, subsubsection_id)


def load_errata_examples(errata_reports, errata_schema):
    """
    Load and format errata examples.
    
    Args:
        errata_reports (list): List of errata reports
        errata_schema (dict): Schema for selecting errata examples
        
    Returns:
        str: Formatted errata examples
    """
    errata_example_text = []
    for category in errata_schema:
        errata_example_text.append(f"# {category}\n\n")
        for errata_id, subcategory in errata_schema[category].items():
            errata_report = next((e for e in errata_reports if e['errata_id'] == errata_id), None)
            if not errata_report:
                print("Could not find errata report", errata_id)
                continue

            rfc_number = errata_report['rfc_number']
            rfc_title = errata_report['rfc_title']
            errata_id = errata_report['errata_id']
            errata_report_contents = errata_report['errata_text']
            errata_explanation = errata_report['errata_category_reason']
            
            errata_example_text.append("\n".join([
                f"## {subcategory}\n"
                f"Errata {errata_id} from {rfc_number} ({rfc_title})",
                "\n",
                errata_report_contents,
                errata_explanation,
            ]))

    return "\n".join(errata_example_text)


def main(rfc_number: int, section_dependency_graph_path: str, corpus_path: str, error_type: int, output_dir: str):    
    # Load the graph and corpus
    with open(section_dependency_graph_path, 'r', encoding="utf-8") as f:
        section_dependencies = json.load(f)

    with open(corpus_path, 'r', encoding="utf-8") as f:
        corpus_data = json.load(f)
    
    # Build dependency dictionary
    dependency_dict = build_dependency_dict(section_dependencies, corpus_data)

    if error_type != 0 and error_type != 1:
        raise ValueError("Invalid category. Use 0 for inconsistencies and 1 for underspecifications.")
    category = "inconsistency" if error_type == 0 else "under-specification"

    prompts_path = os.path.join(BASE_PATH, "..", "..", "prompts", "system-prompts", category)

    with open(os.path.join(prompts_path, "analyzer.md"), "r", encoding="utf-8") as f:
        system_prompt = f.read()
    with open(os.path.join(prompts_path, "evaluator.md"), "r", encoding="utf-8") as f:
        evaluation_system_prompt = f.read()

    # Process RFC
    process_rfc(rfc_number, dependency_dict, system_prompt, evaluation_system_prompt, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze RFCs with a hierarchical approach')
    parser.add_argument('rfc_number', type=int, help='RFC number to analyze')
    parser.add_argument('section_dependency_graph_path', type=str, help='Path to the section dependency graph JSON file')
    parser.add_argument('corpus_path', type=str, help='Path to the corpus JSON file')
    parser.add_argument('category', type=int, help='Error category to look for (0 = inconsistency | 1 = underspecifications)')
    parser.add_argument('--output-dir', type=str, default='rfc_analysis', help='Directory to save the generated reports')
    args = parser.parse_args()
    main(
        rfc_number=args.rfc_number,
        section_dependency_graph_path=args.section_dependency_graph_path,
        corpus_path=args.corpus_path,
        error_type=args.category,
        output_dir=args.output_dir
    )
