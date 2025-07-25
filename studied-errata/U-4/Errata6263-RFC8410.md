# Errata 6263 - RFC 8410

- **RFC Title:** Algorithm Identifiers for Ed25519, Ed448, X25519, and X448 for Use in the Internet X.509 Public Key Infrastructure
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid6263](https://www.rfc-editor.org/errata/eid6263)

```
Section 7 says:


NOTE: There exist some private key import functions that have not picked up the new ASN.1 structure OneAsymmetricKey that is defined in [RFC7748].

It should say:

NOTE: There exist some private key import functions that have not picked up the new ASN.1 structure OneAsymmetricKey that is defined in [RFC5958].

Notes:

RFC7748 does not define or even mention OneAsymmetricKey. The correct reference should be RFC5958 "Asymmetric Key Packages"
```

## Explanation

The original text incorrectly cites RFC 7748 as the source for the OneAsymmetricKey ASN.1 structure.  The correction cites RFC 5958, which is the correct source. This inconsistency would affect those trying to locate the correct ASN.1 definition.
