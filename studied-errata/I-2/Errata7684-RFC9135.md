# Errata 7684 - RFC 9135

- **RFC Title:** Integrated Routing and Bridging in Ethernet VPN (EVPN)
- **RFC Publication Date:** October 2021
- Link to original errata report: [rfc-editor.org/errata/eid7684](https://www.rfc-editor.org/errata/eid7684)

```
Section 6.1 says:


 This route is advertised along with the following extended community:

   *  Tunnel Type Extended Community

It should say:

 This route is advertised along with the following extended community:

   *  Encapsulation Extended Community

Notes:

I guess that solud be Encapsulation Extended Community (or  maybe Tunnel Encapsulation Attribute)

Verifier notes:
See https://mailarchive.ietf.org/arch/msg/bess/TgQR3NHd6wgcYow0B76i7ToBmr0/
```

## Explanation

The original text uses the term "Tunnel Type Extended Community", which is not the correct term for the extended community used in this context. The correction uses the term "Encapsulation Extended Community", which is the correct term and is consistent with the specification.
