# Errata 5483 - RFC 8446

- **RFC Title:** The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid5483](https://www.rfc-editor.org/errata/eid5483)

```
Section 4.2.8.2 says:


For X25519 and X448, the contents of the public value are the byte
string inputs and outputs of the corresponding functions defined in
[RFC7748]: 32 bytes for X25519 and 56 bytes for X448.

It should say:

For X25519 and X448, the contents of the public value are the byte
string outputs of the corresponding functions defined in [RFC7748]: 32
bytes for X25519 and 56 bytes for X448.

Notes:

Per Section 7.4.2 of this RFC and Section 6 of RFC7748, the byte string inputs to the corresponding ECDH scalar multiplication function are the private key and the u-coordinate of the standard public base point, the former of which of course must not be transmitted and the latter of which is a known constant.

Paul Wouters (AD): Resolved but with the following Corrected Text:

For X25519 and X448, the contents of the public value is the K_A or
K_B value described in Section 6 of [RFC7748].  This is 32 bytes for
X25519 and 56 bytes for X448.

From another perspective, including the byte string inputs in the contents of the public value would contradict the resulting content sizes given at the end of the cited paragraph as well as the statement in Section 7.4.2 that the public key put into the KeyShareEntry is the output of ECDH scalar multiplication function.
```

## Explanation

The original text states that the public value includes the byte string inputs to the X25519 and X448 functions, which is incorrect. The correction clarifies that only the byte string outputs are included, resolving the inconsistency with Section 7.4.2 and RFC 7748.
