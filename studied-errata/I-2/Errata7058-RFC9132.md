# Errata 7058 - RFC 9132

- **RFC Title:** Distributed Denial-of-Service Open Threat Signaling (DOTS) Signal Channel Specification
- **RFC Publication Date:** September 2021
- Link to original errata report: [rfc-editor.org/errata/eid7058](https://www.rfc-editor.org/errata/eid7058)

```
Section 5.3 says:


              uses data-channel:target {
                when "/dots-signal/scope/conflict-information/"
                   + "conflict-cause = 'overlapping-targets'";
              }


It should say:

              uses data-channel:target {
                when "../conflict-cause = 'overlapping-targets'";
              }


Notes:

The original YANG statements make the "uses" statement apply to all "list scope" instances as soon as there is at least one "scope" instance that has "conflict-cause" set to "overlapping-targets". I suspect this is not the author's intent.

The corrected YANG statements make the "uses" statement only apply to the specific "scope" instances that have "conflict-cause" set to "overlapping-targets". There are also other ways to fix this issue.
```

## Explanation

The original YANG uses statement applies the augmentation to all list scope instances when it should only apply to instances where conflict-cause is 'overlapping-targets'.  This creates an inconsistency between the intended behavior and the actual effect of the YANG statement.
