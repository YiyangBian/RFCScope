import os
import json
import time
import re
from openai import OpenAI
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv
from rapidfuzz import fuzz, process
from bs4 import BeautifulSoup
from util import cache
from retrieval.rfc_retriever import get_structured_rfc, __get_first_int
from retrieval.rfc2html import markup

load_dotenv()
OpenAIClient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Retry budget for reprompting in case of failure
RETRY_BUDGET = 3

SYSTEM_PROMPT = """You are an expert in networking and have extensive experience writing RFC (Request for Comments) documents related to Internet protocol standards. I am reading a text from or about an RFC document and need your help in extracting all the references from the text. You will help me identify and extract references to sections within the same RFC, other RFCs or their sections, or external documents, as mentioned in the text. Each reference has the following format.

```json
{
    "document_type": "<enum: RFC or EXTERNAL>",
    "document_tag": "<RFC NUMBER (eg. RFC1234) OR EXTERNAL DOCUMENT TAG (eg. IEEE.1234)>",
    "reference_type": "<enum: SECTION or TEXT>",
    "reference_value": "<SECTION_IDENTIFIER or SEARCH_KEYWORDS>"
}
```

The `reference_type` is `SECTION` if a section is explicitly mentioned. In that case, the `reference_value` is the identifier of the section (for example, "1", "2.3", "4.5.6", "7.8.9.10", "A", "B.1", etc.). If no section is explicitly mentioned, `reference_type` is `TEXT` and the `reference_value` contains search keywords that I can use to search the referenced RFC for the relevant text. The search should be made of words that are present in the referenced text and can be used to identify the referenced section (for example, names of entities, topics, rules, etc.).

If a section is referenced without mentioning an RFC number, it probably belongs to the same RFC as the provided text. **Do NOT forget to include references to such sections.** If the given text contains an excerpt or a blockquote from another document, you should consider it as a reference to that document.

Take a deep breath, carefully read the text line-by-line, clause-by-clause, phrase-by-phrase, and provide all references properly."""

USER_QUERY = """Consider the following excerpt from RFC 1234.

```
2.3 A section

This specification uses the foo notation of [RFC2345] along with the
egg rule defined in section 3 of [RFC3456]. Alternatively, one can
use the protocol in section 4.5, which is similar to the foobar 
protocol defined in [IEEE.802.11].
```"""

MODEL_RESPONSE = """```json
{
  "response": [
    {
      "document_type": "RFC",
      "document_tag": "RFC1234",
      "reference_type": "SECTION",
      "reference_value": "2.3"
    },
    {
      "document_type": "RFC",
      "document_tag": "RFC2345",
      "reference_type": "TEXT",
      "reference_value": "foo notation"
    },
    {
      "document_type": "RFC",
      "document_tag": "RFC3456",
      "reference_type": "SECTION",
      "reference_value": "3"
    },
    {
      "document_type": "RFC",
      "document_tag": "RFC1234",
      "reference_type": "SECTION",
      "reference_value": "4.5"
    },
    {
      "document_type": "EXTERNAL",
      "document_tag": "IEEE.802.11",
      "reference_type": "TEXT",
      "reference_value": "foobar protocol"
    }
  ]
}
```"""

@cache(SYSTEM_PROMPT, USER_QUERY, MODEL_RESPONSE)
def __get_references_openai(text: str) -> list[dict[str, str]]:
    for retry_count in range(RETRY_BUDGET):
        try:
            response = OpenAIClient.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": [
                            {
                                "type": "text",
                                "text": SYSTEM_PROMPT
                            }
                        ]
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": USER_QUERY
                            }
                        ]
                    },
                    {
                        "role": "assistant",
                        "content": [
                            {
                                "type": "text",
                                "text": MODEL_RESPONSE
                            }
                        ]
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": text
                            }
                        ]
                    }
                ],
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "response_schema",
                        "strict": True,
                        "schema": {
                                "type": "object",
                                "properties": {
                                    "response": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "document_type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "RFC",
                                                        "EXTERNAL"
                                                    ]
                                                },
                                                "document_tag": {
                                                    "type": "string"
                                                },
                                                "reference_type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "SECTION",
                                                        "TEXT"
                                                    ]
                                                },
                                                "reference_value": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "document_type",
                                                "document_tag",
                                                "reference_type",
                                                "reference_value"
                                            ],
                                            "additionalProperties": False
                                    }
                                }
                            },
                            "required": ["response"],
                            "additionalProperties": False
                        }
                    }
                },
                temperature=1,
                max_completion_tokens=8192,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                store=False
            )
            return json.loads(response.choices[0].message.content, strict=False)["response"]
        except Exception as e:
            if retry_count == RETRY_BUDGET - 1:
                raise ValueError("Failed to extract references:", e) from e
            time.sleep(3) # Wait for 3 seconds before retrying


