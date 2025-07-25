# Errata 7118 - RFC 9286

- **RFC Title:** Manifests for the Resource Public Key Infrastructure (RPKI)
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7118](https://www.rfc-editor.org/errata/eid7118)

```
Section Appendix A says:


fileList           SEQUENCE SIZE (0..MAX) OF FileAndHash

It should say:

fileList           SEQUENCE SIZE (1..MAX) OF FileAndHash

Notes:

Section 7 specifies " A CA's manifest will always contain at least one entry"; therefor, a fileList sequence of size 0 is invalid.
```

## Explanation

The original definition allows for a fileList with zero entries, contradicting Section 7, which states that a manifest will always have at least one entry. The correction sets the minimum size to 1, resolving the inconsistency.
