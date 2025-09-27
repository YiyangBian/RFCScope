import os
import json
import argparse
from tqdm import tqdm
from dotenv import load_dotenv
from openai import OpenAI
from context_constructor.analyze_section_dependencies import build_dependency_dict
from partitioner import process_rfc
from analyzer import run_analyzer
from evaluator import run_evaluator

load_dotenv()
OpenAIClient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Retry budget for API calls
RETRY_BUDGET = 3

# base path for this script
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


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
                        "content": [{"type": "text", "text": system_prompt}],
                    },
                    {"role": "user", "content": [{"type": "text", "text": prompt}]},
                ],
                response_format={"type": "text"},
                reasoning_effort="high",
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


def get_and_save_analysis(
    prompt, system_prompt, evaluation_system_prompt, output_dir, rfc_number, section_id
):
    """
    Generate and save analysis, prompt, and evaluation.

    If the file already exists and is not empty, skip the analysis.
    """
    analysis = run_analyzer(
        prompt, system_prompt, output_dir, rfc_number, section_id, get_output_from_model
    )
    run_evaluator(
        prompt,
        system_prompt,
        evaluation_system_prompt,
        analysis,
        output_dir,
        rfc_number,
        section_id,
        get_output_from_model,
    )


def main(
    rfc_number: int,
    section_dependency_graph_path: str,
    corpus_path: str,
    error_type: int,
    output_dir: str,
):
    # Load the graph and corpus
    with open(section_dependency_graph_path, "r", encoding="utf-8") as f:
        section_dependencies = json.load(f)

    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus_data = json.load(f)

    # Build dependency dictionary
    dependency_dict = build_dependency_dict(section_dependencies, corpus_data)

    if error_type != 0 and error_type != 1:
        raise ValueError(
            "Invalid category. Use 0 for inconsistencies and 1 for underspecifications."
        )
    category = "inconsistency" if error_type == 0 else "under-specification"

    prompts_path = os.path.join(
        BASE_PATH, "..", "..", "prompts", "system-prompts", category
    )

    with open(os.path.join(prompts_path, "analyzer.md"), "r", encoding="utf-8") as f:
        system_prompt = f.read()
    with open(os.path.join(prompts_path, "evaluator.md"), "r", encoding="utf-8") as f:
        evaluation_system_prompt = f.read()

    # Process RFC
    process_rfc(
        rfc_number,
        dependency_dict,
        system_prompt,
        evaluation_system_prompt,
        output_dir,
        get_and_save_analysis,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze RFCs with a hierarchical approach"
    )
    parser.add_argument("rfc_number", type=int, help="RFC number to analyze")
    parser.add_argument(
        "section_dependency_graph_path",
        type=str,
        help="Path to the section dependency graph JSON file",
    )
    parser.add_argument("corpus_path", type=str, help="Path to the corpus JSON file")
    parser.add_argument(
        "category",
        type=int,
        help="Error category to look for (0 = inconsistency | 1 = underspecifications)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="rfc_analysis",
        help="Directory to save the generated reports",
    )
    args = parser.parse_args()
    main(
        rfc_number=args.rfc_number,
        section_dependency_graph_path=args.section_dependency_graph_path,
        corpus_path=args.corpus_path,
        error_type=args.category,
        output_dir=args.output_dir,
    )
