# Errata 5610 - RFC 8226

- **RFC Title:** Secure Telephone Identity Credentials: Certificates
- **RFC Publication Date:** February 2018
- Link to original errata report: [rfc-editor.org/errata/eid5610](https://www.rfc-editor.org/errata/eid5610)

```
Section Appendix A says:


    JWTClaimPermittedValuesList ::= SEQUENCE SIZE (1..MAX) Of
                                      JWTClaimPermittedValues

It should say:

    JWTClaimPermittedValuesList ::= SEQUENCE SIZE (1..MAX) OF
                                      JWTClaimPermittedValues

Notes:

The ASN.1 Compiler require "OF" to be all capital letters.
```

## Explanation

This is a syntax error in the ASN.1 module.
