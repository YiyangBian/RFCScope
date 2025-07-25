# Errata 5983 - RFC 8555

- **RFC Title:** Automatic Certificate Management Environment (ACME)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid5983](https://www.rfc-editor.org/errata/eid5983)

```
Section 9.1 says:


   A file of this type contains one or more certificates encoded with
   the PEM textual encoding, according to [RFC7468].  The textual
   encoding of certificates in this file MUST use the strict encoding
   and MUST NOT include explanatory text.  The ABNF for this format is
   as follows, where "stricttextualmsg" and "eol" are as defined in
   Section 3 of RFC 7468:

   certchain = stricttextualmsg *(eol stricttextualmsg)

It should say:

   A file of this type contains one or more certificates encoded with
   the PEM textual encoding, according to [RFC7468].  The textual
   encoding of certificates in this file MUST use the strict encoding
   and MUST NOT include explanatory text.  The ABNF for this format is
   as follows, where "stricttextualmsg" is as defined in
   Section 3 of RFC 7468:

   certchain = stricttextualmsg *(stricttextualmsg)

Notes:

Examples within RFC 8555 indicate that only one EOL should be present between entries in the PEM chain.

RFC 7468 already defines a stricttextualmsg as ending with EOL
stricttextualmsg = preeb eol
                           strictbase64text
                           posteb eol

If a second EOL is to be added before each strict textual message this would result in a blank line between entries.  The prior example in https://tools.ietf.org/html/rfc8555#section-7.4.2 indicates an intention for only one EOL marker to be used:
   -----BEGIN CERTIFICATE-----
   [End-entity certificate contents]
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   [Issuer certificate contents]
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   [Other certificate contents]
   -----END CERTIFICATE-----
```

## Explanation

The ABNF in Section 9.1 is inconsistent with the examples provided in the RFC and the definition of `stricttextualmsg` in RFC 7468. The ABNF implies multiple EOL characters between certificates, while the examples and the definition of `stricttextualmsg` suggest only one EOL character. This inconsistency affects the correct interpretation and implementation of the certificate chain format and is therefore classified as INCONSISTENT.
