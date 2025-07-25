# Errata 6123 - RFC 8446

- **RFC Title:** The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid6123](https://www.rfc-editor.org/errata/eid6123)

```
Section 2 says:


The handshake protocol allows peers to negotiate a protocol version, select cryptographic algorithms, optionally authenticate each other, and establish shared secret keying material.

Notes:

Only client authentication is optional (albeit, server authentication is implicit for PSK-only key exchange mode)

Paul Wouters(AD): corrected with the following text:

The handshake protocol allows peers to negotiate a protocol version, select cryptographic algorithms, authenticate each other (with client authentication being optional), and establish shared secret keying material.
```

## Explanation

The original description is imprecise about the optionality of authentication.  The corrected text clarifies that client authentication is optional, but server authentication is generally required. This is a clarification rather than a correction of an error affecting implementation.
