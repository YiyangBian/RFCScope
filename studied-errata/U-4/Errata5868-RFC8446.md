# Errata 5868 - RFC 8446

- **RFC Title:** The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid5868](https://www.rfc-editor.org/errata/eid5868)

```
Section 4.2.3 says:


   ECDSA algorithms:  Indicates a signature algorithm using ECDSA
      [ECDSA], the corresponding curve as defined in ANSI X9.62 [ECDSA]
      and FIPS 186-4 [DSS], and the corresponding hash algorithm as
      defined in [SHS].  The signature is represented as a DER-encoded
      [X690] ECDSA-Sig-Value structure.

It should say:

   ECDSA algorithms:  Indicates a signature algorithm using ECDSA
      [ECDSA], the corresponding curve as defined in ANSI X9.62 [ECDSA]
      and FIPS 186-4 [DSS], and the corresponding hash algorithm as
      defined in [SHS].  The signature is represented as a DER-encoded
      [X690] ECDSA-Sig-Value structure as defined in [RFC4492].

Notes:

There is a possibility for confusion as the ECDSA-Sig-Value has two conflicting definitions in authoritative standards. TLS always used the following (see RFC4492):

   ECDSA-Sig-Value ::= SEQUENCE {
     r  INTEGER,
     s  INTEGER
   }

but the publicly accessible SECG SEC1 v2.0 (https://www.secg.org/sec1-v2.pdf) defines it like this:

ECDSA-Sig-Value ::= SEQUENCE {
 r INTEGER,
 s INTEGER,
 a INTEGER OPTIONAL,
 y CHOICE { b BOOLEAN, f FieldElement } OPTIONAL
}

I think using the RFC5480 in the Corrected Text would be cleaner than RFC4492, but the former is not an existing reference, so we would need to update section 12 also.
```

## Explanation

The original description of ECDSA signature representation is ambiguous as the ECDSA-Sig-Value structure has multiple definitions. The corrected description explicitly specifies that the signature must be represented as a DER-encoded ECDSA-Sig-Value structure as defined in RFC 4492, resolving the ambiguity and ensuring consistency.
