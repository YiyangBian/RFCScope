# RFCScope

This repository is based on the artifact for **RFCScope: Detecting Logically Ambiguous Bugs in Internet Protocol Specifications** from **ASE 2025**.

Original repository: [HIPREL-Group/RFCScope](https://github.com/HIPREL-Group/RFCScope)

This fork keeps the original artifact and adds our own extensions for exploring **3GPP specification analysis**, especially for **3GPP TS 38.322 (RLC)**.

## Repository Overview

This repository contains both the original RFCScope artifact and our extension work.

### Original artifact content
The following directories come from the original RFCScope repository:

- `studied-errata/`  
  RFC errata collected and categorized in the original study.

- `prompts/`  
  System and user prompts used in RFCScope for inconsistency and under-specification analysis.

- `detected-bugs/`  
  Bugs selected after manual inspection of RFCScope results.

- `RFCScope/`  
  The original implementation of the RFCScope tool.

### Our extension
- `RFCScope_3GPP/`  
  Our extension work for applying RFCScope-style analysis ideas to **3GPP telecom specifications**.  
  This part focuses on clause-level analysis of **3GPP TS 38.322**, with attention to procedural logic, state-dependent behavior, timers, and cross-clause references.

---

## Original RFCScope Artifact

The original RFCScope artifact studies logically ambiguous bugs in Internet protocol specifications.

Additional materials:
- [Paper draft](https://wenxiwang.github.io/papers/rfcscope/rfcscope_paper.pdf)
- [Video](http://mrigank.in/RFCScope-video)
- [Poster](https://mrigank.in/media/ASE2025Poster.pdf)
- [Slides](https://mrigank.in/media/ASE2025Slides.pdf)

---

## Directory Details

### `studied-errata/`
This directory contains the RFC errata used in the original RFCScope study.

It is organized into the following categories:

- `I-1/` — Direct inconsistency (119 items)
- `I-2/` — Indirect inconsistency (70 items)
- `I-3/` — Inconsistency with common knowledge (13 items)
- `U-1/` — Direct under-specification: undefined terms (7 items)
- `U-2/` — Direct under-specification: incomplete constraints (15 items)
- `U-3/` — Indirect under-specification (10 items)
- `U-4/` — Incorrect or missing references (5 items)

Errata from the **Other** category are not included in this artifact.

Each file follows the naming format:

`Errata<errata-id>-RFC<rfc-number>.md`

Each file includes:
- the original erratum text,
- RFC details,
- a link to the original IETF Errata report,
- and an explanation added by the authors.

These errata come from **Standards Track RFCs** published between **January 2014 and January 2025**.

---

### `prompts/`
This directory contains the prompts used in RFCScope.

#### Structure

- `system-prompts/`
  - `inconsistency/`
    - `analyzer.md`
    - `evaluator.md`
  - `under-specification/`
    - `analyzer.md`
    - `evaluator.md`

- `user-prompts/`
  - `analyzer.md`
  - `evaluator.md`

The system prompts define the role and behavior of the model for each task.

The user prompts are templates that are filled with RFC content and metadata during execution.

---

### `detected-bugs/`
This directory contains the bugs selected after manual inspection of RFCScope’s results.

File names use one of these formats:

- `RFC<number>.md` for one bug in an RFC
- `RFC<number>-<id>.md` for multiple bugs in the same RFC

In total, the original artifact includes **31 detected bugs across 14 RFCs**.

Each file contains:
- the bug report,
- its category,
- and its confirmation status.

The status labels are:

- **Pending** — the authors have not been contacted yet
- **Awaiting response from authors** — the authors were contacted and no reply has been received yet
- **Confirmed by authors** — the RFC authors confirmed the bug
- **Verified on the IETF Errata portal** — the bug has been confirmed and verified on the IETF Errata portal

---

### `RFCScope/`
This directory contains the original implementation of the RFCScope tool.

Please check that directory for setup and execution instructions.

---

### `RFCScope_3GPP/`
This directory contains our extension work built on top of the RFCScope idea.

Our goal is to explore whether RFCScope-style clause analysis can be applied beyond RFCs, especially to **3GPP telecom standards**.

In this extension, we focus on:
- extracting and staging clauses from 3GPP specifications,
- analyzing procedural and stateful clauses,
- identifying possible under-specification and inconsistency signals,
- and supporting follow-up review with LLM-based analysis.

This part is still an ongoing course/research extension and is separate from the original ASE 2025 artifact.

---

## Notes

This repository is a fork and includes both:
1. the original RFCScope artifact, and  
2. our own extension for 3GPP specification analysis.

If you want to reproduce the original ASE 2025 artifact, please use the original directories and follow the instructions under `RFCScope/`.

If you are interested in our extension, please check `RFCScope_3GPP/` for the added files and experiments.
