# Errata 6938 - RFC 8013

- **RFC Title:** Forwarding and Control Element Separation (ForCES) Inter-FE Logical Functional Block (LFB)
- **RFC Publication Date:** February 2017
- Link to original errata report: [rfc-editor.org/errata/eid6938](https://www.rfc-editor.org/errata/eid6938)

```
Section 5.1.1 says:


Caution needs to be exercised on how low the resulting reported link MTU could be: for IPv4 packets, the minimum size is 64 octets [RFC791] and for IPv6 the minimum size is 1280 octets [RFC2460].

It should say:

Caution needs to be exercised on how low the resulting reported link MTU could be: for IPv4 the recommended minimum size is 576 octets [RFC1122] and for IPv6 the minimum size is 1280 octets [RFC2460].

Notes:

The original text mixed minimum packet size with minimum MTU size.
```

## Explanation

The original text incorrectly states the minimum IPv4 packet size, confusing it with the minimum MTU.  The correction uses the recommended minimum IPv4 MTU size, resolving the inconsistency. This inconsistency would mislead implementations calculating or interpreting the reported link MTU.
