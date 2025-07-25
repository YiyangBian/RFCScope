# Errata 7543 - RFC 9008

- **RFC Title:** Using RPI Option Type, Routing Header for Source Routes, and IPv6-in-IPv6 Encapsulation in the RPL Data Plane
- **RFC Publication Date:** April 2021
- Link to original errata report: [rfc-editor.org/errata/eid7543](https://www.rfc-editor.org/errata/eid7543)

```
Section 6 says:


As the Rank information in the RPI artifact is changed at each hop, it
will typically be zero when it arrives at the DODAG root.

It should say:

As the Rank information in the RPI artifact is changed at each hop, it
will typically be non-zero when it arrives at the DODAG root.

Notes:

The SenderRank is 0 if: 
- The packet comes from Internet (and has an RPI)
- The packet has not been forwarded (ie. if the source is a direct child of the DODAG root), as RFC 6550 section 11.2 tells to set SenderRank to 0 at the source.

The typical case is rather a packet that arrives at the DODAG root from a child node forwarding a packet, in which case SenderRank is set to DAGRank(rank) > 0.
```

## Explanation

The original text incorrectly states that the Rank information in the RPI artifact will typically be zero when it arrives at the DODAG root. The correction clarifies that it will typically be non-zero, which is the more accurate and common case. This inconsistency could lead to misinterpretations of the RPI artifact.
