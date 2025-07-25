# Errata 5353 - RFC 8103

- **RFC Title:** Using ChaCha20-Poly1305 Authenticated Encryption in the Cryptographic Message Syntax (CMS)
- **RFC Publication Date:** February 2017
- Link to original errata report: [rfc-editor.org/errata/eid5353](https://www.rfc-editor.org/errata/eid5353)

```
Section 6 says:


   The amount of encrypted data possible in a single invocation of
   AEAD_CHACHA20_POLY1305 is 2^32-1 blocks of 64 octets each, because of
   the size of the block counter field in the ChaCha20 block function.
   This gives a total of 247,877,906,880 octets, which is likely to be
   sufficient to handle the size of any CMS content type.  Note that the
   ciphertext length field in the authentication buffer will accommodate
   2^64 octets, which is much larger than necessary.

It should say:

   The amount of encrypted data possible in a single invocation of
   AEAD_CHACHA20_POLY1305 is 2^32-1 blocks of 64 octets each, because of
   the size of the block counter field in the ChaCha20 block function.
   This gives a total of 274,877,906,880 octets, which is likely to be
   sufficient to handle the size of any CMS content type.  Note that the
   ciphertext length field in the authentication buffer will accommodate
   2^64 octets, which is much larger than necessary.

Notes:

The calculated total number of octets that can be encrypted in a single invocation is incorrect. See RFC Errata, Erratum ID 4858, RFC 7539.
```

## Explanation

The original calculation of the maximum encrypted data size for AEAD_CHACHA20_POLY1305 is incorrect. The correction provides the correct calculation, resolving the inconsistency. This inconsistency would affect implementations that rely on the correct maximum size for encryption.