def is_reference_from_rfc(reference: dict, reference_information: list[dict]) -> None | str:
    """
    Check if the reference is from an RFC, even though it may be
    marked as EXTERNAL. `reference` should be an EXTERNAL reference.
    
    If not, return None. If it is, return the RFC number as a string.
    """
    # the document tag may hint at the RFC
    if "RFC" in reference["document_tag"]:
        try:
            # get the rfc number from the document tag
            return str(__get_first_int(reference["document_tag"]))
        except Exception:
            return None

    # it is also possible that the URL of the "external" reference is
    # actually linking to an RFC.
    if reference_information:
        matching_refs = [ref for ref in reference_information if ref["tag"] == reference["document_tag"]]
        if matching_refs:
            # get the first matching reference
            matching_ref = matching_refs[0]
            
            if matching_ref["links"]:
                # take the first link
                url = matching_ref["links"][0]["address"]
                
                if "RFC" in url.upper():
                    # get the rfc number from the url
                    try:
                        return str(__get_first_int(url))
                    except Exception:
                        return None

                elif "BCP" in url.upper():
                    # sometimes a BCP may be referenced instead of a particular RFC
                    # but we can possibly extract the RFC number from the citation text
                    
                    citation_text = matching_ref["text"]
                    
                    # search for "RFC{nothing or a single non-digit character}\d+" in the citation text
                    # and get the first occurrence
                    search = re.search(r'RFC[^\d]?\d+', citation_text)
                    
                    if search:
                        search_result = search.group(0)
                        try:
                            return str(__get_first_int(search_result))                            
                        except Exception:
                            return None

    return None


def get_references(text: str, reference_information: list[dict] = None) -> list[dict[str, str]]:
    """
    Get the references to other RFCs in the given text.
    The response has the following format:
    
    [
        {
            "document_type": "...", # RFC or EXTERNAL
            "document_tag": "...", # RFC NUMBER or EXTERNAL DOCUMENT TAG
            "reference_type": "...", # SECTION or TEXT
            "reference_value": "..." # SECTION_IDENTIFIER or SEARCH_TEXT
        },
    ]

    It is recommended that the text starts with information about the RFC it is taken from.
    
    :param text: The text to analyze.
    :param reference_information: A list of dictionaries containing the reference information.
    If provided, it is used to enhance the classification of the extracted references.
    :return: A list of references to other RFCs in the text.
    :raises: ValueError if the model fails to generate a response.
    """
    references_list = __get_references_openai(text)

    # process the references to reclassify EXTERNAL references
    # which are actually RFCs
    for reference in references_list:
        if reference["document_type"] == "EXTERNAL":
            rfc_number = is_reference_from_rfc(reference, reference_information)
            if rfc_number:
                reference["document_type"] = "RFC"
                reference["document_tag"] = f"RFC{rfc_number}"

    return references_list


def __get_flat_sections_list(sections: dict) -> list[dict]:
    """
    Get a flat list of sections from the structured RFC.
    """
    sections_list = []
    for section in sections:
        sections_list.append({
            "identifier": section,
            "title": sections[section]["title"],
            "content": sections[section]["content"],
            "children": list(sections[section]["children"].keys())
        })
        sections_list.extend(__get_flat_sections_list(sections[section]["children"]))
    return sections_list


