# Errata 6809 - RFC 8986

- **RFC Title:** Segment Routing over IPv6 (SRv6) Network Programming
- **RFC Publication Date:** February 2021
- Link to original errata report: [rfc-editor.org/errata/eid6809](https://www.rfc-editor.org/errata/eid6809)

```
Section 4.10 says:


When N receives a packet whose IPv6 DA is S and S is a local End.DX2
SID

It should say:

When N receives a packet whose IPv6 DA is S and S is a local End.DX2V
SID


Notes:

Looks like a typo in the original text
```

## Explanation

The original text uses the incorrect SID type (End.DX2) when referring to a local End.DX2V SID. This inconsistency misidentifies the relevant SID type and may lead to incorrect processing of packets with such SIDs.
