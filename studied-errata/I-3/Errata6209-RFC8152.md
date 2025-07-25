# Errata 6209 - RFC 8152

- **RFC Title:** CBOR Object Signing and Encryption (COSE)
- **RFC Publication Date:** July 2017
- Link to original errata report: [rfc-editor.org/errata/eid6209](https://www.rfc-editor.org/errata/eid6209)

```
Section 9 says:


can be used to prove the identity

It should say:

cannot be used to prove the identity

Notes:

MACs cannot be used to prove identity to a third party.  There is a missing "not" in the sentence.
```

## Explanation

The original text incorrectly states that MACs can be used to prove identity. The corrected text accurately reflects that MACs cannot be used for this purpose.  This inconsistency affects the understanding of MAC functionality and may lead to incorrect implementations.
