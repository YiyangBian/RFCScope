# Errata 7736 - RFC 9085

- **RFC Title:** Border Gateway Protocol - Link State (BGP-LS) Extensions for Segment Routing
- **RFC Publication Date:** August 2021
- Link to original errata report: [rfc-editor.org/errata/eid7736](https://www.rfc-editor.org/errata/eid7736)

```
Section 2.3.5 says:


   A Prefix NLRI, that has been advertised with a Range TLV, is
   considered a normal routing prefix (i.e., prefix reachability) only
   when there is also an IGP metric TLV (TLV 1095) associated it.
   Otherwise, it is considered only as the first prefix in the range for
   prefix-to-SID mapping advertisement.

It should say:

   A Prefix NLRI, that has been advertised with a Range TLV, is
   considered a normal routing prefix (i.e., prefix reachability) only
   when there is also a Prefix Metric TLV (TLV 1155) associated with it.
   Otherwise, it is considered only as the first prefix in the range for
   prefix-to-SID mapping advertisement.

Notes:

The current text is referring to the wrong BGP-LS TLV. Since the Range TLV is associated with a Prefix NLRI, the "Prefix Metric TLV (TLV 1155)" should be referenced here since the "IGP metric TLV (TLV 1095)" is associated with a Link NLRI.

Verifier note: in addition to the fix proposed by Ketan, I added a preposition: "associated with it", and corrected an indefinite article: "a Prefix".
```

## Explanation

The original text refers to the incorrect TLV (IGP metric TLV, TLV 1095) for Prefix NLRIs. The correction uses the correct TLV (Prefix Metric TLV, TLV 1155), which is consistent with the specification.  This inconsistency could affect implementations that rely on the correct TLV to identify normal routing prefixes.
