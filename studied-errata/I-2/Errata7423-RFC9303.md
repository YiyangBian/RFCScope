# Errata 7423 - RFC 9303

- **RFC Title:** Locator/ID Separation Protocol Security (LISP-SEC)
- **RFC Publication Date:** October 2022
- Link to original errata report: [rfc-editor.org/errata/eid7423](https://www.rfc-editor.org/errata/eid7423)

```
Section 6.9 says:


ITR MUST set the 'EID HMAC ID' field to 0 before computing the HMAC.

It should say:

ITR MUST set the 'EID HMAC' field to 0 before computing the HMAC.

Notes:

0 (zero) must be set in the 'EID HMAC' field, not in the 'EID HMAC ID' field
```

## Explanation

The original text refers to the incorrect field ('EID HMAC ID'). The correction uses the correct field name ('EID HMAC'), resolving the inconsistency. This inconsistency would affect implementations computing the HMAC.
