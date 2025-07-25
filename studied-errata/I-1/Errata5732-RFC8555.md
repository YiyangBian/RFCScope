# Errata 5732 - RFC 8555

- **RFC Title:** Automatic Certificate Management Environment (ACME)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid5732](https://www.rfc-editor.org/errata/eid5732)

```
Section 8 says:


A challenge object with an error MUST have status
equal to "invalid".

It should say:

A challenge object with an error MUST have status
equal to "processing" or "invalid".

Notes:

Section 8.2 says that 'The server MUST add an entry to the "error" field in the challenge after each failed validation query'.  However, if the challenge must then become "invalid", it is never possible to retry any validation query (because "invalid" is a final state for a challenge object).
This erratum is necessary to permit validation query retries to ever happen.
```

## Explanation

The statement in Section 8 that a challenge object with an error MUST have status equal to "invalid" is inconsistent with the retry mechanism described in Section 8.2.  Section 8.2 indicates that failed validation attempts add an error to the challenge object, but the "invalid" status prevents retries.  The corrected statement allows for the "processing" status, enabling retry attempts before the challenge becomes definitively "invalid", thus resolving the inconsistency.
