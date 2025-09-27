import os
import json
import argparse
from tqdm import tqdm
from dotenv import load_dotenv
from openai import OpenAI
from utils import cache
from utils.rfc_retriever import __get_first_int

load_dotenv()
OpenAIClient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Retry budget for API calls
RETRY_BUDGET = 3


@cache
def get_external_reference_summary(
    document_tag, reference_value, reference_type, url, reference_text
):
    """
    Generate a summary for an external reference using GPT-4o-search.

    Args:
        document_tag (str): Document tag
        reference_value (str): Reference value
        reference_type (str): Reference type
        url (str): URL of the external reference
        reference_text (str): Reference text

    Returns:
        str: Generated summary
    """
    document_title = (
        reference_text + f"({document_tag})" if reference_text else document_tag
    )
    prompt = f"Can you look up the following document: {document_title}?"

    if url:
        prompt += "You can find the document at the following URL: " + url

    if reference_type == "SECTION":
        prompt += (
            "\n\nI am looking for section " + reference_value + " in the document."
        )
    else:
        prompt += "\n\nI am looking for " + reference_value + " in the document."

    for retry_count in range(RETRY_BUDGET):
        try:
            completion = OpenAIClient.chat.completions.create(
                model="gpt-4o-search-preview",
                messages=[
                    {
                        "role": "developer",
                        "content": [
                            {
                                "type": "text",
                                "text": """Today you will behave as a search engine for internal use at the Internet Engineering Task Force (IETF). At IETF, we often cite documents, white papers, research papers, technical manuals, etc. from across the internet. Your task will be to take information about the title or URL of such documents, along with what we are looking at in the document, and return a concise but complete summary of that topic from the source. Do you hallucinate and stick to the material in the source, which you will find through a web search.""",
                            }
                        ],
                    },
                    {"role": "user", "content": [{"type": "text", "text": prompt}]},
                ],
                response_format={"type": "text"},
                web_search_options={"search_context_size": "high"},
            )
            return completion.choices[0].message.content
        except Exception as e:
            if retry_count == RETRY_BUDGET - 1:
                tqdm.write(f"Failed to generate summary due to error: {e}")
                return ""
            tqdm.write(f"Retrying due to error: {e}")


def build_section_dependency_graph(corpus, references_information):
    """
    Build a dependency graph from a corpus file.

    Args:
        corpus (dict): The corpus to build the graph from
        references_information (dict): The dependency graph to use for reference extraction

    Returns:
        dict: A graph in the form of a list of edges. An edge is a dictionary with the following structure:
            {
                "source": {
                    "rfc_number": str,
                    "section_id": str
                },
                "document_type": "RFC" | "EXTERNAL",
                "document_tag": "RFC_NUMBER" | "EXTERNAL_DOCUMENT_TAG",
                "reference_type": "SECTION" | "TEXT",
                "reference_value": "SECTION_ID" | "KEY PHRASE",
                "importance": "normative" | "informative" | "unknown",
                "updates": bool,
                "url": "" | "EXTERNAL_URL",
                "reference_text": "" | "EXTERNAL_DOCUMENT_REFERENCE_TEXT",
                "reference_summary": "" | "EXTERNAL_DOCUMENT_REFERENCE_SUMMARY"
            }
    """
    # Initialize the graph
    graph = []

    rfc = corpus[0]
    rfc_number = rfc["rfc_number"]
    if "structured_content" in rfc:
        process_sections_for_graph(
            rfc_number, rfc["structured_content"], graph, [], references_information
        )

    # clean the graph
    indices_to_remove = set()

    # remove duplicate edges
    for i, edge in enumerate(graph):
        for j, other_edge in enumerate(graph):
            if i < j and all(
                edge[p] == other_edge[p]
                for p in [
                    "source",
                    "document_type",
                    "document_tag",
                    "reference_type",
                    "reference_value",
                ]
            ):
                indices_to_remove.add(j)

    # remove self references
    for i, edge in enumerate(graph):
        if (
            edge["source"]["rfc_number"] == edge["document_tag"]
            and edge["source"]["section_id"] == edge["reference_value"]
        ):
            indices_to_remove.add(i)

    # execute the removals
    graph = [edge for i, edge in enumerate(graph) if i not in indices_to_remove]

    return graph


def process_sections_for_graph(rfc_number, sections, graph, updates, references):
    """
    Process sections recursively to build the graph.

    Args:
        rfc_number (str): RFC number
        sections (dict): Dictionary of sections
        graph (list): The graph being built
        updates (list): List of RFCs updated by this RFC
        references (list): List of references for this RFC
    """
    for section_id, section in sections.items():
        # Process references from decomposed_content
        if "decomposed_content" in section:
            for chunk in section["decomposed_content"]:
                if "references" in chunk and chunk["references"]:
                    for ref in chunk["references"]:
                        document_tag = __get_first_int(ref["rfc_number"])

                        # search for the reference in the references list
                        importance = "unknown"
                        for reference in references:
                            if all(
                                p in reference["tag"]
                                for p in [str(document_tag), "RFC"]
                            ):
                                importance = reference["type"]
                                break

                        graph.append(
                            {
                                "source": {
                                    "rfc_number": rfc_number,
                                    "section_id": section_id,
                                },
                                "document_type": "RFC",
                                "document_tag": str(document_tag),
                                "reference_type": "SECTION",
                                "reference_value": ref["section_id"],
                                "importance": importance,
                                "updates": document_tag in updates,
                                "url": "",
                                "reference_text": "",
                                "reference_summary": "",
                            }
                        )

                if "external_references" in chunk and chunk["external_references"]:
                    for external_ref in chunk["external_references"]:
                        document_tag = external_ref["tag"]

                        # search for the reference in the references list
                        importance, url, reference_text = "unknown", "", ""
                        for reference in references:
                            if document_tag in reference["tag"]:
                                importance = reference["type"]
                                reference_text = reference["text"]
                                if reference["links"]:
                                    # take the first link
                                    url = reference["links"][0]["address"]
                                break

                        # generate the summary
                        reference_summary = get_external_reference_summary(
                            document_tag,
                            external_ref["reference_value"],
                            external_ref["reference_type"],
                            url,
                            reference_text,
                        )

                        graph.append(
                            {
                                "source": {
                                    "rfc_number": rfc_number,
                                    "section_id": section_id,
                                },
                                "document_type": "EXTERNAL",
                                "document_tag": document_tag,
                                "reference_type": external_ref["reference_type"],
                                "reference_value": external_ref["reference_value"],
                                "importance": importance,
                                "updates": False,
                                "url": url,
                                "reference_text": reference_text,
                                "reference_summary": reference_summary,
                            }
                        )

        # Process child sections
        if "children" in section:
            process_sections_for_graph(
                rfc_number, section["children"], graph, updates, references
            )


def main(corpus_path, references_path, output_dir):
    output_path = os.path.join(output_dir, "section_dependencies.json")

    # load the corpus
    with open(corpus_path, "r") as f:
        corpus = json.load(f)

    # load the references
    with open(references_path, "r") as f:
        references = json.load(f)

    # Build the graph
    graph = build_section_dependency_graph(corpus, references)

    # Save the graph
    with open(output_path, "w") as f:
        json.dump(graph, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a section dependency graph from an RFC corpus"
    )
    parser.add_argument("corpus_path", type=str, help="Path to the corpus JSON file")
    parser.add_argument(
        "references_path", type=str, help="Path to the RFC references JSON file"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Output directory path for saving the output graph JSON file",
    )
    args = parser.parse_args()
    main(args.corpus_path, args.references_path, args.output)
