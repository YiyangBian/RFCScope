# Errata 7134 - RFC 9252

- **RFC Title:** BGP Overlay Services Based on Segment Routing over IPv6 (SRv6)
- **RFC Publication Date:** July 2022
- Link to original errata report: [rfc-editor.org/errata/eid7134](https://www.rfc-editor.org/errata/eid7134)

```
Section 6.4 says:


                  +---------------------------------------+
                  |  RD (8 octets)                        |
                  +---------------------------------------+
                  |  Ethernet Tag ID (4 octets)           |
                  +---------------------------------------+
                  |  IP Address Length (1 octet)          |
                  +---------------------------------------+
                  |  Originating Router's IP Address      |
                  |          (4 or 16 octets)             |
                  +---------------------------------------+

                        Figure 10: EVPN Route Type 4


It should say:

                  +---------------------------------------+
                  |  RD (8 octets)                        |
                  +---------------------------------------+
                  |Ethernet Segment Identifier (10 octets)|
                  +---------------------------------------+
                  |  IP Address Length (1 octet)          |
                  +---------------------------------------+
                  |  Originating Router's IP Address      |
                  |          (4 or 16 octets)             |
                  +---------------------------------------+

                        Figure 10: EVPN Route Type 4


Notes:

The 2nd field in the figure should be "Ethernet Segment Identifier" of size 10 octets instead of the "Ethernet Tag ID" of size 4 octets.

RFC7432 is the EVPN specification for Ethernet Segment Route (Type 4) and hence the format in section 7.4 of RFC7432 is the correct one.
RFC9252 has an error when showing the encoding format of this EVPN Route Type 4 as a reminder in Figure 10 in section 6.4. 

This is an editorial error.
```

## Explanation

The original figure uses the incorrect field name and size for the Ethernet Tag ID field, which should be the Ethernet Segment Identifier with 10 octets. This inconsistency should be corrected to reflect the correct encoding of EVPN Route Type 4.
