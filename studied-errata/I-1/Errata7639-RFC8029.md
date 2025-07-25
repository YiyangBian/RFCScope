# Errata 7639 - RFC 8029

- **RFC Title:** Detecting Multiprotocol Label Switched (MPLS) Data-Plane Failures
- **RFC Publication Date:** March 2017
- Link to original errata report: [rfc-editor.org/errata/eid7639](https://www.rfc-editor.org/errata/eid7639)

```
Section 4.5 says:


If the Reply Mode in the echo request is "Reply via an
IPv4 UDP packet with Router Alert", then the IP header MUST contain
the Router Alert IP Option of value 0x0 [RFC2113] for IPv4 or 69
[RFC7506] for IPv6.

It should say:

If the Reply Mode in the echo request is "Reply via an
IPv4/IPv6 UDP packet with Router Alert", then the IP header MUST contain
the Router Alert IP Option of value 0x0 [RFC2113] for IPv4 or 69
[RFC7506] for IPv6.

Notes:

The description of the Reply Mode recorded in the IANA "Reply Modes" sub-registry of the "Multiprotocol Label Switching (MPLS) Label Switched Paths (LSPs) Ping Parameters" registry is "Reply via an IPv4/IPv6 UDP packet with Router Alert".
```

## Explanation

The original text only mentions IPv4 packets in the description of the Reply Mode, while the IANA registry and the actual behavior include both IPv4 and IPv6 packets. This omission creates an inconsistency between the description and the broader functionality.
