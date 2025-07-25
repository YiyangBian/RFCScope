# Errata 7081 - RFC 8754

- **RFC Title:** IPv6 Segment Routing Header (SRH)
- **RFC Publication Date:** March 2020
- Link to original errata report: [rfc-editor.org/errata/eid7081](https://www.rfc-editor.org/errata/eid7081)

```
Section 4.1.1 says:


A reduced SRH does not contain the first segment of the related SR
Policy (the first segment is the one already in the DA of the IPv6
header), and the Last Entry field is set to n-2, where n is the
number of elements in the SR Policy.


It should say:

A reduced SRH does not contain the first segment of the related SR
Policy (the first segment is the one already in the DA of the IPv6
header), and the Last Entry field is set to n-2, where n is the
number of elements in the SR Policy.

When an SRH includes TLVs and only one 128-bit Segment, the reduced
SRH MUST NOT be used to avoid errors of SRH TLV processing defined
in section 2.1. 


Notes:

When only one single Segment is included in the SRH, the last entry will be 0 forever, so a segment endpoint node cannot specify whether the last Segment is included or removed from the SRH. 

As defined in section 2.1, only when the header length of SRH larger then (0+1)*2, the TLVs will be processed. 
1.	When the Segment is removed, Segment Lefts = Last Entry = 0, each segment endpoint node will skip the bytes 8-16, and then process the following bytes following the TLV processing rules, which will cause errors.
2.	When the segment is not removed, Segment Lefts = Last Entry = 0, each segment endpoint will process the TLVs correctly from byte 8+16. 

Choosing option 2 can avoid processing error of SRH TLVs and be compatible with the current hardware implementation. Thus option 1 MUST be avoid in implementation.
```

## Explanation

The original text does not address the case where an SRH contains only one segment and TLVs. The correction adds a restriction against using a reduced SRH in this case, avoiding potential errors in SRH TLV processing.  This inconsistency would lead to implementations incorrectly handling reduced SRHs with only one segment and TLVs.
