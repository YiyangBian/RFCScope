# Errata 5127 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5127](https://www.rfc-editor.org/errata/eid5127)

```
Section 5.2. says:


IMSK = First 32 octets of TLS-PRF(EMSK, "TEAPbindkey@ietf.org" |
     "\0" | 64)

It should say:

IMSK = First 32 octets of TLS-PRF(EMSK, "TEAPbindkey@ietf.org" |
     "\0", 64)

Notes:

According to

RFC5246 The Transport Layer Security (TLS) Protocol Version 1.2

5.  HMAC and the Pseudorandom Function

"TLS's PRF is created by applying P_hash to the secret as:

      PRF(secret, label, seed) = P_<hash>(secret, label + seed)"
```

## Explanation

The erratum corrects the formula for IMSK calculation. The original formula incorrectly includes a pipe symbol between "\0" and 64, where it should be a comma.  This is an inconsistency because the corrected formula adheres to the TLS-PRF specification described in RFC 5246, whereas the original formula does not. This inconsistency can lead to incorrect IMSK generation, affecting the security of the TEAP protocol.
