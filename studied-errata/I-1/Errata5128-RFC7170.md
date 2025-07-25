# Errata 5128 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5128](https://www.rfc-editor.org/errata/eid5128)

```
Section 5.2. says:


IMCK[j] = TLS-PRF(S-IMCK[j-1], "Inner Methods Compound Keys",
                IMSK[j], 60)

It should say:

IMCK[j] = the first 60 octets of TLS-PRF(S-IMCK[j-1],
              "Inner Methods Compound Keys",
              IMSK[j])

Notes:

According to

RFC5246 The Transport Layer Security (TLS) Protocol Version 1.2

5.  HMAC and the Pseudorandom Function

"TLS's PRF is created by applying P_hash to the secret as:

     PRF(secret, label, seed) = P_<hash>(secret, label + seed)"

Paul Wouters(AD): Corrected the text proposed by the original submitter, as it now appears in 7170bis
```

## Explanation

The erratum corrects the formula for calculating IMCK[j]. The original formula incorrectly specifies a length of 60 octets as a parameter to the TLS-PRF function, whereas the TLS-PRF function from RFC 5246 does not take an explicit length parameter.  The correction clarifies that only the first 60 octets of the result are used. This inconsistency would lead to an incorrect calculation of IMCK[j], affecting the security of TEAP.
