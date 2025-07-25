# Errata 5870 - RFC 8360

- **RFC Title:** Resource Public Key Infrastructure (RPKI) Validation Reconsidered
- **RFC Publication Date:** April 2018
- Link to original errata report: [rfc-editor.org/errata/eid5870](https://www.rfc-editor.org/errata/eid5870)

```
Section 4.2.3 says:


       ext-pe-autonomousSysIds-v2 EXTENSION ::= {
         SYNTAX ASIdentifiers
         IDENTIFIED BY id-pe-autonomousSysIds-v2
       }

       id-pe-autonomousSysIds OBJECT IDENTIFIER ::= { id-pe 29 }

It should say:

       ext-pe-autonomousSysIds-v2 EXTENSION ::= {
         SYNTAX ASIdentifiers
         IDENTIFIED BY id-pe-autonomousSysIds-v2
       }

       id-pe-autonomousSysIds-v2 OBJECT IDENTIFIER ::= { id-pe 29 }

Notes:

The "-v2" is missing from the identifier.  It is needed for the ASN.1 module to compile properly.
```

## Explanation

The original ASN.1 definition is missing "-v2" in the OBJECT IDENTIFIER, which is necessary for correct compilation and consistency with the EXTENSION definition.  The missing "-v2" creates an inconsistency that could prevent proper use of the ASN.1 module.
