# Errata 6955 - RFC 7915

- **RFC Title:** IP/ICMP Translation Algorithm
- **RFC Publication Date:** June 2016
- Link to original errata report: [rfc-editor.org/errata/eid6955](https://www.rfc-editor.org/errata/eid6955)

```
Section 4.5 says:


Calculating an IPv6 checksum and forwarding the packet (which has performance implications).

It should say:

Calculating an UDP checksum and forwarding the packet (which has performance implications).

Notes:

IPv6 doesn't have a checksum. The text appears to refer to the UDP checksum
```

## Explanation

The errata corrects a factual error in Section 4.5. The original text incorrectly mentions calculating an IPv6 checksum, while IPv6 doesn't have a header checksum. This error is directly related to implementation as it provides an instruction that is impossible to implement correctly and suggests a different protocol's checksum, UDP checksum, instead.  The correction is essential for correct implementation.
