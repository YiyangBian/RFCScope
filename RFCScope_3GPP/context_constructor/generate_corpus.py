import re
import os
import json
import argparse
from utils.rfc_retriever import get_structured_rfc, get_rfc_title

base_path = os.path.dirname(os.path.abspath(__file__))


def __get_section_contents(section_id: str, section_data: dict) -> str:
    """
    Get the contents of the given section.
    """
    return "\n".join(
        [
            f"{section_id}. {section_data['title']}",
            "",
            section_data["content"],
            "",
            *[
                __get_section_contents(child, section_data["children"][child])
                for child in section_data["children"]
            ],
            "",
        ]
    )


def __contains_table_of_contents(content: str) -> bool:
    """
    Check if the given content contains a table of contents.

    This is done by checking if the content contains a line with just
    "Table of Contents" and blank lines before and after it.
    """
    match = re.search(r"\n\s*Table of Contents\s*\n", content)
    return match is not None


def __should_skip_section(
    section_data: dict,
    skip_references: bool,
    skip_considerations: bool,
    skip_legacy_sections: bool,
) -> bool:
    """
    Unified function to determine if a section should be skipped based on the given options.
    """
    if skip_references and (
        section_data["title"].lower().startswith("references")
        or section_data["title"].lower()
        in ["normative references", "informative references"]
    ):
        return True  # skip the references section

    if skip_considerations and section_data["title"].lower().endswith("considerations"):
        return True  # skip the considerations section

    if skip_legacy_sections:
        if section_data["title"].lower() in [
            "acknowledgements",
            "acknowledgments",  # alternate spelling
            "authors' addresses",
            "author's address",
            "conclusion",
        ] or any(
            title_keywords in section_data["title"].lower()
            for title_keywords in ["copyright statement", "intellectual property"]
        ):
            return True  # skip legacy sections

    return False


def get_rfc_contents(
    rfc_number: int,
    skip_preamble: bool = True,
    skip_references: bool = True,
    skip_considerations: bool = True,
    skip_legacy_sections: bool = True,
) -> str:
    """
    Get the contents of the given RFC (`rfc_number`) as a single string.

    * If `skip_preamble` is True, any sections before the main content will be
    skipped. This is required only for older RFCs where the main content does
    not start with the first section.
    * If `skip_references` is True, any references section will be skipped.
    * If `skip_considerations` is True, any considerations section will be skipped.
    * If `skip_legacy_sections` is True, sections like "Acknowledgements", "Authors'
    Addresses", "Copyright", etc. will be skipped. These sections are usually
    present in older RFCs and are not a part of the main content in newer RFCs.
    """
    rfc_contents = get_structured_rfc(rfc_number)
    section_contents = []

    for section_id, section_data in rfc_contents.items():
        if not __should_skip_section(
            section_data, skip_references, skip_considerations, skip_legacy_sections
        ):
            section_contents.append(__get_section_contents(section_id, section_data))

    if skip_preamble:
        # find the first section with a table of contents
        # and skip everything before that (including the section itself)
        for i, section_content in enumerate(section_contents):
            if __contains_table_of_contents(section_content):
                section_contents = section_contents[i + 1 :]
                break

    return "".join(section_contents)


def get_rfc_structured_contents(
    rfc_number: int,
    skip_preamble: bool = True,
    skip_references: bool = True,
    skip_considerations: bool = True,
    skip_legacy_sections: bool = True,
) -> dict:
    """
    Get the contents of the given RFC as a structured dictionary, preserving the section hierarchy.
    Returns a dictionary of section data with the same filtering options as get_rfc_contents.
    """
    rfc_contents = get_structured_rfc(rfc_number)
    filtered_contents = {}

    for section_id, section_data in rfc_contents.items():
        if not __should_skip_section(
            section_data, skip_references, skip_considerations, skip_legacy_sections
        ):
            filtered_contents[section_id] = section_data

    if skip_preamble:
        # find the first section with a table of contents
        # and skip everything before that (including the section itself)
        sections_to_remove = []
        found_toc = False
        for section_id, section_data in filtered_contents.items():
            if not found_toc:
                found_toc = __contains_table_of_contents(section_data["content"])
                sections_to_remove.append(section_id)
            if found_toc:
                break

        if found_toc:
            for section_id in sections_to_remove:
                del filtered_contents[section_id]

    return filtered_contents


def get_rfc_contents_from_complete_graph(
    rfc_number: str,
    skip_preamble: bool = True,
    skip_references: bool = True,
    skip_considerations: bool = True,
    skip_legacy_sections: bool = True,
) -> list[dict]:
    """
    Get the contents of the RFC as a singleton list of

    {
        "rfc_number": int,
        "rfc_title": str,
        "content": str,
        "structured_content": dict
    }

    * If `skip_preamble` is True, any sections before the main content will be
    skipped. This is required only for older RFCs where the main content does
    not start with the first section.
    * If `skip_references` is True, any references section will be skipped.
    * If `skip_considerations` is True, any considerations section will be skipped.
    * If `skip_legacy_sections` is True, sections like "Acknowledgements", "Authors'
    Addresses", "Copyright", etc. will be skipped. These sections are usually present
    in older RFCs and are not a part of the main content in newer RFCs.
    """
    corpus = []
    corpus.append(
        {
            "rfc_number": rfc_number,
            "rfc_title": get_rfc_title(rfc_number),
            "content": get_rfc_contents(
                rfc_number,
                skip_preamble,
                skip_references,
                skip_considerations,
                skip_legacy_sections,
            ),
            "structured_content": get_rfc_structured_contents(
                rfc_number,
                skip_preamble,
                skip_references,
                skip_considerations,
                skip_legacy_sections,
            ),
        }
    )

    return corpus


def main(rfc_number: int, output_directory: str):
    output_path = os.path.join(output_directory, "corpus.json")

    # Generate the corpus
    corpus = get_rfc_contents_from_complete_graph(rfc_number)

    # Save the corpus
    with open(output_path, "w") as f:
        json.dump(corpus, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate RFC corpus from dependency graph"
    )
    parser.add_argument(
        "rfc_number", type=int, help="RFC number to generate corpus for"
    )
    parser.add_argument(
        "output", type=str, help="Path to the output directory for saving the corpus"
    )
    args = parser.parse_args()
    main(args.rfc_number, args.output)
