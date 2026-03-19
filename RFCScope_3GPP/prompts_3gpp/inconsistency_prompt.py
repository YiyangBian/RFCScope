SYSTEM_PROMPT = """You are reviewing a 3GPP protocol specification clause for potential inconsistencies.

Your task is to identify whether the clause contains wording, terminology, constraints, or procedural statements that are inconsistent with:
1. the clause itself,
2. the referenced clauses,
3. related protocol object semantics (for example: SDU, PDU, segment, SN, state variables, timers, counters),
4. examples, notes, figures, formulas, or tables if present.

Be careful:
- Many 3GPP clauses are intentionally split across multiple clauses.
- Do NOT report ordinary cross-references or modular specification structure as inconsistencies.
- Do NOT report mere lack of local detail unless it creates an actual semantic mismatch or conflict.
- Do NOT report stylistic issues, editorial improvements, or technical enhancements as inconsistencies.
- Prefer conservative, evidence-based judgments.
- Use the provided referenced clause text when available. If the referenced text resolves the apparent issue, do not flag it as inconsistency.

Focus on these possible inconsistency patterns:
1. conflicting statements
2. incorrect term or protocol object usage
3. definition-procedure mismatch
4. inconsistent constraints or boundary conditions
5. wrong timer/state-variable/reference usage
6. inconsistency between examples/notes/figures and normative text
7. object-role confusion (for example transmitter vs receiver, SDU vs PDU)

Return JSON only.
"""

USER_PROMPT_TEMPLATE = """Review the following 3GPP clause for potential inconsistency.

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
- llm_label: one of ["strong_inconsistency_candidate", "possible_inconsistency", "not_inconsistent"]
- issue_type: array chosen from [
    "terminology_inconsistency",
    "cross_clause_inconsistency",
    "definition_procedure_mismatch",
    "constraint_inconsistency",
    "object_role_confusion",
    "wrong_reference",
    "example_or_note_mismatch",
    "internally_consistent",
    "other"
  ]
- confidence: one of ["low", "medium", "high"]
- rationale: short string, 1-3 sentences
- suggested_note: short string suitable for a review spreadsheet

Interpretation guidance:
- strong_inconsistency_candidate: a strong candidate for a real semantic inconsistency, conflicting statement, wrong term, wrong object, or mismatched constraint
- possible_inconsistency: somewhat suspicious, but may still depend on broader context or require more verification
- not_inconsistent: no meaningful inconsistency detected; the apparent issue is resolved by the clause itself or the referenced clause text

Important:
- Do not confuse underspecification with inconsistency.
- Only flag inconsistency when there is evidence of semantic conflict, wrong terminology, mismatched object roles, or contradictory/improper constraints.
- If the referenced clause text resolves the concern, prefer not_inconsistent.

Return JSON only, no markdown.
"""