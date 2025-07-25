# Errata 4677 - RFC 7788

- **RFC Title:** Home Networking Control Protocol
- **RFC Publication Date:** April 2016
- Link to original errata report: [rfc-editor.org/errata/eid4677](https://www.rfc-editor.org/errata/eid4677)

```
Section 8 says:


   A network-wide
   zone is appended to all single labels or unqualified zones in order
   to qualify them. ".home" is the default; however, an administrator
   MAY configure the announcement of a Domain-Name TLV (Section 10.6)
   for the network to use a different one.

It should say:

   A network-wide
   zone is appended to all single labels or unqualified zones in order 
   to qualify them.  A default value for this TLV MUST be set, although 
   the default value of the Domain-Name TLV (Section 10.6) is out of 
   scope of this document, and an administrator MAY configure the 
   announcement of a Domain-Name TLV for the network.

Notes:

It may appear that the use of the label ".home" is unofficially assigning this to be added to the Special Use Domain Registry. That registry can only be updated using the process outlined in RFC6761, therefore the text identifying ".home" as the default network-wide zone is in error.

It is unclear of the IESG and the IETF in publishing this proposed standard if the intent was to use ".home" as an example or placeholder until a name can be reserved.

AD Note: A default label is a requirement for HNCP and its interoperability. As such the Homenet chosen label, ".home", is a strong candidate for the RFC6761 process. The WG will be directed to follow this process and seek (again) the consensus on the ".home" label and work with other IETF WGs as appropriate.
```

## Explanation

The original text states that ".home" is the default network-wide zone, implying that this value is implicitly defined.  The correction clarifies that a default value MUST be set but that the specific default value is out of scope of this document, thus removing the implicit definition of ".home" as the default.  This inconsistency could lead to implementations using ".home" as the default without proper consideration of the process for defining such values.
