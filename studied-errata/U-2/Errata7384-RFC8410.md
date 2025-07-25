# Errata 7384 - RFC 8410

- **RFC Title:** Algorithm Identifiers for Ed25519, Ed448, X25519, and X448 for Use in the Internet X.509 Public Key Infrastructure
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid7384](https://www.rfc-editor.org/errata/eid7384)

```
Section 9 says:


    sa-Ed25519 SIGNATURE-ALGORITHM ::= {
       IDENTIFIER id-Ed25519
        PARAMS ARE absent
        PUBLIC-KEYS {pk-Ed25519}
        SMIME-CAPS { IDENTIFIED BY id-Ed25519 }
    }

    pk-Ed25519 PUBLIC-KEY ::= {
        IDENTIFIER id-Ed25519
        -- KEY no ASN.1 wrapping --
        PARAMS ARE absent
        CERT-KEY-USAGE {digitalSignature, nonRepudiation,
                        keyCertSign, cRLSign}
        PRIVATE-KEY CurvePrivateKey
    }

It should say:

    sa-Ed25519 SIGNATURE-ALGORITHM ::= {
       IDENTIFIER id-Ed25519
        PARAMS ARE absent
        PUBLIC-KEYS {pk-Ed25519}
        SMIME-CAPS { IDENTIFIED BY id-Ed25519 }
    }

    pk-Ed25519 PUBLIC-KEY ::= {
        IDENTIFIER id-Ed25519
        -- KEY no ASN.1 wrapping --
        PARAMS ARE absent
        CERT-KEY-USAGE {digitalSignature, nonRepudiation,
                        keyCertSign, cRLSign}
        PRIVATE-KEY CurvePrivateKey
    }

   sa-Ed448 SIGNATURE-ALGORITHM ::= {
      IDENTIFIER id-Ed448
       PARAMS ARE absent
       PUBLIC-KEYS {pk-Ed448}
       SMIME-CAPS { IDENTIFIED BY id-Ed448 }
   }

   pk-Ed448 PUBLIC-KEY ::= {
       IDENTIFIER id-Ed448
       -- KEY no ASN.1 wrapping --
       PARAMS ARE absent
       CERT-KEY-USAGE {digitalSignature, nonRepudiation,
                       keyCertSign, cRLSign}
       PRIVATE-KEY CurvePrivateKey
   }

Notes:

The definitions for sa-Ed448 and pk-Ed448 are missing from RFC 8410.
```

## Explanation

The original specification omits the definitions for sa-Ed448 and pk-Ed448, while the description implies that these should be included.  This omission creates an inconsistency, because the definitions are necessary for complete support of Ed448 signatures and keys.  The correction adds these definitions, resolving the inconsistency.
