# Errata 7817 - RFC 9252

- **RFC Title:** BGP Overlay Services Based on Segment Routing over IPv6 (SRv6)
- **RFC Publication Date:** July 2022
- Link to original errata report: [rfc-editor.org/errata/eid7817](https://www.rfc-editor.org/errata/eid7817)

```
Section 3.2.1 says:


   As defined in [RFC8986], the sum of the Locator Block Length (LBL),
   Locator Node Length (LNL), Function Length (FL), and Argument Length
   (AL) fields MUST be less than or equal to 128 and greater than the
   sum of Transposition Offset and Transposition Length.

It should say:

   As defined in [RFC8986], the sum of the Locator Block Length (LBL),
   Locator Node Length (LNL), Function Length (FL), and Argument Length
   (AL) fields MUST be less than or equal to 128 and greater than or
   equal to the sum of Transposition Offset and Transposition Length.

Notes:

The sum of Trans Off and Trans Length can be equal to the LBL+LNL+FL+AL when the last part of the SID (function or argument) is getting transposed.

This is clear also from the example below in the next paragraph of the same section:

   As an example, consider that the sum of the Locator Block and the
   Locator Node parts is 64.  For an SRv6 SID where the entire Function
   part of size 16 bits is transposed, the transposition offset is set
   to 64 and the transposition length is set to 16.  While for an SRv6
   SID for which the FL is 24 bits and only the lower order 20 bits are
   transposed (e.g., due to the limit of the MPLS Label field size), the
   transposition offset is set to 68 and the transposition length is set
   to 20.
```

## Explanation

The original text incorrectly requires that the sum of LBL, LNL, FL, and AL be strictly greater than the sum of Transposition Offset and Transposition Length. The correction changes this to greater than or equal to, which is consistent with the example provided and the possible scenarios where the last part of the SID is transposed.