def __find_section(sections: dict, section_identifier: str) -> dict:
    """
    Find a section in the structured RFC based on the section identifier.
    """
    if section_identifier in sections:
        return sections[section_identifier]
    for section in sections:
        found_section = __find_section(sections[section]["children"], section_identifier)
        if found_section:
            return found_section
    return None


def __create_langchain_documents_from_rfc(structured_rfc: dict) -> InMemoryVectorStore:
    """
    Given a structured RFC, return a vector store containing all the sections as documents.
    """
    flattened_sections = __get_flat_sections_list(structured_rfc)
    documents = []
    for section in flattened_sections:
        documents.append(Document(
            page_content=section["title"] + "\n\n" + section["content"],
            metadata={
                "identifier": section["identifier"]
            }
        ))

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = InMemoryVectorStore(embeddings)
    
    vector_store.add_documents(documents=all_splits)

    return vector_store


def __process_section_reference(reference: dict, rfc_number: str, reference_rfc: dict) -> dict[str, dict[str, dict]]:
    # first try to perform an exact search for the 'reference_value' in the RFC section identifiers
    choices = [section["identifier"].strip() for section in __get_flat_sections_list(reference_rfc)]
    reference["reference_value"] = reference["reference_value"].strip()
    
    if reference["reference_value"] in choices:
        selected_section = reference["reference_value"]

    else:
        # otherwise, resort to a fuzzy search
        selected_section = process.extractOne(reference["reference_value"], choices, scorer=fuzz.ratio)[0]

    section = __find_section(reference_rfc, selected_section)

    return {
        rfc_number: {
            selected_section: {
                "title": section["title"],
                "content": section["content"]
            }
        }
    }


@cache
def __process_text_reference(reference: dict, rfc_number: str, reference_rfc: dict) -> dict[str, dict[str, dict]]:
    # do a semantic search for the 'reference_value' in the RFC sections
    vector_store = __create_langchain_documents_from_rfc(reference_rfc)
    search_results = vector_store.similarity_search(reference["reference_value"])

    # if no search results are found, return an empty dictionary
    if not search_results:
        return {} # no results found if the keyword is not present in the RFC!

    selected_section_identifier = search_results[0].metadata["identifier"]
    section = __find_section(reference_rfc, selected_section_identifier)

    return {
        rfc_number: {
            selected_section_identifier: {
                "title": section["title"],
                "content": section["content"]
            }
        }
    }


def process_reference(reference: dict) -> dict[str, dict[str, dict]]:
    """
    Process a single reference to another RFC. The reference is a dictionary
    with the following format.
    
    {        
        "document_type": "...", # RFC or EXTERNAL
        "document_tag": "...",
        "reference_type": "...", # SECTION or TEXT
        "reference_value": "..." # SECTION_IDENTIFIER or SEARCH_TEXT
    }
    
    External references are not handled by this function and return an empty dictionary.
    
    :param reference: A dictionary containing the reference information.
    :return: A dictionary with the reference text extracted from the RFC. The dictionary
    has the following format.
    
    {
        "rfc_number": {
            "section_identifier": {
                "title": "...",
                "content": "..."
            }
        }
    }
    """
    if reference["document_type"] == "RFC":
        rfc_number = reference["document_tag"]
        reference_rfc = get_structured_rfc(rfc_number)

        if reference["reference_type"] == "SECTION":
            try:
                return __process_section_reference(reference, rfc_number, reference_rfc)
            except Exception:
                return {} # some exception occurred

        if reference["reference_type"] == "TEXT":
            try:
                return __process_text_reference(reference, rfc_number, reference_rfc)
            except Exception:
                return {} # some exception occurred

        return {} # invalid reference type

    else: 
        return {}# this function does not handle external references


