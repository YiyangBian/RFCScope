# Errata 7734 - RFC 9085

- **RFC Title:** Border Gateway Protocol - Link State (BGP-LS) Extensions for Segment Routing
- **RFC Publication Date:** August 2021
- Link to original errata report: [rfc-editor.org/errata/eid7734](https://www.rfc-editor.org/errata/eid7734)

```
Section 2.3.5 says:


11 or 12 octets depending on the label or index encoding of the SID.

It should say:

15 or 16 octets depending on the label or index encoding of the SID.

Notes:

Length of the TLV does not account for the Prefix-SID Sub-TLVs type and length fields: 2 octets each = 4 octets in total.
This is valid for all variants: IS-IS, OSPFv2 and OSPFv3.

Note: see also https://mailarchive.ietf.org/arch/msg/idr/G_3KN-XXqyXbSXO1doiNJbK_gIA/
```

## Explanation

The original text incorrectly calculates the length of the TLV, omitting the type and length fields of the Prefix-SID Sub-TLVs. The correction adds these four octets to the length calculation, making it consistent with the actual TLV size.
