# Errata 7102 - RFC 8754

- **RFC Title:** IPv6 Segment Routing Header (SRH)
- **RFC Publication Date:** March 2020
- Link to original errata report: [rfc-editor.org/errata/eid7102](https://www.rfc-editor.org/errata/eid7102)

```
Section 2 says:


Segments Left:  Defined in [RFC8200], Section 4.4.

It should say:

Segments Left:  Defined in [RFC8200], Section 4.4.
Specifically, for the SRH, the number of unprocessed 
128-bit entries in the Segment List.

Notes:

RFC8754 describes “The encoding of IPv6 segments in the SRH” where IPv6 segments are defined in RFC8402.  RFC8402 describes binding SIDs and adjacency SIDs for SRv6. Both these SID types identify more than a single explicitly listed intermediate node to be visited.

The current definition of Segments Left only indicates it is defined in RFC8200, and RFC8200 defines it as “Number of route  segments remaining, i.e., number of explicitly listed intermediate nodes still to be visited before reaching the final destination”.

Previous versions of draft-ietf-6man-segment-routing-header (0-11) referenced RFC2460/RFC8200 and described the Segments Left field by use in the SRH; as an index into the Segment List. This was removed in later versions (12/13) to consolidate the use of segments left to be specific to the segment processed (now section 4.3.1).  However, that removed the definition of its meaning in the SRH which led to the current issue.

The corrected text restores the meaning of Segments Left for the SRH in relation to Segment List (which is not defined in RFC8200), while still leaving its use during segment processing to the segment definition (section 4.3.1 or future documents).
```

## Explanation

The original text only states that the Segments Left field is defined in RFC 8200 but does not provide its meaning in the context of the SRH. This omission makes the specification incomplete and potentially ambiguous, particularly regarding its relationship to the Segment List within the SRH.