def collect_all_reference_texts(references: list[dict[str, str]]) -> dict[str, dict[str, dict]]:
    """
    Collect all reference texts from the list of references. The returned dictionary
    is a flattened section structure without children.
    
    The `reference_information` parameter is used to provide additional information
    about the references. This is supposed to be a list of references obtained from the 
    dependency graph of the RFC. The function will use this information to enhance the
    search for references in the given text.
    """
    reference_texts = {}
    for reference in references:
        processed_reference = process_reference(reference)
        
        for rfc_number in processed_reference:
            if rfc_number in reference_texts:
                reference_texts[rfc_number].update(processed_reference[rfc_number])
            else:
                reference_texts[rfc_number] = processed_reference[rfc_number]

    return reference_texts


def get_references_from_text(text: str) -> tuple[list[dict[str, str]], dict[str, dict[str, dict]]]:
    """
    Get a list of references and a dictionary containing the reference texts
    from the given text.
    
    This function is not intended for direct use. It is suggested that you
    use get_references_from_rfc_excerpt or get_references_from_erratum instead.
    """
    refs = get_references(text)
    ref_texts = collect_all_reference_texts(refs)
    return refs, ref_texts


def __search_for_section_references(excerpt_text: str) -> list[str]:
    """
    Search for section references in the given excerpt text.
    
    Returns a list of references found in the text.
    """
    # provide the excerpt to rfc2html to get the HTML content
    html = markup(excerpt_text)
    soup = BeautifulSoup(html, 'html.parser')
    
    # look at all <a> tags which contain "#section-" in their href
    section_refs = []
    for a in soup.find_all('a'):
        href = a.get('href')
        if href and "#section-" in href:
            section_refs.append(href)

    refs = []
    for ref in section_refs:
        section_identifier = ref.split("#section-", 1)[-1].strip()
        
        # the source RFC in the hyperlink is not reliable
        # and so we leave it as a placeholder to let the model decide
        refs.append(f"Section {section_identifier} of RFC <PLEASE FIGURE OUT THE RFC NUMBER>")

    return refs


def get_references_from_rfc_excerpt(rfc_number: str, excerpt_text: str, references: dict = None) -> tuple[list[dict[str, str]], dict[str, dict[str, dict]]]:
    """
    Get the references from the given RFC excerpt. The function returns a tuple
    containing the references and the reference texts.
    
    If the `references` is provided, references in the given RFC are available are
    used to enhance the prompt by including the list of references to look for.
    """
    prompt = f"Consider the following excerpt from RFC {rfc_number}.\n\n```\n{excerpt_text}\n```"
    
    # enhance the prompt by including the list of references to look for
    references_to_look_for = []

    # look for any section identifiers
    references_to_look_for.extend(__search_for_section_references(excerpt_text))
    
    # if the dependency graph is provided, check for all external references

    # get all reference tags
    reference_tags = [ref["tag"] for ref in references]
    
    # now check which of these references are present in the excerpt
    reference_tags_present = list(filter(lambda ref: ref in excerpt_text, reference_tags))
    
    references_to_look_for.extend([
        f"{ref['tag']} ({ref['text']})"
        for ref in references
        if ref["tag"] in reference_tags_present
    ])

    # if no references are found, we can short-circuit and return empty results
    if not references_to_look_for:
        return [], {}

    # now we can enhance the prompt by including the list of references to look for
    prompt += "\n\nThe following reference tags are present in the excerpt and you should restrict your search to these references:\n\n" + "\n".join([
        f"* {ref}" for ref in references_to_look_for
    ])
    
    # some more instructions
    prompt += "\n\n**Please DO NOT include any other references in your response.**"

    refs = get_references(prompt, references)
    ref_texts = collect_all_reference_texts(refs)
    return refs, ref_texts


def get_references_from_erratum(rfc_number: str, erratum_text: str) -> tuple[list[dict[str, str]], dict[str, dict[str, dict]]]:
    """
    Get the references from the given RFC erratum. The function returns a tuple
    containing the references and the reference texts.
    """
    refs = get_references(f"Consider the following erratum for RFC {rfc_number}.\n\n```\n{erratum_text}\n```")
    ref_texts = collect_all_reference_texts(refs)
    return refs, ref_texts
