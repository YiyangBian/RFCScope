# Errata 7565 - RFC 8555

- **RFC Title:** Automatic Certificate Management Environment (ACME)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid7565](https://www.rfc-editor.org/errata/eid7565)

```
Section 8.1 says:


 The "Thumbprint" step indicates the computation specified in
   [RFC7638], using the SHA-256 digest [FIPS180-4].  As noted in
   [RFC7518] any prepended zero octets in the fields of a JWK object
   MUST be stripped before doing the computation.

It should say:

The "Thumbprint" step indicates the computation specified in
   [RFC7638], using the SHA-256 digest [FIPS180-4].  As noted in
   [RFC7518] any additional prepended zero octets in the fields of a JWK object
   MUST be stripped before doing the computation.  
   Fixed length fields such as found in ECDSA keys should be their natural length and 
   leading zero octets should not be stripped.

Notes:

This comment was really aimed at the leading 0 octet sometimes used with RSA, but the comment is not RSA specific. ECDSA keys can have fixed length fields (X,Y) where there can be leading zeros.  This led me astray in implementing an ECDSA thumbprint routine for ACME. The result was that 1/128 ECDSA keys failed to generate t humbp[rint as leading zeros were removed.
```

## Explanation

The description in Section 8.1 regarding zero octet stripping before thumbprint computation is unclear and inconsistent when applied to ECDSA keys with fixed-length fields.  The original text implies that all leading zero octets should be stripped, but this is incorrect for ECDSA, leading to incorrect thumbprint calculation. This inconsistency directly impacts the correct implementation of the thumbprint calculation for ECDSA keys and is therefore classified as INCONSISTENT.
