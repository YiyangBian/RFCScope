import tiktoken
from utils.references import __get_flat_sections_list

encoding = tiktoken.encoding_for_model("o3-mini")


def build_dependency_dict(section_dependencies, corpus):
    """
    Build a dictionary of dependencies from the section dependencies list. The
    dictionary is closed in the sense that it includes all sections of all RFCs
    in the corpus, even if they have no dependencies (i.e., the dependency list is
    an empty list).

    Args:
        section_dependencies (list): List of section dependencies
        corpus (list): List of RFC documents

    Returns:
        dict: Dictionary mapping source nodes to their RFC dependencies
    """
    dependency_dict = {}

    for dep in section_dependencies:
        source = (dep["source"]["rfc_number"], dep["source"]["section_id"])
        if source not in dependency_dict:
            dependency_dict[source] = []

        if dep["document_type"] == "RFC":
            target = ("RFC", dep["document_tag"], dep["reference_value"])

            if target not in dependency_dict[source]:
                dependency_dict[source].append(target)

        if dep["document_type"] == "EXTERNAL":
            if dep["reference_text"]:
                target_name = f"{dep['reference_text']} ({dep['document_tag']})"
            else:
                target_name = dep["document_tag"]
            target = ("EXTERNAL", target_name, dep["reference_summary"])

            if target not in dependency_dict[source]:
                dependency_dict[source].append(target)

    # take the closure of the dependency dict
    for rfc in corpus:
        rfc_number = rfc["rfc_number"]
        sections_list = __get_flat_sections_list(rfc["structured_content"])

        for section in sections_list:
            section_id = section["identifier"]
            if (rfc_number, section_id) not in dependency_dict:
                dependency_dict[(rfc_number, section_id)] = []

    return dependency_dict
