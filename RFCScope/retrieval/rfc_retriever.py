import requests
from bs4 import BeautifulSoup
from util.cache import cache
from retrieval.rfc2html import markup


def __get_first_int(s: str) -> int:
    """
    Extracts the first integer from the given string.
    """
    first_int = ''
    found_first_digit = False
    for c in s:
        if not found_first_digit and c.isdigit():
            found_first_digit = True
        if found_first_digit and c.isdigit():
            first_int += c
        elif found_first_digit:
            break
    return int(first_int)


def __clean_text(s: str) -> str:
    """
    Clean the text by converting non-ASCII characters to ASCII.
    """
    return s.replace('\u00a0', ' ')


@cache
def fetch_rfc(rfc_number: int | str) -> str:
    """
    Fetches the RFC document with the given number in HTML format.
    The HTML content is generated from the plain text version of the 
    RFC document with the rfc2html tool.
    
    :param rfc_number: The RFC number to fetch. Can be an integer or a string. 
    If it is a string, the first integer in the string will be used.
    
    :return: The HTML content of the RFC document.
    :raises: ValueError if the RFC document could not be fetched.
    """
    rfc_number = __get_first_int(str(rfc_number))
    rfc_url = f"https://www.rfc-editor.org/rfc/rfc{rfc_number}.txt"

    try:
        response = requests.get(rfc_url)
        response.raise_for_status()
        return markup(response.text)
    except Exception:
        raise ValueError(f"Failed to fetch RFC {rfc_number}.")


def __clean_word(word: str) -> str:
    if word[-1] == '.':
        return word[:-1]
    return word


def __check_word(word: str) -> bool:
    """
    Check if the word is a valid section identifier word.
    
    A valid section identifier word is of the form S(.X)*[.] where
    S is a capital letter or a number, and X is a number. 
    """
    word = __clean_word(word)
    
    parts = word.split('.')
    if not parts:
        return False

    if not parts[0].isdigit() and not (len(parts[0]) == 1 and parts[0].isupper()):
        return False

    for part in parts[1:]:
        if not part.isdigit():
            return False

    return True


def __check_heading(heading_text: str) -> str | None:
    """
    Check if the heading is a valid section heading.
    If it is, return the section identifier. Otherwise, return None.
    """
    heading_text = heading_text.strip()
    if not heading_text:
        return None

    words = [w.strip() for w in heading_text.split()]
    if len(words) < 2:
        return None

    # check if the first word is a valid section identifier
    if __check_word(words[0]):
        return __clean_word(words[0])

    # check if the first two words are 'Appendix' and a valid section identifier
    if words[0] == 'Appendix' and __check_word(words[1]):
        return __clean_word(words[1])

    return None


def __split_identifier_for_comparison(identifier: str) -> tuple:
    """
    Splits the section identifier into a tuple of integers for comparison.
    
    Letters are converted to their ASCII values (and will usually be kept
    after the numbers).
    """
    parts = identifier.split('.')
    return tuple(int(part) if part.isdigit() else ord(part) for part in parts)


