# Errata 5703 - RFC 8422

- **RFC Title:** Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS) Versions 1.2 and Earlier
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid5703](https://www.rfc-editor.org/errata/eid5703)

```
Section 5.10. says:


All RSA signatures must be generated and verified according to
   Section 7.2 of [RFC8017].

It should say:

All RSA signatures must be generated and verified according to
   Section 8.2 of [RFC8017].

Notes:

Section 7.2 of RFC 8017 describes the RSAES-PKCS1-v1_5 encryption scheme. Section 8.2 of RFC 8017 describes the RSASSA-PKCS1-v1_5 signature scheme. The original text contradicts the natural expectation and is probably wrong. If it was intended, there should have been a thorough explanation (like in the well-known case of IKEv1 using the encryption scheme for signing).
```

## Explanation

The original text references the RSAES-PKCS1-v1_5 encryption scheme instead of the RSASSA-PKCS1-v1_5 signature scheme for RSA signature generation and verification. This inconsistency between the referenced section and the expected signature scheme affects the correct implementation of RSA signatures.
