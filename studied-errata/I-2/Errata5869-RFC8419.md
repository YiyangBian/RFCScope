# Errata 5869 - RFC 8419

- **RFC Title:** Use of Edwards-Curve Digital Signature Algorithm (EdDSA) Signatures in the Cryptographic Message Syntax (CMS)
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid5869](https://www.rfc-editor.org/errata/eid5869)

```
Section 2.3 says:


      hashalgs  OBJECT IDENTIFIER  ::=  { joint-iso-itu-t(2)
                              country(16) us(840) organization(1)
                              gov(101) csor(3) nistalgorithm(4) 2 }

It should say:

      hashAlgs  OBJECT IDENTIFIER  ::=  { joint-iso-itu-t(2)
                              country(16) us(840) organization(1)
                              gov(101) csor(3) nistalgorithm(4) 2 }

Notes:

The "hashAlgs" requires a capital letter for the other definitions in the section.
```

## Explanation

"hashAlgs" becomes an undefined term if the only provided definition is for "hashalgs".
