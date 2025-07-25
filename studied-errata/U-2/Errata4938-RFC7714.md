# Errata 4938 - RFC 7714

- **RFC Title:** AES-GCM Authenticated Encryption in the Secure Real-time Transport Protocol (SRTP)
- **RFC Publication Date:** December 2015
- Link to original errata report: [rfc-editor.org/errata/eid4938](https://www.rfc-editor.org/errata/eid4938)

```
Section 11 says:


A Key Derivation Function (KDF) is used to derive all of the required
encryption and authentication keys from a secret value shared by the
endpoints.  The AEAD_AES_128_GCM algorithm MUST use the (128-bit)
AES_CM PRF KDF described in [RFC3711].  AEAD_AES_256_GCM MUST use the
AES_256_CM_PRF KDF described in [RFC6188].

It should say:

A Key Derivation Function (KDF) is used to derive all of the required
encryption and authentication keys from a secret value shared by the
endpoints.  The AEAD_AES_128_GCM algorithm MUST use the (128-bit)
AES_CM PRF KDF described in [RFC3711].  AEAD_AES_256_GCM MUST use the
AES_256_CM_PRF KDF described in [RFC6188].  Since the KDF functions in
those RFCs assume as input a 112-bit master salt, the 96-bit master
salt specified in this document must be multiplied by 2^16 to form the
112-bit salt used as the master salt in those key derivation functions.

Notes:

The salt specified in RFC 7714 is 96 bits in length, but intended for use in KDF functions defined in RFC 3711.  This led to different interpretations when implementing this RFC.  A more complete description was presented on the avtcore mailing list (https://mailarchive.ietf.org/arch/msg/avt/IRfLuNKglD3qhqwSz3v3t0CG6fA) and, after some dialog, there seemed to be agreement to adopt the approach most widely implemented (https://mailarchive.ietf.org/arch/msg/avt/-C1cIWQXpyzS2KfBjGR6B2kK92w).  This suggested text is intended to reflect that agreement.  In effect, 16 zero bits are padded to the right of the salt value  defined in RFC 7714 (creating a 112 bit salt value) before it is used as described in the KDF functions defined in RFC 3711 that require a 112 bit salt value.
```

## Explanation

The original text does not specify how to handle the 96-bit master salt defined in RFC 7714 with the 112-bit master salt assumed by the KDF functions in RFC 3711. The correction clarifies that the 96-bit salt must be multiplied by 2^16 to create a 112-bit salt, resolving the inconsistency.
