import os
import re
import json
import argparse
from bs4 import BeautifulSoup
from utils.rfc_retriever import get_structured_rfc
from utils.rfc2html import markup


def __extract_references(content: str) -> list[dict]:
    """
    Extract references from the given content.

    Return a list of references, where each reference is a dictionary
    with the following format:

    {
        "tag": str,
        "text": str,
        "links": [urs]
    }
    """
    content = "\n" + content  # for convenience

    # check if there is an [XXXX] in the content
    # and if there is, take the indentation of its first occurrence
    first_tag = re.search(r"\[(.*?)\]", content)
    if first_tag is None:
        return []

    line_with_first_tag = content[: first_tag.start()].split("\n")[-1]
    indentation_size = len(line_with_first_tag) - len(line_with_first_tag.lstrip())
    indentation = " " * indentation_size

    # find each [XXXX] in the content and extract the intervening text
    references = []
    for match in re.finditer(rf"\n{indentation}\[(.*?)\]", content):
        tag = match.group(1)
        start = match.end()

        next_ref = re.search(rf"\n{indentation}\[(.*?)\]", content[start:])
        if next_ref is not None:
            end = next_ref.start() + start
        else:
            end = len(content)

        text = content[start:end].strip()
        text_lines = [line.strip() for line in text.split("\n") if line.strip()]
        text = " ".join(text_lines)

        # convert to HTML and extract links
        html_text = markup(text)
        soup = BeautifulSoup(html_text, "html.parser")
        a_tags = soup.find_all("a")
        links = [{"text": a.text, "address": a.get("href")} for a in a_tags]

        references.append({"tag": tag, "text": text, "links": links})

    return references


def __extract_reference_section(content: str, section_title: str) -> dict:
    """
    Extract the reference section from the given content based on the section title.
    """
    search = re.search(rf"\n{section_title}\s+\n", content)
    if search is not None:
        start = search.start()

        # get lines and remove the leading empty lines
        lines = content[start:].split("\n")
        while lines and not lines[0].strip():
            lines.pop(0)

        content = []
        for line in lines[1:]:  # skip the first line with the title
            if line and not line[0].isspace():
                break
            content.append(line)
        return {
            "title": lines[0].strip(),
            "content": "\n".join(content),
            "children": {},
        }

    return None


def get_referenced_rfcs(rfc_number: int) -> list[dict]:
    """
    Get all RFCs referenced by the given RFC.

    Return a list of references, where each reference is a dictionary
    with the following format:

    {
        "type": "normative" | "informative" | "unknown",
        "tag": str,
        "text": str,
        "links": [urs]
    }

    and url is a dictionary with the following format:

    {
        "text": str,
        "address": str # may be complete or partial
    }

    If the words 'normative' or 'informative' are not found in the reference
    section title, the type is set to 'unknown'.
    """
    rfc_contents = get_structured_rfc(rfc_number)

    reference_sections = []

    # if there is a section with the title "References" or "Normative References"
    # or "Informative References", then add it to the reference_sections list
    for _, section_data in rfc_contents.items():
        if section_data["title"].lower() in [
            "references",
            "normative references",
            "informative references",
        ]:
            reference_sections.append(section_data)

    # if no reference section is found this way, select the last section with 'references' in the title
    if not reference_sections:
        for _, section_data in rfc_contents.items():
            if section_data["title"].lower().startswith("references"):
                reference_sections = [section_data]

    # if no reference section is found this way either, it is likely that "References" was not marked as a section
    # we will select the last instance of "\nReferences\s+\n", etc. in sections of the RFC and capture everything until
    # indentation is restored to the original level
    if not reference_sections:
        # we first re-fetch the rfc_contents but without cleaning the legacy sections
        # since the references section might be one of those
        rfc_contents = get_structured_rfc(rfc_number, clean_legacy_sections=False)

        reference_section = None
        normative_reference_section = None
        informative_reference_section = None
        for _, section_data in rfc_contents.items():
            reference_section = (
                __extract_reference_section(section_data["content"], "References")
                or reference_section
            )
            normative_reference_section = (
                __extract_reference_section(
                    section_data["content"], "Normative References"
                )
                or normative_reference_section
            )
            informative_reference_section = (
                __extract_reference_section(
                    section_data["content"], "Informative References"
                )
                or informative_reference_section
            )

        reference_sections = [
            x
            for x in [
                reference_section,
                normative_reference_section,
                informative_reference_section,
            ]
            if x is not None
        ]

    if reference_sections is None:
        return []

    references = []
    for references_section in reference_sections:
        # If the title is "Normative References" or "Informative References",
        # then all references are of that type.
        if references_section["title"].lower() == "normative references":
            refs = __extract_references(references_section["content"])
            for ref in refs:
                ref["type"] = "normative"
            references.extend(refs)
        elif references_section["title"].lower() == "informative references":
            refs = __extract_references(references_section["content"])
            for ref in refs:
                ref["type"] = "informative"
            references.extend(refs)

        # otherwise check if there are sub-sections with the titles
        # "Normative References" or "Informative References"
        elif any(
            references_section["children"][child_id]["title"].lower()
            in ["normative references", "informative references"]
            for child_id in references_section["children"]
        ):
            for child_id in references_section["children"]:
                child = references_section["children"][child_id]
                if child["title"].lower() == "normative references":
                    refs = __extract_references(child["content"])
                    for ref in refs:
                        ref["type"] = "normative"
                    references.extend(refs)
                elif child["title"].lower() == "informative references":
                    refs = __extract_references(child["content"])
                    for ref in refs:
                        ref["type"] = "informative"
                    references.extend(refs)

        # otherwise, all references are of unknown type
        else:
            refs = __extract_references(references_section["content"])
            for ref in refs:
                ref["type"] = "unknown"
            references.extend(refs)

    return references


def main(rfc_number: str, output_dir: str):
    """Parses the references from the given RFC number and saves them to the given path."""
    output_path = os.path.join(output_dir, f"references.json")
    with open(output_path, "w") as f:
        json.dump(get_referenced_rfcs(int(rfc_number)), f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract references from an RFC and save them to a JSON file"
    )
    parser.add_argument(
        "rfc_number", type=str, help="RFC number to extract references from"
    )
    parser.add_argument(
        "output_directory",
        type=str,
        help="Path to the directory where the output JSON file will be saved",
    )

    args = parser.parse_args()
    main(args.rfc_number, args.output_directory)
