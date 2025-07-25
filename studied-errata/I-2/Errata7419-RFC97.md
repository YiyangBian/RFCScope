# Errata 7419 - RFC 97

- **RFC Title:** HTTP Semantics
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7419](https://www.rfc-editor.org/errata/eid7419)

```
Section 8.3.2 says:


   In the fields defined by this document, charset names appear either
   in parameters (Content-Type), or, for Accept-Encoding, in the form of
   a plain token.

It should say:

   In the fields defined by this document, charset names appear either
   in parameters (Content-Type), or, for Accept-Charset, in the form of
   a plain token.

Notes:

Accept-Encoding is the preferred list of response content codings.  Accept-Charset is the preferred list of response charsets.
```

## Explanation

The text in Section 8.3.2 incorrectly mentions "Accept-Encoding" when it should refer to "Accept-Charset". This inconsistency creates confusion, as "Accept-Encoding" is for content codings, not character sets.  This directly affects the correct interpretation of how charset names are used, leading to potential implementation errors.  Therefore, it is classified as INCONSISTENT.
