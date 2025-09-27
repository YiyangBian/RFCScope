import json
import argparse
from tqdm import tqdm
from utils.references import get_references_from_rfc_excerpt

MIN_PARA_LINES = (
    3  # minimum number of lines in a paragraph to be considered a paragraph
)


def __merge_short_paragraphs(paragraphs: list[str]) -> list[str]:
    """
    If any paragraph is too short, merge it with the previous one.
    If the first paragraph is too short, merge it with the previous one.
    Do this recursively until no more merges are possible.
    """
    if len(paragraphs) <= 1:
        return paragraphs

    new_paragraphs = []
    for i, paragraph in enumerate(paragraphs):
        if i == 0:
            # always add the first paragraph
            new_paragraphs.append(paragraph)
            continue

        if len(paragraph.split("\n")) < MIN_PARA_LINES:
            # merge with the previous paragraph
            new_paragraphs[-1] += f"\n\n{paragraph}"
        else:
            new_paragraphs.append(paragraph)

    # now check the first paragraph
    if len(new_paragraphs[0].split("\n")) < MIN_PARA_LINES:
        new_paragraphs[1] = f"{new_paragraphs[0]}\n\n{new_paragraphs[1]}"
        new_paragraphs = new_paragraphs[1:]

    # check if any more merges are possible
    if len(new_paragraphs) != len(paragraphs):
        return __merge_short_paragraphs(new_paragraphs)

    return new_paragraphs


def __get_external_references(references: list[dict]) -> list[dict]:
    """
    Extract external references from the references list.
    """
    external_references_list = []
    for reference in references:
        if reference["document_type"] != "RFC":
            external_references_list.append(
                {
                    "tag": reference["document_tag"],
                    "reference_type": reference["reference_type"],
                    "reference_value": reference["reference_value"],
                }
            )

    return external_references_list


def __referenced_texts_to_references_list(referenced_texts: dict) -> list[dict]:
    """
    Convert the referenced texts dictionary to a list of references with just the
    RFC number and section ID.
    """
    references_list = []
    for rfc_number, sections in referenced_texts.items():
        for section_id, _ in sections.items():
            references_list.append({"rfc_number": rfc_number, "section_id": section_id})

    return references_list


def split_content_into_chunks(
    rfc_number: str,
    content: str,
    perform_reference_extraction: bool = False,
    references_information: dict = None,
) -> list[dict]:
    """
    Split content into meaningful chunks, typically paragraphs.
    Each chunk should ideally represent a complete thought or statement.

    If `perform_reference_extraction` is True, references will be extracted from the content.
    If `references_information` is provided, it will be used to enhance reference extraction.

    A chunk is a dictionary with the following structure.
    ```
    {
        "text": str  # The actual content of the chunk,
        "references": [{
            "rfc_number": str,  # The RFC number referenced in the chunk
            "section_id": str   # The section ID referenced in the chunk
        }],
        "external_references": [{
            "tag": str,  # The tag of the external reference
            "reference_type": "SECTION" | "TEXT", # how the reference is made
            "reference_value": str,  # the section identifier or referrenced text
        }]
    }
    ```
    """
    # First split by double newlines (paragraphs)
    paragraphs = [p for p in content.split("\n\n")]

    # remove empty paragraphs
    paragraphs = [p for p in paragraphs if p]

    # merge short paragraphs
    paragraphs = __merge_short_paragraphs(paragraphs)

    chunks = []
    for paragraph in tqdm(paragraphs, desc="Splitting content into chunks"):
        if perform_reference_extraction:
            references, referenced_texts = get_references_from_rfc_excerpt(
                rfc_number, paragraph, references_information
            )

            references_list = __referenced_texts_to_references_list(referenced_texts)
            external_references_list = __get_external_references(references)
        else:
            references_list = []
            external_references_list = []

        chunks.append(
            {
                "text": paragraph,
                "references": references_list,
                "external_references": external_references_list,
            }
        )

    return chunks


def process_sections(
    rfc_number: str,
    sections: dict,
    perform_reference_extraction: bool = False,
    references: dict = None,
) -> dict:
    """
    Process a section and all its subsections, adding decomposed_content field.
    Returns the modified section dictionary (although it's modified in place).

    If `perform_reference_extraction` is True, references will be extracted from the content.
    If `references` is provided, it will be used to enhance reference extraction.
    """
    for section_id, section in sections.items():
        tqdm.write(f"Processing section {section_id}. {section['title']}")

        if "content" in section:
            decomposed_content = split_content_into_chunks(
                rfc_number, section["content"], perform_reference_extraction, references
            )
            if "decomposed_content" not in section:
                section["decomposed_content"] = decomposed_content
            else:
                # just update the decomposed content
                for i, chunk in enumerate(decomposed_content):
                    section["decomposed_content"][i]["text"] = chunk["text"]
                    section["decomposed_content"][i]["references"] = (
                        chunk["references"] if chunk["references"] else []
                    )
                    section["decomposed_content"][i]["external_references"] = (
                        chunk["external_references"]
                        if chunk["external_references"]
                        else []
                    )

        if "children" in section:
            process_sections(
                rfc_number,
                section["children"],
                perform_reference_extraction,
                references,
            )

    return sections


def process_corpus(
    input_path: str,
    output_path: str,
    perform_reference_extraction: bool = False,
    references: dict = None,
):
    """
    Process the corpus file at input_path and save the result to output_path.

    If `perform_reference_extraction` is True, references will be extracted from the content.
    If `references` is provided, it will be used to enhance reference extraction.
    """
    with open(input_path, "r") as f:
        corpus = json.load(f)

    rfc = corpus[0]
    if "structured_content" in rfc:
        process_sections(
            rfc["rfc_number"],
            rfc["structured_content"],
            perform_reference_extraction,
            references,
        )

    with open(output_path, "w") as f:
        json.dump(corpus, f, indent=2)


def main(corpus_path: str, references_path: str):
    with open(references_path, "r") as f:
        references = json.load(f)

    process_corpus(corpus_path, corpus_path, True, references)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process RFC corpus to decompose section contents"
    )
    parser.add_argument("input", type=str, help="Path to the input corpus JSON file")
    parser.add_argument(
        "--references", type=str, help="Path to the RFC references JSON file"
    )
    args = parser.parse_args()

    main(args.input, args.references)
