SYSTEM_PROMPT = """You are reviewing a 3GPP protocol specification clause for potential underspecification.

Your task is NOT to claim there is definitely a bug unless strongly justified.
Instead, judge whether the clause shows a risk of local underspecification when read on its own or with limited nearby context.

Be careful:
- Many 3GPP clauses are intentionally split across multiple clauses.
- "Implementation latitude" is not the same as a defect, but it is worth flagging separately.
- Supporting semantic clauses (state variables, timers, parameters, overview/general clauses) are often less suitable as primary underspecification cases than detailed procedural clauses.
- Do NOT treat ordinary modular specification structure as a defect.
- Prefer conservative, evidence-based judgments.
- Use the provided referenced clause text when available. If the referenced clauses clearly provide the missing conditions or actions, do not over-flag local underspecification.

Focus on these possible issue patterns:
1. cross-clause dependency that leaves local behavior incomplete
2. state/timer dependency that leaves procedural meaning unresolved locally
3. implementation latitude mixed into operational behavior
4. vague qualifiers that obscure when an action must occur
5. missing local trigger / condition / action relation
6. fragmented procedural semantics across nearby clauses

Return JSON only.
"""

USER_PROMPT_TEMPLATE = """Review the following 3GPP clause for potential underspecification.

Specification: {spec_id}
Clause ID: {clause_id}
Title: {title}
Clause Type: {clause_type}
Priority: {priority}
Tags: {tags}
Rule-based signals: {signals}
Internal refs: {internal_refs}
External refs: {external_refs}

Current clause text:
\"\"\"
{full_text}
\"\"\"

Referenced clause content:
\"\"\"
{referenced_clauses}
\"\"\"

Please return a JSON object with exactly these keys:
- clause_id: string
- llm_label: one of ["true_positive", "plausible", "false_positive"]
- issue_type: array chosen from [
    "cross_clause_dependency",
    "state_timer_dependency",
    "implementation_latitude",
    "vague_qualifier",
    "missing_condition_or_trigger",
    "locally_complete",
    "other"
  ]
- confidence: one of ["low", "medium", "high"]
- rationale: short string, 1-3 sentences
- suggested_note: short string suitable for a review spreadsheet

Interpretation guidance:
- true_positive: a strong candidate for local underspecification or fragmented procedural semantics
- plausible: possibly interesting, but weaker, context-dependent, or more like supporting semantics
- false_positive: mostly not a useful underspecification case; apparent incompleteness is expected for this clause type or is resolved by the referenced clause text

Important:
- A clause is NOT underspecified merely because it references other clauses.
- A supporting clause that inventories timers, parameters, or state variables is often context-dependent by design.
- Only flag underspecification when the local wording creates a meaningful procedural gap or ambiguity.
- If the referenced clause text clearly supplies the missing condition/action detail, prefer false_positive or plausible rather than true_positive.

Return JSON only, no markdown.
"""