def process_rfc_html(html: str, clean_legacy_sections: bool = True) -> dict:
    """
    Processes the HTML content of an RFC document to extract the text content
    in the structure of sections and subsections. The structure is as follows.
    
    {
        "section_identifier": {
            "title": "section_title",
            "content": "section_content",
            "children": {
                "section_identifier": {
                    ...
                },
                ...
            }
        },
    }

    :param html: The HTML content of the RFC document.
    :param clean_legacy_sections: Whether to clean up legacy sections. (default: True)
    :return: A nested dictionary representing the structure of the RFC document.
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    # replace all pre elements with their inner HTML
    for pre in soup.find_all('pre'):
        pre.unwrap()
        
    # remove all .grey elements and <hr> elements
    for elem in soup.select('.grey, hr'):
        elem.decompose()

    # find all h2, h3, h4, h5, h6 elements for which a valid section identifier can be extracted
    all_headings = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])

    # while most RFCs have titles of the form {section_identifier}. {section_title},
    # some legacy RFCs have titles of the form {section_identifier} - {section_title}
    # so we convert the latter to the former
    for heading in all_headings:
        # check if there is an `a.selflink` element which is followed by ' - '
        selflink = heading.select_one('a.selflink')
        if selflink and selflink.next_sibling and selflink.next_sibling.text[:3] == ' - ':
            # create a new text node with modified text
            new_text = soup.new_string(". " + selflink.next_sibling.text[3:])
            selflink.next_sibling.replace_with(new_text)

    headings = []
    for heading in all_headings:
        if __check_heading(heading.text):
            headings.append(heading)

    # if no headings could be found, short-circuit
    if not headings:
        return {}

    # TODO: remove erroneous headings, for example, remove 25 out of
    # [1, 2, 3, 25, 4], or remove 1 out of [1, 2, 3, 4, 6, 1, 7, 8]

    sections_array = []
    for heading in headings:
        # get the section identifier and title
        section_identifier = __check_heading(heading.text)
        
        # the section title is the thing after section_identifier, but we will also
        # take care of the case when the word "Appendix" is present at the start
        section_title = heading.text
        if section_title.strip().startswith("Appendix"):
            section_title = section_title.split("Appendix", 1)[1].strip()
        section_title = section_title.split(section_identifier, 1)[1][1:].strip()
        section_title = __clean_text(section_title)

        # get the section content
        # the content is the text between the heading and the next heading (all headings are siblings)
        # there may be text that is not placed in a tag.
        content = ''
        for sibling in heading.next_siblings:
            if sibling in headings:
                break
            if sibling.name is None:
                sibling_content = str(sibling)
                
                # remove leading and trailing blank lines
                lines = sibling_content.split('\n')
                non_empty_line_indices = [i for i, line in enumerate(lines) if line.strip()]
                if non_empty_line_indices:
                    start_line = min(non_empty_line_indices)
                    end_line = max(non_empty_line_indices)
                    sibling_content = '\n'.join(lines[start_line:end_line + 1])
            else:
                sibling_content = sibling.get_text()

            # if the last character of the content is not a whitespace, we should add a space
            # to the content, so that the next text will be separated by a space
            if sibling_content and content and content[-1].strip():
                # it is usually difficult to tell if this correction is to be made and so we
                # will only do it in a few cases for now
                # TODO: Is there a general rule for this?
                if content[-1].isalpha() or content[-1] in ['.']: 
                    content += ' '

            content += sibling_content
            
        # add the section to the sections array
        sections_array.append({
            'identifier': section_identifier,
            'title': section_title,
            'content': __clean_text(content),
            'children': [],
            'parent': None
        })

    if clean_legacy_sections:
        # the last section may also contain metadata like
        # contributors, acknowledgements, author addresses, etc.
        # we will remove this metadata. (this is only in newer RFCs)
        last_section_content = sections_array[-1]['content']
        lines = last_section_content.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        if non_empty_lines:
            # find the indentation of the first non-empty line
            first_non_empty_line = non_empty_lines[0]
            indentation = len(first_non_empty_line) - len(first_non_empty_line.lstrip())
            
            # check if any line has less indentation than the first non-empty line
            # if so, remove that line and all following lines
            for i, line in enumerate(lines):
                if line.strip() and len(line) - len(line.lstrip()) < indentation:
                    lines = lines[:i]
                    break

            sections_array[-1]['content'] = '\n'.join(lines)
        else:
            # if the last section is empty, remove it
            sections_array.pop()

        # the last section of some old RFCs may have an "Index" section
        # we will remove this section
        if sections_array and "\nIndex\n" in sections_array[-1]['content']:
            sections_array[-1]['content'] = sections_array[-1]['content'].split("\nIndex\n", 1)[0]

    # populate the children of each section
    for section in sections_array:
        identifier = section['identifier'].split('.')
        
        # this section is a child of the section with the longest identifier that is a prefix of this section's identifier
        # the prefix-checking is done for tuples of the identifier parts
        parent = None
        for other_section in sections_array:
            other_identifier = other_section['identifier'].split('.')
            if (
                all(x == y for x, y in zip(identifier, other_identifier)) and
                (parent is None or len(other_identifier) > len(parent['identifier'].split('.'))) and
                len(other_identifier) < len(identifier)
            ):
                parent = other_section

        if parent is not None:
            parent['children'].append(section)
            section['parent'] = parent

    # now build the tree structure from the sections array
    sections = {}

    def build_subtree(section):
        """
        Builds the subtree of the given section and returns it.
        """
        children = {}
        for child in section['children']:
            children[child['identifier']] = build_subtree(child)
        return {
            'title': section['title'],
            'content': section['content'],
            'children': children
        }

    for section in sections_array:
        if not section['parent']:
            sections[section['identifier']] = build_subtree(section)

    return sections


def get_structured_rfc(rfc_number: int | str, clean_legacy_sections: bool = True) -> dict:
    """
    Fetches the RFC document with the given number and returns its structured content.
    
    :param rfc_number: The RFC number to fetch. Can be an integer or a string. 
    If it is a string, the first integer in the string will be used.
    
    :return: The structured content of the RFC document.
    :raises: ValueError if the RFC document could not be fetched.
    """
    try:
        return process_rfc_html(fetch_rfc(rfc_number), clean_legacy_sections)
    except Exception:
        return {}


@cache
def get_rfc_title(rfc_number: int | str) -> str:
    """
    Returns the title of the RFC document with the given number.
    
    Returns an empty string if the title could not be found.
    """
    try:
        rfc_number = __get_first_int(str(rfc_number))
        rfc_info_url = f"https://www.rfc-editor.org/info/rfc{rfc_number}"
        response = requests.get(rfc_info_url)
        response.raise_for_status()
    
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # find the first .entryheader element and select the last h3 inside it
        entry_header = soup.select_one('.entryheader')
        h3 = entry_header.select('h3')[-1]
    
        # take all content in the h3 element until any other tag
        # and return the text
        title = ''
        for elem in h3.contents:
            if elem.name:
                break
            title += str(elem)
            
        title = title.strip()
        
        # remove the last comma
        if title and title[-1] == ',':
            title = title[:-1].strip()
        
        return title
    except Exception:
        return '' # return empty string if the title could not be found
