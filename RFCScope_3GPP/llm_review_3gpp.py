import os
import re
import json
import time
import argparse
from typing import Any, Dict

from openai import OpenAI


# ============================================================
# 1) Prompt import by task
# ============================================================

def load_prompts(task: str):
    if task == "underspec":
        from prompts_3gpp.underspec_prompt import (
            SYSTEM_PROMPT,
            USER_PROMPT_TEMPLATE,
        )
    elif task == "inconsistency":
        from prompts_3gpp.inconsistency_prompt import (
            SYSTEM_PROMPT,
            USER_PROMPT_TEMPLATE,
        )
    else:
        raise ValueError(f"Unsupported task: {task}")

    return SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


# ============================================================
# 2) Utilities
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(obj: Any, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def safe_sleep(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def truncate_text(text: str, max_chars: int = 4000) -> str:
    text = (text or "").strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n...[TRUNCATED]"


def get_rule_signals(item: Dict[str, Any]) -> list:
    return item.get("rule_signals", item.get("signals", []))


def get_rule_score(item: Dict[str, Any]) -> Any:
    return item.get("rule_score", item.get("score"))


def format_referenced_clauses(item: Dict[str, Any], max_total_chars: int = 4000) -> str:
    refs = item.get("referenced_clauses", [])
    if not refs:
        return "None"

    blocks = []
    total = 0

    for ref in refs:
        block = (
            f"Referenced Clause ID: {ref.get('clause_id', '')}\n"
            f"Title: {ref.get('title', '')}\n"
            f"Text:\n{ref.get('text', '').strip()}\n"
        )

        if total + len(block) > max_total_chars:
            remaining = max_total_chars - total
            if remaining > 200:
                block = block[:remaining].rstrip() + "\n...[TRUNCATED]\n"
                blocks.append(block)
            break

        blocks.append(block)
        total += len(block)

    return "\n---\n".join(blocks) if blocks else "None"


# ============================================================
# 3) Prompt construction
# ============================================================

def build_user_prompt(item: Dict[str, Any], user_prompt_template: str) -> str:
    return user_prompt_template.format(
        spec_id=item.get("spec_id", "38.322"),
        clause_id=item["clause_id"],
        title=item.get("title", ""),
        clause_type=item.get("clause_type", ""),
        priority=item.get("priority", ""),
        tags=", ".join(item.get("tags", [])),
        signals=" | ".join(get_rule_signals(item)),
        internal_refs=", ".join(item.get("internal_refs", [])),
        external_refs=", ".join(item.get("external_refs", [])),
        referenced_clauses=format_referenced_clauses(item, max_total_chars=4000),
        full_text=truncate_text(item.get("full_text", ""), max_chars=5000),
    )


# ============================================================
# 4) LLM call
# ============================================================

def parse_json_response(text: str) -> Dict[str, Any]:
    text = (text or "").strip()
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def review_one_clause(
    client: OpenAI,
    model: str,
    item: Dict[str, Any],
    system_prompt: str,
    user_prompt_template: str,
    task: str,
) -> Dict[str, Any]:
    user_prompt = build_user_prompt(item, user_prompt_template)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    content = response.choices[0].message.content
    parsed = parse_json_response(content)

    result = {
        "task": task,
        "clause_id": item["clause_id"],
        "title": item.get("title", ""),
        "rule_score": get_rule_score(item),
        "rule_signals": get_rule_signals(item),
        "clause_type": item.get("clause_type", ""),
        "tags": item.get("tags", []),
        "priority": item.get("priority", ""),
        "internal_refs": item.get("internal_refs", []),
        "external_refs": item.get("external_refs", []),
        "referenced_clauses": item.get("referenced_clauses", []),
        "snippet": item.get("snippet", ""),
        "full_text": item.get("full_text", ""),
        "llm_review": parsed,
        "human_label": item.get("human_label", ""),
        "human_notes": item.get("human_notes", ""),
    }
    return result


# ============================================================
# 5) Summary
# ============================================================

def build_summary(results: list, errors: list, num_requested: int, task: str) -> Dict[str, Any]:
    if task == "underspec":
        label_keys = ["true_positive", "plausible", "false_positive"]
    elif task == "inconsistency":
        label_keys = [
            "strong_inconsistency_candidate",
            "possible_inconsistency",
            "not_inconsistent",
        ]
    else:
        label_keys = []

    label_counts = {
        label: sum(
            1 for r in results
            if r.get("llm_review", {}).get("llm_label") == label
        )
        for label in label_keys
    }

    return {
        "task": task,
        "num_requested": num_requested,
        "num_completed": len(results),
        "num_errors": len(errors),
        "label_counts": label_counts,
    }


# ============================================================
# 6) Main
# ============================================================

def main(
    input_path: str,
    output_dir: str,
    model: str,
    top_k: int,
    sleep_sec: float,
    task: str,
) -> None:
    ensure_dir(output_dir)

    system_prompt, user_prompt_template = load_prompts(task)

    print("Running LLM review for 3GPP candidate clauses.")
    print(f"Task: {task}")
    print(f"Input file: {input_path}")
    print(f"Output dir: {output_dir}")
    print(f"Model: {model}")
    print(f"Top-K: {top_k}")

    items = load_json(input_path)
    if not isinstance(items, list):
        raise ValueError("Input JSON must be a list of review items.")

    items = items[:top_k]
    print(f"Loaded {len(items)} items for review.")

    client = OpenAI()

    results = []
    errors = []

    for idx, item in enumerate(items, start=1):
        clause_id = item.get("clause_id", f"unknown_{idx}")
        print(f"[{idx}/{len(items)}] Reviewing clause {clause_id} ...")

        try:
            reviewed = review_one_clause(
                client=client,
                model=model,
                item=item,
                system_prompt=system_prompt,
                user_prompt_template=user_prompt_template,
                task=task,
            )
            results.append(reviewed)
        except Exception as e:
            errors.append({
                "task": task,
                "clause_id": clause_id,
                "error": str(e),
            })

        safe_sleep(sleep_sec)

    results_path = os.path.join(output_dir, f"llm_review_results_{task}.json")
    errors_path = os.path.join(output_dir, f"llm_review_errors_{task}.json")
    summary_path = os.path.join(output_dir, f"llm_review_summary_{task}.json")

    save_json(results, results_path)
    save_json(errors, errors_path)

    summary = build_summary(
        results=results,
        errors=errors,
        num_requested=len(items),
        task=task,
    )
    save_json(summary, summary_path)

    print("\nDone.")
    print(f"Saved results to: {results_path}")
    print(f"Saved errors to: {errors_path}")
    print(f"Saved summary to: {summary_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LLM second-pass review for 3GPP candidate clauses."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to input candidate JSON file"
    )
    parser.add_argument(
        "--out",
        type=str,
        required=True,
        help="Directory to save LLM review results"
    )
    parser.add_argument(
        "--task",
        type=str,
        required=True,
        choices=["underspec", "inconsistency"],
        help="Review task type"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-5",
        help="OpenAI model name"
    )
    parser.add_argument(
        "--top_k",
        type=int,
        default=10,
        help="Number of top items to review"
    )
    parser.add_argument(
        "--sleep_sec",
        type=float,
        default=0.0,
        help="Optional delay between requests"
    )

    args = parser.parse_args()

    main(
        input_path=args.input,
        output_dir=args.out,
        model=args.model,
        top_k=args.top_k,
        sleep_sec=args.sleep_sec,
        task=args.task,
    )