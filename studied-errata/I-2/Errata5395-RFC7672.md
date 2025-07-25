# Errata 5395 - RFC 7672

- **RFC Title:** SMTP Security via Opportunistic DNS-Based Authentication of Named Entities (DANE) Transport Layer Security (TLS)
- **RFC Publication Date:** October 2015
- Link to original errata report: [rfc-editor.org/errata/eid5395](https://www.rfc-editor.org/errata/eid5395)

```
Section 2.1.1 says:


   DNS records that would be
   classified "indeterminate" in the sense of [RFC4035] are simply
   classified as "insecure".

It should say:

   DNS records that would be
   classified "indeterminate" in the sense of [RFC4033] are simply
   classified as "insecure".
```

## Explanation

The erratum points out an incorrect reference in Section 2.1.1 of RFC 7672. The original text refers to RFC4035, while the correction points to RFC4033. This is a factual error that directly impacts implementation and understanding of the specification. Therefore, it's classified as INCONSISTENT.
