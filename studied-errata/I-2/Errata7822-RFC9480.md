# Errata 7822 - RFC 9480

- **RFC Title:** Certificate Management Protocol (CMP) Updates
- **RFC Publication Date:** November 2023
- Link to original errata report: [rfc-editor.org/errata/eid7822](https://www.rfc-editor.org/errata/eid7822)

```
Section A.2 says:


PKIHeader ::= SEQUENCE {
       pvno                INTEGER     { cmp1999(1), cmp2000(2),
                                         cmp2012(3) },

It should say:

PKIHeader ::= SEQUENCE {
       pvno                INTEGER     { cmp1999(1), cmp2000(2),
                                         cmp2021(3) },

Notes:

There is a typo in the ASN.1 module regarding the cmp version.  This was noticed in the RFC 4210-bis draft document and has been corrected there, but also affects this document which has already been published.
```

## Explanation

The original ASN.1 module uses the incorrect version number ("cmp2012") for the CMP protocol. The correction uses the correct version number ("cmp2021"), resolving the inconsistency. This inconsistency would affect implementations that rely on the correct version number for processing CMP messages.
