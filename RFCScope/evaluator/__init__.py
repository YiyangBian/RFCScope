import os
from typing import Callable


def run_evaluator(
    prompt,
    system_prompt,
    evaluation_system_prompt,
    analysis,
    output_dir,
    rfc_number,
    section_id,
    get_output_from_model: Callable,
) -> None:
    evaluation_filename = os.path.join(
        output_dir, f"rfc{rfc_number}", f"section{section_id}_evaluation.md"
    )

    # generate evaluation if it doesn't already exist
    if (
        not os.path.exists(evaluation_filename)
        or os.path.getsize(evaluation_filename) == 0
    ):
        evaluation_prompt = "\n".join(
            [
                f"You provided the following instructions to your student:\n\n```\n{system_prompt}\n```\n",
                f"The student produced the following analysis:\n\n{analysis}\n",
                f"The relevant RFC text provided to the student was:\n\n{prompt}\n",
            ]
        )
        evaluation = get_output_from_model(
            evaluation_prompt, evaluation_system_prompt, "evaluation"
        )

        with open(evaluation_filename, "w", encoding="utf-8") as f:
            f.write(evaluation)
