import os
import re
import json
import argparse
from typing import List, Dict, Any, Tuple, Set

try:
    from pypdf import PdfReader
except ImportError:
    raise ImportError("Please install pypdf first: pip install pypdf")


# ============================================================
# 1) Regex patterns
# ============================================================

# Real clause headings, e.g.
# 1 Scope
# 4.2 RLC architecture
# 5.1.3 RLC entity release
CLAUSE_HEADING_RE = re.compile(
    r"^(?P<id>\d+(?:\.\d+)*)(?:\s+)(?P<title>[A-Z][^\n]{0,200})$"
)

# TOC-like line detection:
# 1 Scope .................... 6
# 4.2 RLC architecture ...... 7
TOC_LINE_RE_1 = re.compile(r"\.{5,}")
TOC_LINE_RE_2 = re.compile(r"\s\.{2,}\s*\d+\s*$")

# Internal clause refs
INTERNAL_REF_PATTERNS = [
    re.compile(r"\bclause\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE),
    re.compile(r"\bsubclause\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE),
    re.compile(r"\bsee\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE),
    re.compile(r"\baccording to\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE),
    re.compile(r"\bin\s+clause\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE),
    re.compile(r"\bunder\s+clause\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE),
]

# External refs:
# 3GPP TS 38.323
# 3GPP TR 21.905
# ETSI TS 138 322
# TS 38.323
# TR 21.905
EXTERNAL_REF_PATTERNS = [
    re.compile(r"\b3GPP\s+TS\s+(\d+\.\d+)\b", re.IGNORECASE),
    re.compile(r"\b3GPP\s+TR\s+(\d+\.\d+)\b", re.IGNORECASE),
    re.compile(r"\bETSI\s+TS\s+(\d+\s+\d+\s+\d+)\b", re.IGNORECASE),
    re.compile(r"\bTS\s+(\d+\.\d+)\b", re.IGNORECASE),
    re.compile(r"\bTR\s+(\d+\.\d+)\b", re.IGNORECASE),
]

FIGURE_CAPTION_RE = re.compile(
    r"^Figure\s+\d+(?:\.\d+)*-\d+\s*:\s*.+$",
    re.IGNORECASE
)

# Figure start without caption
FIGURE_START_RE = re.compile(
    r"^Figure\s+\d+(?:\.\d+)*-\d+\b",
    re.IGNORECASE
)


# ============================================================
# 2) Utilities
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_json(obj: Any, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def normalize_whitespace(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def get_clause_level(clause_id: str) -> int:
    return clause_id.count(".") + 1


def get_parent_clause_id(clause_id: str) -> str:
    if "." not in clause_id:
        return ""
    return clause_id.rsplit(".", 1)[0]


def sort_clause_ids(ids: Set[str]) -> List[str]:
    return sorted(ids, key=lambda x: [int(p) for p in x.split(".")])


def is_toc_line(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if TOC_LINE_RE_1.search(line):
        return True
    if TOC_LINE_RE_2.search(line):
        return True
    return False


def looks_like_front_matter_noise(line: str) -> bool:
    bad_keywords = [
        "Route des",
        "Cedex",
        "FRANCE",
        "Tel.:",
        "Siret",
        "Sous-Préfecture",
        "Important notice",
        "Legal Notice",
        "Modal verbs terminology",
        "Intellectual Property Rights",
    ]
    low = line.lower()
    return any(k.lower() in low for k in bad_keywords)


# ============================================================
# 3) Text cleaning
# ============================================================

def remove_header_footer_lines(lines: List[str]) -> List[str]:
    cleaned = []

    for line in lines:
        s = line.strip()

        if not s:
            cleaned.append("")
            continue

        # Common ETSI header/footer noise
        if s == "ETSI":
            continue
        if "ETSI TS 138 322 V19.0.0" in s:
            continue
        if "3GPP TS 38.322 version 19.0.0 Release 19" in s:
            continue

        # Combined compressed header/footer line
        if re.search(
            r"ETSI TS 138 322 V19\.0\.0.*3GPP TS 38\.322 version 19\.0\.0 Release 19",
            s
        ):
            continue

        cleaned.append(s)

    return cleaned


def remove_figure_noise(lines: List[str]) -> List[str]:
    """
    Keep figure captions like:
      Figure 4.2.1-1: Overview model of the RLC sub layer
    Remove scattered figure drawing labels between a figure start and caption.
    """
    cleaned = []
    in_figure_block = False

    for line in lines:
        s = line.strip()

        if not s:
            if not in_figure_block:
                cleaned.append("")
            continue

        if FIGURE_CAPTION_RE.match(s):
            cleaned.append(s)
            in_figure_block = False
            continue

        if FIGURE_START_RE.match(s) and not FIGURE_CAPTION_RE.match(s):
            in_figure_block = True
            continue

        # If we are inside a figure block, skip lines until caption
        if in_figure_block:
            continue

        cleaned.append(s)

    return cleaned


def clean_page_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\u00ad", "")  # soft hyphen
    text = text.replace("‐", "-")
    text = text.replace("–", "-")
    text = text.replace("—", "-")

    # Join hyphenated line breaks:
    # retransmis-\nsion -> retransmission
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    lines = [line.strip() for line in text.splitlines()]
    lines = remove_header_footer_lines(lines)
    lines = remove_figure_noise(lines)

    text = "\n".join(lines)
    text = normalize_whitespace(text)
    return text


# ============================================================
# 4) PDF parsing
# ============================================================

def extract_pdf_pages(pdf_path: str) -> List[Dict[str, Any]]:
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages):
        raw = page.extract_text() or ""
        cleaned = clean_page_text(raw)
        pages.append({
            "page_num": i + 1,
            "text": cleaned
        })

    return pages


def merge_pages_to_document(pages: List[Dict[str, Any]]) -> str:
    return "\n\n".join(page["text"] for page in pages if page["text"].strip())


# ============================================================
# 5) Clause extraction
# ============================================================

def detect_clause_headings(lines: List[str]) -> List[Tuple[int, str, str]]:
    headings = []

    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        if is_toc_line(line):
            continue

        m = CLAUSE_HEADING_RE.match(line)
        if not m:
            continue

        clause_id = m.group("id").strip()
        title = m.group("title").strip()

        if len(title) < 2:
            continue

        # Skip obvious front page/address artifacts like "650 Route des Lucioles"
        if clause_id.isdigit() and int(clause_id) > 100:
            continue

        if looks_like_front_matter_noise(line):
            continue

        headings.append((i, clause_id, title))

    return headings


def build_clause_tree(document_text: str) -> List[Dict[str, Any]]:
    lines = document_text.splitlines()
    headings = detect_clause_headings(lines)

    if not headings:
        raise ValueError(
            "No clause headings detected. You may need to adjust CLAUSE_HEADING_RE."
        )

    # Start only from the first real clause 1
    start_idx = None
    for idx, (line_idx, clause_id, title) in enumerate(headings):
        if clause_id == "1":
            start_idx = idx
            break

    if start_idx is None:
        raise ValueError("Could not find the first real clause '1'.")

    headings = headings[start_idx:]

    clauses = []

    for idx, (start_line, clause_id, title) in enumerate(headings):
        end_line = headings[idx + 1][0] if idx + 1 < len(headings) else len(lines)

        raw_block = "\n".join(lines[start_line:end_line]).strip()

        content_lines = lines[start_line + 1:end_line]
        content = "\n".join(content_lines).strip()
        content = normalize_whitespace(content)

        clause = {
            "clause_id": clause_id,
            "title": title,
            "level": get_clause_level(clause_id),
            "parent_clause_id": get_parent_clause_id(clause_id),
            "raw_block": raw_block,
            "text": content,
            "children": [],
        }
        clauses.append(clause)

    id_to_clause = {c["clause_id"]: c for c in clauses}
    for clause in clauses:
        parent_id = clause["parent_clause_id"]
        if parent_id and parent_id in id_to_clause:
            id_to_clause[parent_id]["children"].append(clause["clause_id"])

    return clauses


# ============================================================
# 6) Reference extraction
# ============================================================

def extract_internal_refs(
    text: str,
    valid_clause_ids: Set[str],
    current_clause_id: str
) -> List[str]:
    refs = set()

    # First, capture explicit clause-style references
    for pattern in INTERNAL_REF_PATTERNS:
        for match in pattern.finditer(text):
            ref = match.group(1).strip()
            if ref in valid_clause_ids and ref != current_clause_id:
                refs.add(ref)

    # Then, fallback to naked clause-like ids, but avoid figure numbers
    for match in re.finditer(r"\b(\d+(?:\.\d+)+)\b", text):
        ref = match.group(1).strip()

        if ref not in valid_clause_ids:
            continue
        if ref == current_clause_id:
            continue

        # Skip if it appears as a figure/table numbering prefix, e.g.
        # Figure 4.2.1-1
        # Table 5.1.2-3
        figure_like = re.search(
            rf"\b(?:Figure|Table)\s+{re.escape(ref)}-\d+\b",
            text,
            re.IGNORECASE
        )
        if figure_like:
            continue

        refs.add(ref)

    return sort_clause_ids(refs)


def normalize_external_ref(raw_match: str, pattern_index: int) -> str:
    """
    Normalize reference strings into a consistent style.
    """
    raw = raw_match.strip()

    if pattern_index == 0:
        # 3GPP TS x.y
        return raw.upper().replace("3GPP TS", "3GPP TS")
    elif pattern_index == 1:
        # 3GPP TR x.y
        return raw.upper().replace("3GPP TR", "3GPP TR")
    elif pattern_index == 2:
        # ETSI TS 138 322
        return raw.upper().replace("ETSI TS", "ETSI TS")
    elif pattern_index == 3:
        num = re.search(r"TS\s+(\d+\.\d+)", raw, re.IGNORECASE).group(1)
        return f"3GPP TS {num}"
    elif pattern_index == 4:
        num = re.search(r"TR\s+(\d+\.\d+)", raw, re.IGNORECASE).group(1)
        return f"3GPP TR {num}"

    return raw


def extract_external_refs(text: str) -> List[str]:
    refs = set()

    for idx, pattern in enumerate(EXTERNAL_REF_PATTERNS):
        for match in pattern.finditer(text):
            refs.add(normalize_external_ref(match.group(0), idx))

    return sorted(refs)


# ============================================================
# 7) Corpus + dependencies
# ============================================================

def generate_corpus(
    clauses: List[Dict[str, Any]],
    spec_id: str,
) -> List[Dict[str, Any]]:
    valid_clause_ids = {c["clause_id"] for c in clauses}

    corpus = []
    for clause in clauses:
        internal_refs = extract_internal_refs(
            text=clause["text"],
            valid_clause_ids=valid_clause_ids,
            current_clause_id=clause["clause_id"]
        )
        external_refs = extract_external_refs(clause["text"])

        item = {
            "doc_type": "3GPP_TS",
            "spec_id": spec_id,
            "clause_id": clause["clause_id"],
            "title": clause["title"],
            "level": clause["level"],
            "parent_clause_id": clause["parent_clause_id"],
            "children": clause["children"],
            "text": clause["text"],
            "internal_refs": internal_refs,
            "external_refs": external_refs,
        }
        corpus.append(item)

    return corpus


def build_section_dependencies(corpus: List[Dict[str, Any]]) -> Dict[str, Any]:
    graph = {
        "nodes": [],
        "edges": []
    }

    for item in corpus:
        graph["nodes"].append({
            "id": item["clause_id"],
            "title": item["title"],
            "level": item["level"],
        })

        for ref in item["internal_refs"]:
            graph["edges"].append({
                "source": item["clause_id"],
                "target": ref,
                "type": "internal_clause_reference"
            })

        if item["parent_clause_id"]:
            graph["edges"].append({
                "source": item["clause_id"],
                "target": item["parent_clause_id"],
                "type": "parent_clause"
            })

    return graph


# ============================================================
# 8) Main
# ============================================================

def main(pdf_path: str, output_dir: str, spec_id: str) -> None:
    ensure_dir(output_dir)

    print("Preparing 3GPP spec for analysis.")
    print(f"PDF: {pdf_path}")
    print(f"Output directory: {output_dir}")
    print(f"Spec ID: {spec_id}")

    print("\n[Step 1] Extracting text from PDF ...")
    pages = extract_pdf_pages(pdf_path)
    raw_text_path = os.path.join(output_dir, "raw_text.json")
    save_json(pages, raw_text_path)
    print(f"Saved raw page text to: {raw_text_path}")

    print("\n[Step 2] Merging pages into a single document ...")
    document_text = merge_pages_to_document(pages)

    print("\n[Step 3] Detecting clause headings and building clause tree ...")
    clauses = build_clause_tree(document_text)
    clause_tree_path = os.path.join(output_dir, "clause_tree.json")
    save_json(clauses, clause_tree_path)
    print(f"Detected {len(clauses)} clauses.")
    print(f"Saved clause tree to: {clause_tree_path}")

    print("\n[Step 4] Generating corpus ...")
    corpus = generate_corpus(clauses, spec_id)
    corpus_path = os.path.join(output_dir, "corpus.json")
    save_json(corpus, corpus_path)
    print(f"Saved corpus to: {corpus_path}")

    print("\n[Step 5] Building section dependency graph ...")
    section_dependencies = build_section_dependencies(corpus)
    deps_path = os.path.join(output_dir, "section_dependencies.json")
    save_json(section_dependencies, deps_path)
    print(f"Saved section dependencies to: {deps_path}")

    print("\nDone.")
    print("Generated files:")
    print(f"  - {raw_text_path}")
    print(f"  - {clause_tree_path}")
    print(f"  - {corpus_path}")
    print(f"  - {deps_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Stage a 3GPP/ETSI PDF for analysis by constructing clause-level context."
    )
    parser.add_argument(
        "--pdf",
        type=str,
        required=True,
        help="Path to the ETSI-published PDF file"
    )
    parser.add_argument(
        "--out",
        type=str,
        required=True,
        help="Directory where staged files will be written"
    )
    parser.add_argument(
        "--spec",
        type=str,
        default="38.322",
        help="Specification identifier, e.g. 38.322"
    )

    args = parser.parse_args()

    main(
        pdf_path=args.pdf,
        output_dir=args.out,
        spec_id=args.spec,
    )