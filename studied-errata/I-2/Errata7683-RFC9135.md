# Errata 7683 - RFC 9135

- **RFC Title:** Integrated Routing and Bridging in Ethernet VPN (EVPN)
- **RFC Publication Date:** October 2021
- Link to original errata report: [rfc-editor.org/errata/eid7683](https://www.rfc-editor.org/errata/eid7683)

```
Section 4.2. says:


  2.  However, if PE2 is configured for asymmetric IRB mode, PE2 will
       advertise TS4 MAC/IP information in a MAC/IP Advertisement route
       with a zero Label2 field and no Route Target identifying IP-VRF1.
       In this case, PE2 will install TS4 information in its ARP table
       and BT1.  When a packet from TS2 to TS4 arrives at PE1, a longest
       prefix match on IP-VRF1's route table will yield the local IRB
       interface to BT1, where a subsequent ARP and bridge table lookup
       will provide the information for an asymmetric forwarding mode to
       PE2.

It should say:

  2.  However, if PE2 is configured for asymmetric IRB mode, PE2 will
       advertise TS4 MAC/IP information in a MAC/IP Advertisement route
       with a zero Label2 field and no Route Target identifying IP-VRF1.
       In this case, PE1 will install TS4 information in its ARP table
       and BT1.  When a packet from TS2 to TS4 arrives at PE1, a longest
       prefix match on IP-VRF1's route table will yield the local IRB
       interface to BT1, where a subsequent ARP and bridge table lookup
       will provide the information for an asymmetric forwarding mode to
       PE2.

Notes:

PE1 will use ARP table for forwarding traffic to PE2 - seems like typo
```

## Explanation

The original text incorrectly states that PE2 installs TS4 information in its ARP table, while the correct behavior is for PE1 to install this information. This inconsistency could lead to implementations incorrectly handling asymmetric IRB forwarding.
