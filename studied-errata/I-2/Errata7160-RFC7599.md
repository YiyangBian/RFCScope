# Errata 7160 - RFC 7599

- **RFC Title:** Mapping of Address and Port using Translation (MAP-T)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid7160](https://www.rfc-editor.org/errata/eid7160)

```
Section 10.1 says:


Translating an IPv4 packet to carry it across the MAP domain will increase its size (typically by 20 bytes).

It should say:

Translating an IPv4 packet to carry it across the MAP domain will increase its size (typically either 20 or 28 bytes with fragmentation).

Notes:

In the context of MTU, it is important to account for packet fragmentation. If an IPv4 packet is fragmented, the size will increase by 28 bytes during translation. The IPv6 header is 20 bytes larger than the IPv4 header, and in addition the 8 byte IPv6 Fragmentation Header must be added.

----
Verifier note
==========
 with help of Yong Cui: fragmentation indeed needs to be taken into account.
```

## Explanation

The original text only considers the size increase without fragmentation, while fragmentation can also occur, leading to a different size increase.  The correction accounts for both scenarios, providing a more complete and accurate description of the size increase during translation. This inconsistency would lead to incorrect calculations of the size of translated packets.
