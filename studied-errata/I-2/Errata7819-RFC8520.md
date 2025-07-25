# Errata 7819 - RFC 8520

- **RFC Title:** Manufacturer Usage Description Specification
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid7819](https://www.rfc-editor.org/errata/eid7819)

```
Section 13.1 says:


Note: A MUD file may need to be re-signed if the signature expires.

It should say:

Note: A MUD file may need to be re-signed if the certificate needed
to validate the signature expires.

Notes:

The signature does not expire, but the certificate does.
```

## Explanation

The original text incorrectly states that the signature expires. The certificate used to validate the signature is what expires, not the signature itself. This inconsistency affects the understanding of the MUD file management process.
