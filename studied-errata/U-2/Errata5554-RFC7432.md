# Errata 5554 - RFC 7432

- **RFC Title:** BGP MPLS-Based Ethernet VPN
- **RFC Publication Date:** February 2015
- Link to original errata report: [rfc-editor.org/errata/eid5554](https://www.rfc-editor.org/errata/eid5554)

```
Section 7 says:


Clarifications to following sub-sections:
Section 7.1
Section 7.2
Section 7.5


It should say:

Section 7.1:
Add below text to the section 7.1 regarding the encoding
of MPLS label field:

"The value of the 20-bit MPLS label is encoded in the high-order 
20 bits of the 3 octets MPLS Label field."

Section 7.2:
Add below text to the section 7.2 regarding the encoding 
of both the MPLS label fields:

"The value of the 20-bit MPLS label is encoded in the high-order
20 bits of the 3 octets MPLS Label1 and MPLS Label2 fields."

Section 7.5:
Add below text to the section 7.5 regarding the encoding of 
ESI Label field:

"The value of the 20-bit MPLS label is encoded in the high-order
20 bits of the 3 octets ESI Label field."


Notes:

MPLS label is a 20-bit value and is stored in a 3 bytes field in a packet. 
The 20-bit MPLS label value is generally stored in higher order 20 bits 
of the 3 octet label field. The exact encoding to be followed for storing 
MPLS label values are not explicitly mentioned in the RFC 7432 under 
section 7.1, 7.2 and 7.5 for different types of EVPN routes. This lead to
ambiguity in different  implementations. Hence a clarification is required.
```

## Explanation

The original specification lacks explicit details on the encoding of MPLS label values within 3-octet fields. The lack of this information leads to ambiguity in implementations, resulting in different interpretations of the encoding.  The erratum's suggested additions address this incompleteness, making the specification more precise and improving interoperability.
