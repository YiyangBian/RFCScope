# Errata 5113 - RFC 7788

- **RFC Title:** Home Networking Control Protocol
- **RFC Publication Date:** April 2016
- Link to original errata report: [rfc-editor.org/errata/eid5113](https://www.rfc-editor.org/errata/eid5113)

```
Section 10 says:


10.2.2.  DHCPv6-Data TLV

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |    Type: DHCPv6-Data (37)     |          Length: > 0          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[...]

10.2.3.  DHCPv4-Data TLV

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type: DHCPv4-Data (38)    |          Length: > 0          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


It should say:

10.2.2.  DHCPv6-Data TLV

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |    Type: DHCPv6-Data (38)     |          Length: > 0          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[...]

10.2.3.  DHCPv4-Data TLV

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type: DHCPv4-Data (37)    |          Length: > 0          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


Notes:

Section 13 (IANA Considerations) of the document says:

      37: DHCPv4-Data

      38: DHCPv6-Data

Those code points from Section 13 are in the "HNCP TLV Types" IANA registry as well as in the current source code of shncpd and tcpdump. The code points shown in Sections 10.2.2 and 10.2.3 were likely swapped by mistake.

-- Verifier note --
The IANA registry for HNCP TLV types (https://www.iana.org/assignments/dncp-registry/dncp-registry.xhtml#hncp-tlv-types) has indeed 37 for DHCPv4 and the open source SHNCPD has the same https://github.com/jech/shncpd/blob/master/receive.c
```

## Explanation

The Type values for DHCPv4-Data and DHCPv6-Data TLVs are swapped in Section 10.  This inconsistency is between the values shown in Section 10 and the values defined in Section 13 and the IANA registry.  This inconsistency would affect implementations parsing or generating these TLVs.
