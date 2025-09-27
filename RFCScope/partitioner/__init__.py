import os
from tqdm import tqdm
from typing import Callable
import tiktoken
from utils.references import __find_section, __get_flat_sections_list
from utils.rfc_retriever import (
    get_structured_rfc,
    get_rfc_title,
    __split_identifier_for_comparison,
)
from context_constructor.generate_corpus import get_rfc_structured_contents


# Initialize tokenizer
encoding = tiktoken.encoding_for_model("o3-mini")


# Token limit for direct analysis
TOKEN_LIMIT = 175000


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
            if any(
                dep_section.startswith(parent_section)
                for parent_section in dep_sections
                if parent_section != dep_section
            ):
                sections_to_remove.add(i)

        # remove duplicates
        for i, dep_section in enumerate(dep_sections):
            if dep_section in dep_sections[:i]:
                sections_to_remove.add(i)

        deps[dep_rfc] = [
            dep_sections[i]
            for i in range(len(dep_sections))
            if i not in sections_to_remove
        ]

        # sort the sections by their identifiers
        deps[dep_rfc].sort(key=__split_identifier_for_comparison)

    # collect the texts
    texts = []

    def get_text(sections):
        for section_id in sections:
            section_title = sections[section_id]["title"]
            section_content = sections[section_id]["content"]
            section_heading_level = section_id.count(".") + 2

            texts.append(
                f"{'#' * section_heading_level} {section_id}. {section_title}\n\n"
            )
            texts.append(section_content)
            texts.append("\n\n")

            get_text(sections[section_id]["children"])

    # Get all dependency texts
    for dep_rfc, dep_sections in deps.items():
        dep_rfc_contents = get_structured_rfc(dep_rfc)
        dep_rfc_title = get_rfc_title(dep_rfc)

        texts.append(f"# Referenced Sections from RFC {dep_rfc}: {dep_rfc_title}\n\n")
        texts.append(
            "The following sections were referenced. Remaining sections are not included.\n\n"
        )

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
        section_heading_level = section["identifier"].count(".") + 2

        texts.append(
            f"{'#' * section_heading_level} {section['identifier']}. {section_title}\n\n"
        )
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
    dependency_content = get_section_content(
        rfc_number, section_id, dependency_dict, deep_dependency
    )

    prompt = (
        f"Let us analyze section {section_id} of RFC {rfc_number}. All references made by section {section_id} have also been included below.\n\n"
        + rfc_content
        + "\n---\n"
        + dependency_content
    )

    return prompt


def process_rfc(
    rfc_number,
    dependency_dict,
    system_prompt,
    evaluation_system_prompt,
    output_dir,
    get_and_save_analysis: Callable,
):
    """
    Process an RFC according to the hierarchical section analysis algorithm.

    Args:
        rfc_number (str): RFC number
        dependency_dict (dict): Dictionary of dependencies
        system_prompt (str): System prompt for analysis
        evaluation_system_prompt (str): System prompt for evaluation
        output_dir (str): Output directory
        get_and_save_analysis (function): Function to get and save analysis
    """
    rfc_flat_sections = __get_flat_sections_list(
        get_rfc_structured_contents(rfc_number)
    )

    # Get all level-1 sections
    level1_sections = [s for s in rfc_flat_sections if s["identifier"].count(".") == 0]

    os.makedirs(os.path.join(output_dir, f"rfc{rfc_number}"), exist_ok=True)

    for section in tqdm(
        level1_sections, desc=f"Processing RFC {rfc_number} Level-1 sections"
    ):
        section_id = section["identifier"]
        prompt = create_prompt(rfc_number, section_id, dependency_dict)
        prompt_tokens = len(encoding.encode(prompt))

        # Get level-2 subsections of this section
        level2_subsections = section["children"]

        # If no subsections or token count is under the limit, analyze this section directly
        if not level2_subsections or prompt_tokens < TOKEN_LIMIT:
            get_and_save_analysis(
                prompt,
                system_prompt,
                evaluation_system_prompt,
                output_dir,
                rfc_number,
                section_id,
            )
        else:
            # Process level-2 subsections

            # first process the "zero" subsection
            prompt = create_prompt(
                rfc_number, section_id, dependency_dict, deep_dependency=False
            )
            get_and_save_analysis(
                prompt,
                system_prompt,
                evaluation_system_prompt,
                output_dir,
                rfc_number,
                section_id,
            )

            subsections = [
                s for s in rfc_flat_sections if s["identifier"] in level2_subsections
            ]
            for subsection in tqdm(
                subsections,
                desc=f"Processing RFC {rfc_number} Section {section_id} subsections",
            ):
                subsection_id = subsection["identifier"]
                prompt = create_prompt(rfc_number, subsection_id, dependency_dict)
                prompt_tokens = len(encoding.encode(prompt))

                # Get sub-subsections
                level3_subsubsections = subsection["children"]

                # If no sub-subsections or token count is under the limit, analyze this subsection
                if not level3_subsubsections or prompt_tokens < TOKEN_LIMIT:
                    get_and_save_analysis(
                        prompt,
                        system_prompt,
                        evaluation_system_prompt,
                        output_dir,
                        rfc_number,
                        subsection_id,
                    )
                else:
                    # Process level-3 sections

                    # first process the "zero" subsubsection
                    prompt = create_prompt(
                        rfc_number,
                        subsection_id,
                        dependency_dict,
                        deep_dependency=False,
                    )
                    get_and_save_analysis(
                        prompt,
                        system_prompt,
                        evaluation_system_prompt,
                        output_dir,
                        rfc_number,
                        subsection_id,
                    )

                    subsubsections = [
                        s
                        for s in rfc_flat_sections
                        if s["identifier"] in level3_subsubsections
                    ]
                    for subsubsection in tqdm(
                        subsubsections,
                        desc=f"Processing RFC {rfc_number} Section {subsection_id} subsubsections",
                    ):
                        subsubsection_id = subsubsection["identifier"]
                        prompt = create_prompt(
                            rfc_number, subsubsection_id, dependency_dict
                        )
                        prompt_tokens = len(encoding.encode(prompt))

                        get_and_save_analysis(
                            prompt,
                            system_prompt,
                            evaluation_system_prompt,
                            output_dir,
                            rfc_number,
                            subsubsection_id,
                        )
