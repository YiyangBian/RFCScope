# Errata 7652 - RFC 9252

- **RFC Title:** BGP Overlay Services Based on Segment Routing over IPv6 (SRv6)
- **RFC Publication Date:** July 2022
- Link to original errata report: [rfc-editor.org/errata/eid7652](https://www.rfc-editor.org/errata/eid7652)

```
Section 3.2.1 says:


   Transposition Offset indicates the bit position, and Transposition
   Length indicates the number of bits that are being taken out of the
   SRv6 SID value and encoded in the MPLS Label field.  The bits that
   have been shifted out MUST be set to 0 in the SID value.

It should say:

   Transposition Offset indicates the bit position and Transposition
   Length indicates the number of bits that are being taken out of the
   SRv6 SID value and put into high order bits of MPLS label field. The
   bits that have been shifted out MUST be set to 0 in the SID value.

Notes:

This errata reverses an editorial change that was made during the AUTH48 phase and restores the text that came from the WG and IESG review. Refer https://datatracker.ietf.org/doc/html/draft-ietf-bess-srv6-services-15#page-10

This change was made during the AUTH48 since the "high order bits" was already covered under various subsections of Sec 6. However, readers have reported that there are other places in Sec 6 and Sec 5 where transposition also occurs and that the original text was still required.
```

## Explanation

The original description of Transposition Offset and Transposition Length is unclear about the placement of the extracted bits within the MPLS Label field. The correction clarifies that these bits are put into the high-order bits of the MPLS Label field, resolving the ambiguity.
