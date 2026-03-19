import os
from typing import Callable


def run_analyzer(
    prompt,
    system_prompt,
    output_dir,
    rfc_number,
    section_id,
    get_output_from_model: Callable,
) -> str:
    output_filename = os.path.join(
        output_dir, f"rfc{rfc_number}", f"section{section_id}_analysis.md"
    )
    prompt_filename = os.path.join(
        output_dir, f"rfc{rfc_number}", f"section{section_id}_prompt.md"
    )

    with open(prompt_filename, "w", encoding="utf-8") as f:
        f.write(prompt)

    # generate analysis if it doesn't already exist
    if os.path.exists(output_filename) and os.path.getsize(output_filename) > 0:
        analysis = open(output_filename, encoding="utf-8").read()
    else:
        analysis = get_output_from_model(prompt, system_prompt, "analysis")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(analysis)

    return analysis
