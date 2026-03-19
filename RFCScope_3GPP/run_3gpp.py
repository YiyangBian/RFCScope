import os
import re
import json
import argparse
from typing import List, Dict, Any


# ============================================================
# 1) Utilities
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_json(obj: Any, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_text(text: str) -> str:
    text = (text or "").replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def make_snippet(text: str, max_len: int = 320) -> str:
    text = normalize_text(text)
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip() + " ..."


def truncate_for_context(text: str, max_chars: int = 1200) -> str:
    text = normalize_text(text)
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + " ...[TRUNCATED]"


# ============================================================
# 2) Candidate filtering + clause typing
# ============================================================

EXCLUDED_TITLE_KEYWORDS = {
    "scope",
    "references",
    "definitions",
    "abbreviations",
}

NORMATIVE_TERMS = [
    "shall",
    "should",
    "may",
    "when",
    "if",
    "upon",
    "must",
]

ACTION_VERBS = [
    "establish",
    "release",
    "reset",
    "stop",
    "discard",
    "deliver",
    "detect",
    "reassemble",
    "segment",
    "include",
    "request",
    "submit",
    "receive",
    "generate",
    "set",
    "follow",
    "fit",
    "support",
    "start",
    "update",
    "maintain",
    "place",
    "consider",
    "indicate",
    "interpret",
]

PROCEDURAL_TITLE_HINTS = [
    "establishment",
    "re-establishment",
    "release",
    "receiving",
    "transmitting",
    "procedures",
    "handling",
    "side",
    "actions",
    "expiry",
    "retransmission",
]

DEPENDENCY_HINT_PATTERNS = [
    re.compile(r"\bfollow the procedures in clause\s+\d+(?:\.\d+)*\b", re.IGNORECASE),
    re.compile(r"\bas defined in\s+TS\s+\d+\.\d+\b", re.IGNORECASE),
    re.compile(r"\bas specified in clause\s+\d+(?:\.\d+)*\b", re.IGNORECASE),
    re.compile(r"\bsee clause\s+\d+(?:\.\d+)*\b", re.IGNORECASE),
]

PARAMETER_HINT_WORDS = [
    "timer",
    "timers",
    "state variable",
    "state variables",
    "initial value",
    "initial values",
    "configuration",
    "configured",
    "counter",
    "counters",
]

IMPLEMENTATION_PATTERNS = [
    re.compile(r"\bup to [a-z0-9\- ]+ implementation\b", re.IGNORECASE),
    re.compile(r"\bimplementation specific\b", re.IGNORECASE),
    re.compile(r"\bimplementation-dependent\b", re.IGNORECASE),
    re.compile(r"\bimplementation dependent\b", re.IGNORECASE),
    re.compile(r"\bdetails are left up to [a-z0-9\- ]+ implementation\b", re.IGNORECASE),
]

FIELD_TITLE_HINTS = [
    "field",
    "fields",
]

CONSTANT_TITLE_HINTS = [
    "constant",
    "constants",
]

FORMAT_TITLE_HINTS = [
    "format",
    "formats",
    "pdu format",
]

SUPPORTING_SEMANTICS_HINTS = [
    "state variables",
    "timers",
    "configurable parameters",
]

ARCHITECTURE_TITLE_HINTS = [
    "architecture",
    "entities",
    "services",
    "functions",
    "introduction",
    "general",
]

# Inconsistency-oriented lexical hints
OBJECT_MIX_PATTERNS = [
    re.compile(r"\bsn of the corresponding rlc sdu\b", re.IGNORECASE),
    re.compile(r"\bpositive acknowledgement for an rlc sdu\b", re.IGNORECASE),
    re.compile(r"\bnegative acknowledgement for an rlc sdu\b", re.IGNORECASE),
    re.compile(r"\bamd pdu\b.*\brlc sdu\b", re.IGNORECASE),
    re.compile(r"\bumd pdu\b.*\brlc sdu\b", re.IGNORECASE),
    re.compile(r"\bincluding the rlc header\b", re.IGNORECASE),
]

WRONG_REFERENCE_STYLE_PATTERNS = [
    re.compile(r"\bsee clauses?\s+\d+(?:\.\d+)*\s+and\s+TS\s+\d+\.\d+\b", re.IGNORECASE),
]

CONFLICT_TERM_GROUPS = [
    ("discard", "deliver"),
    ("reset", "retain"),
    ("start", "stop"),
]


def contains_normative_signal(text: str) -> bool:
    low = text.lower()
    return any(term in low for term in NORMATIVE_TERMS)


def looks_excluded_title(title: str) -> bool:
    low = title.lower().strip()
    return any(k == low or k in low for k in EXCLUDED_TITLE_KEYWORDS)


def count_bullets(text: str) -> int:
    return len(re.findall(r"(?m)^\s*-\s+", text))


def has_action_verb(text: str) -> bool:
    low = text.lower()
    return any(re.search(rf"\b{re.escape(v)}\b", low) for v in ACTION_VERBS)


def has_dependency_signal(text: str) -> bool:
    for pat in DEPENDENCY_HINT_PATTERNS:
        if pat.search(text):
            return True
    return False


def has_implementation_signal(text: str) -> bool:
    return any(p.search(text) for p in IMPLEMENTATION_PATTERNS)


def infer_clause_type(item: Dict[str, Any]) -> str:
    title = item.get("title", "").lower().strip()
    text = normalize_text(item.get("text", "")).lower()

    if any(h in title for h in CONSTANT_TITLE_HINTS):
        return "constant_definition"

    if any(h in title for h in FIELD_TITLE_HINTS):
        return "field_definition"

    if any(h in title for h in FORMAT_TITLE_HINTS):
        return "format_definition"

    if any(h == title for h in SUPPORTING_SEMANTICS_HINTS):
        return "supporting_semantics"

    if title == "general":
        parent = item.get("parent_clause_id", "")
        if parent.startswith(("5.", "6.", "7.")):
            return "procedural"
        return "architecture_overview"

    if any(h in title for h in PROCEDURAL_TITLE_HINTS):
        return "procedural"

    if "shall" in text or "when " in text or "upon " in text or "if " in text:
        return "procedural"

    if any(h in title for h in ARCHITECTURE_TITLE_HINTS):
        return "architecture_overview"

    if item.get("external_refs") or item.get("internal_refs"):
        return "reference_heavy"

    return "descriptive"


def infer_tags(item: Dict[str, Any]) -> List[str]:
    text = normalize_text(item.get("text", ""))
    low = text.lower()
    tags = []

    if has_implementation_signal(text):
        tags.append("implementation_defined")

    if has_dependency_signal(text) or item.get("internal_refs"):
        tags.append("cross_clause_dependency")

    if any(word in low for word in PARAMETER_HINT_WORDS):
        tags.append("state_or_timer_dependency")

    if count_bullets(text) > 0:
        tags.append("has_bullets")

    if "figure " in low:
        tags.append("contains_figure_caption")

    return tags


def infer_priority(item: Dict[str, Any]) -> str:
    text = normalize_text(item.get("text", "")).lower()
    title = item.get("title", "").lower()
    clause_type = infer_clause_type(item)
    tags = infer_tags(item)
    bullets = count_bullets(text)

    if clause_type in {"field_definition", "constant_definition", "format_definition"}:
        return "low"

    if clause_type in {"supporting_semantics", "architecture_overview"}:
        return "low"

    if "implementation_defined" in tags and clause_type == "procedural":
        return "high"

    if "shall" in text and ("when " in text or "if " in text or "upon " in text) and bullets > 0:
        return "high"

    if "shall" in text and bullets > 0:
        return "high"

    if any(h in title for h in PROCEDURAL_TITLE_HINTS):
        return "medium"

    if item.get("level", 0) >= 3 and has_action_verb(text):
        return "medium"

    return "low"


def is_candidate_clause(item: Dict[str, Any]) -> bool:
    text = normalize_text(item.get("text", ""))
    title = item.get("title", "")

    if not text:
        return False

    if looks_excluded_title(title):
        return False

    clause_type = infer_clause_type(item)

    if clause_type in {
        "procedural",
        "supporting_semantics",
        "field_definition",
        "constant_definition",
        "format_definition",
        "architecture_overview",
    }:
        return True

    if contains_normative_signal(text):
        return True

    if has_dependency_signal(text):
        return True

    return False


# ============================================================
# 3) Reference context collection
# ============================================================

def collect_internal_ref_context(
    item: Dict[str, Any],
    corpus_by_id: Dict[str, Dict[str, Any]],
    max_refs: int = 3,
    max_chars_per_ref: int = 1200,
) -> List[Dict[str, str]]:
    ref_contexts = []
    seen = set()

    for ref_id in item.get("internal_refs", []):
        if ref_id in seen:
            continue
        seen.add(ref_id)

        ref_item = corpus_by_id.get(ref_id)
        if not ref_item:
            continue

        ref_contexts.append({
            "clause_id": ref_id,
            "title": ref_item.get("title", ""),
            "text": truncate_for_context(ref_item.get("text", ""), max_chars=max_chars_per_ref),
        })

        if len(ref_contexts) >= max_refs:
            break

    return ref_contexts


# ============================================================
# 4) Underspecification analysis
# ============================================================

def analyze_underspecification(item: Dict[str, Any]) -> Dict[str, Any]:
    text = normalize_text(item.get("text", ""))
    low = text.lower()
    clause_type = infer_clause_type(item)
    tags = infer_tags(item)
    priority = infer_priority(item)

    signals = []
    score = 0.0

    if clause_type in {"field_definition", "constant_definition", "format_definition"}:
        if "implementation_defined" in tags:
            signals.append("Definition-style clause contains implementation latitude.")
            score += 1.0
        return {
            "clause_id": item["clause_id"],
            "title": item["title"],
            "clause_type": clause_type,
            "tags": tags,
            "priority": priority,
            "rule_score": round(score, 2),
            "rule_signals": signals,
            "likely_issue": score >= 2,
            "snippet": make_snippet(text),
        }

    if ("when " in low or "if " in low or "upon " in low) and not has_action_verb(low):
        signals.append("Conditional trigger appears without clear action verb.")
        score += 2.0

    if contains_normative_signal(text) and len(text.split()) < 12:
        signals.append("Normative clause is very short and may omit important detail.")
        score += 1.0

    if any(word in low for word in PARAMETER_HINT_WORDS):
        signals.append("Clause mentions timers/state/configuration concepts that may require explicit definitions.")
        score += 1.0

    dep_hits = 0
    for pat in DEPENDENCY_HINT_PATTERNS:
        if pat.search(text):
            dep_hits += 1
    if dep_hits > 0 or item.get("internal_refs"):
        signals.append("Clause depends on other clauses/specifications for procedural detail.")
        score += 1.0

    if "shall" in low and count_bullets(text) == 0 and len(text.split()) < 25:
        signals.append("Clause contains 'shall' but has limited explicit procedural breakdown.")
        score += 1.0

    vague_patterns = [
        r"\bas needed\b",
        r"\bif needed\b",
        r"\bas soon as they are available\b",
        r"\brelevant\b",
        r"\bappropriate\b",
    ]
    vague_hits = [vp for vp in vague_patterns if re.search(vp, low)]
    if vague_hits:
        signals.append("Clause contains potentially vague qualifiers.")
        score += 0.5

    if re.search(r"\bif any\b", low):
        signals.append("Clause contains a weak optionality qualifier ('if any').")
        score += 0.25

    if "implementation_defined" in tags:
        signals.append("Clause includes implementation-defined / implementation-latitude wording.")
        score += 1.5

    if clause_type in {"supporting_semantics", "architecture_overview"}:
        score -= 0.5

    return {
        "clause_id": item["clause_id"],
        "title": item["title"],
        "clause_type": clause_type,
        "tags": tags,
        "priority": priority,
        "rule_score": round(score, 2),
        "rule_signals": signals,
        "likely_issue": score >= 2,
        "snippet": make_snippet(text),
    }


# ============================================================
# 5) Inconsistency-risk analysis
# ============================================================

def analyze_inconsistency(item: Dict[str, Any]) -> Dict[str, Any]:
    text = normalize_text(item.get("text", ""))
    low = text.lower()
    clause_type = infer_clause_type(item)
    tags = infer_tags(item)
    priority = infer_priority(item)

    signals = []
    score = 0.0

    if clause_type in {"field_definition", "constant_definition", "format_definition"}:
        return {
            "clause_id": item["clause_id"],
            "title": item["title"],
            "clause_type": clause_type,
            "tags": tags,
            "priority": priority,
            "rule_score": round(score, 2),
            "rule_signals": signals,
            "likely_issue": False,
            "snippet": make_snippet(text),
        }

    if "shall" in low and "may" in low:
        signals.append("Clause mixes mandatory ('shall') and optional ('may') language.")
        score += 1.5

    if "shall" in low and "should" in low:
        signals.append("Clause mixes mandatory ('shall') and advisory ('should') language.")
        score += 1.0

    if re.search(r"\bshall\b", low) and re.search(r"\bshall not\b", low):
        signals.append("Clause contains both positive and negative mandatory forms.")
        score += 1.0

    for a, b in CONFLICT_TERM_GROUPS:
        if a in low and b in low:
            signals.append(f"Clause mentions both '{a}' and '{b}'; check whether conditions are fully disambiguated.")
            score += 0.75

    if re.search(r"\beither\b", low) and re.search(r"\bor\b", low) and "if" not in low:
        signals.append("Clause presents alternatives that may need clearer disambiguation.")
        score += 0.5

    if any(p.search(text) for p in OBJECT_MIX_PATTERNS):
        signals.append("Clause may mix protocol object terminology or roles in a suspicious way.")
        score += 2.0

    if "corresponding rlc sdu" in low and "sn" in low:
        signals.append("Clause links SN semantics to an RLC SDU in a potentially inconsistent way.")
        score += 2.0

    if any(p.search(text) for p in WRONG_REFERENCE_STYLE_PATTERNS):
        signals.append("Clause contains a potentially awkward or inconsistent reference style.")
        score += 0.5

    if "example" in low and ("shall" in low or "must" in low):
        signals.append("Clause mixes example-oriented text with strong normative wording; verify consistency.")
        score += 0.5

    return {
        "clause_id": item["clause_id"],
        "title": item["title"],
        "clause_type": clause_type,
        "tags": tags,
        "priority": priority,
        "rule_score": round(score, 2),
        "rule_signals": signals,
        "likely_issue": score >= 2,
        "snippet": make_snippet(text),
    }


# ============================================================
# 6) Review packaging
# ============================================================

def package_review_items(
    ranked_results: List[Dict[str, Any]],
    corpus_by_id: Dict[str, Dict[str, Any]],
    top_k: int = 15
) -> List[Dict[str, Any]]:
    review_items = []

    for res in ranked_results[:top_k]:
        clause_id = res["clause_id"]
        item = corpus_by_id[clause_id]
        referenced_clauses = collect_internal_ref_context(
            item=item,
            corpus_by_id=corpus_by_id,
            max_refs=3,
            max_chars_per_ref=1200,
        )

        review_items.append({
            "spec_id": item.get("spec_id", ""),
            "clause_id": clause_id,
            "title": res["title"],
            "level": item["level"],
            "parent_clause_id": item["parent_clause_id"],
            "children": item["children"],
            "clause_type": res["clause_type"],
            "tags": res["tags"],
            "priority": res["priority"],
            "rule_score": res["rule_score"],
            "rule_signals": res["rule_signals"],
            "internal_refs": item.get("internal_refs", []),
            "external_refs": item.get("external_refs", []),
            "referenced_clauses": referenced_clauses,
            "snippet": res["snippet"],
            "full_text": item["text"],
        })

    return review_items


def build_manual_review_seed(
    ranked_results: List[Dict[str, Any]],
    corpus_by_id: Dict[str, Dict[str, Any]],
    top_k: int = 20,
    review_kind: str = "underspec"
) -> List[Dict[str, Any]]:
    seed = []

    for res in ranked_results[:top_k]:
        clause_id = res["clause_id"]
        item = corpus_by_id[clause_id]
        referenced_clauses = collect_internal_ref_context(
            item=item,
            corpus_by_id=corpus_by_id,
            max_refs=3,
            max_chars_per_ref=1200,
        )

        seed.append({
            "spec_id": item.get("spec_id", ""),
            "review_kind": review_kind,
            "clause_id": clause_id,
            "title": res["title"],
            "level": item["level"],
            "parent_clause_id": item["parent_clause_id"],
            "clause_type": res["clause_type"],
            "tags": res["tags"],
            "priority": res["priority"],
            "rule_score": res["rule_score"],
            "rule_signals": res["rule_signals"],
            "internal_refs": item.get("internal_refs", []),
            "external_refs": item.get("external_refs", []),
            "referenced_clauses": referenced_clauses,
            "snippet": res["snippet"],
            "full_text": item["text"],
            "human_label": "",
            "human_notes": "",
        })

    return seed


# ============================================================
# 7) Main pipeline
# ============================================================

def main(input_dir: str, output_dir: str, spec_id: str) -> None:
    ensure_dir(output_dir)

    corpus_path = os.path.join(input_dir, "corpus.json")
    if not os.path.exists(corpus_path):
        raise FileNotFoundError(f"corpus.json not found: {corpus_path}")

    print("Running 3GPP clause analysis.")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Spec ID: {spec_id}")

    print("\n[Step 1] Loading corpus ...")
    corpus = load_json(corpus_path)
    for item in corpus:
        if "spec_id" not in item:
            item["spec_id"] = spec_id
    corpus_by_id = {item["clause_id"]: item for item in corpus}
    print(f"Loaded {len(corpus)} corpus items.")

    print("\n[Step 2] Selecting candidate clauses ...")
    candidates = []
    for item in corpus:
        if is_candidate_clause(item):
            enriched = dict(item)
            enriched["spec_id"] = spec_id
            enriched["clause_type"] = infer_clause_type(item)
            enriched["tags"] = infer_tags(item)
            enriched["priority"] = infer_priority(item)
            enriched["snippet"] = make_snippet(item["text"])
            candidates.append(enriched)

    priority_rank = {"high": 0, "medium": 1, "low": 2}
    clause_type_rank = {
        "procedural": 0,
        "supporting_semantics": 1,
        "reference_heavy": 2,
        "architecture_overview": 3,
        "descriptive": 4,
        "field_definition": 5,
        "format_definition": 6,
        "constant_definition": 7,
    }

    candidates.sort(
        key=lambda x: (
            priority_rank.get(x["priority"], 9),
            clause_type_rank.get(x["clause_type"], 9),
            -x.get("level", 0),
            x["clause_id"],
        )
    )

    candidate_path = os.path.join(output_dir, "candidate_clauses.json")
    save_json(candidates, candidate_path)
    print(f"Selected {len(candidates)} candidate clauses.")
    print(f"Saved candidates to: {candidate_path}")

    print("\n[Step 3] Running underspecification signal analysis ...")
    underspec_results = [analyze_underspecification(item) for item in candidates]
    underspec_results.sort(
        key=lambda x: (
            -x["rule_score"],
            priority_rank.get(x["priority"], 9),
            clause_type_rank.get(x["clause_type"], 9),
            x["clause_id"],
        )
    )
    underspec_path = os.path.join(output_dir, "underspecification_signals.json")
    save_json(underspec_results, underspec_path)
    print(f"Saved underspecification signals to: {underspec_path}")

    print("\n[Step 4] Running inconsistency-risk signal analysis ...")
    inconsistency_results = [analyze_inconsistency(item) for item in candidates]
    inconsistency_results.sort(
        key=lambda x: (
            -x["rule_score"],
            priority_rank.get(x["priority"], 9),
            clause_type_rank.get(x["clause_type"], 9),
            x["clause_id"],
        )
    )
    inconsistency_path = os.path.join(output_dir, "inconsistency_signals.json")
    save_json(inconsistency_results, inconsistency_path)
    print(f"Saved inconsistency signals to: {inconsistency_path}")

    print("\n[Step 5] Packaging top review items ...")
    top_underspec_review = package_review_items(underspec_results, corpus_by_id, top_k=15)
    top_inconsistency_review = package_review_items(inconsistency_results, corpus_by_id, top_k=15)

    top_underspec_path = os.path.join(output_dir, "top_underspec_review.json")
    top_inconsistency_path = os.path.join(output_dir, "top_inconsistency_review.json")

    save_json(top_underspec_review, top_underspec_path)
    save_json(top_inconsistency_review, top_inconsistency_path)

    print(f"Saved top underspec review items to: {top_underspec_path}")
    print(f"Saved top inconsistency review items to: {top_inconsistency_path}")

    print("\n[Step 6] Building manual review seed files ...")
    manual_underspec_seed = build_manual_review_seed(
        underspec_results, corpus_by_id, top_k=20, review_kind="underspec"
    )
    manual_inconsistency_seed = build_manual_review_seed(
        inconsistency_results, corpus_by_id, top_k=20, review_kind="inconsistency"
    )

    manual_underspec_seed_path = os.path.join(output_dir, "manual_review_seed_underspec.json")
    manual_inconsistency_seed_path = os.path.join(output_dir, "manual_review_seed_inconsistency.json")

    save_json(manual_underspec_seed, manual_underspec_seed_path)
    save_json(manual_inconsistency_seed, manual_inconsistency_seed_path)

    print(f"Saved manual underspec review seed to: {manual_underspec_seed_path}")
    print(f"Saved manual inconsistency review seed to: {manual_inconsistency_seed_path}")

    print("\n[Step 7] Writing summary ...")
    summary = {
        "spec_id": spec_id,
        "num_corpus_items": len(corpus),
        "num_candidates": len(candidates),
        "num_likely_underspec": sum(1 for x in underspec_results if x["likely_issue"]),
        "num_likely_inconsistency": sum(1 for x in inconsistency_results if x["likely_issue"]),
        "top_underspec_clause_ids": [x["clause_id"] for x in underspec_results[:10]],
        "top_inconsistency_clause_ids": [x["clause_id"] for x in inconsistency_results[:10]],
        "top_candidate_clause_ids": [x["clause_id"] for x in candidates[:15]],
    }
    summary_path = os.path.join(output_dir, "summary.json")
    save_json(summary, summary_path)
    print(f"Saved summary to: {summary_path}")

    print("\nDone.")
    print("Generated files:")
    print(f"  - {candidate_path}")
    print(f"  - {underspec_path}")
    print(f"  - {inconsistency_path}")
    print(f"  - {top_underspec_path}")
    print(f"  - {top_inconsistency_path}")
    print(f"  - {manual_underspec_seed_path}")
    print(f"  - {manual_inconsistency_seed_path}")
    print(f"  - {summary_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run first-pass analysis over staged 3GPP corpus."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Directory containing corpus.json"
    )
    parser.add_argument(
        "--out",
        type=str,
        required=True,
        help="Directory where analysis outputs will be saved"
    )
    parser.add_argument(
        "--spec",
        type=str,
        default="38.322",
        help="Specification identifier"
    )

    args = parser.parse_args()

    main(
        input_dir=args.input,
        output_dir=args.out,
        spec_id=args.spec,
    )