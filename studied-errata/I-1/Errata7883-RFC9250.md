# Errata 7883 - RFC 9250

- **RFC Title:** DNS over Dedicated QUIC Connections
- **RFC Publication Date:** May 2022
- Link to original errata report: [rfc-editor.org/errata/eid7883](https://www.rfc-editor.org/errata/eid7883)

```
Section 7.5 says:


Implementations SHOULD use the mechanisms defined in Section 5.4 to
mitigate this attack.

It should say:

Implementations MUST use the padding mechanisms defined in Section 5.4
to mitigate this attack.

Notes:

Section 5.4 states that "[i]mplementations MUST protect against the traffic analysis attacks described in Section 7.5", but Section 7.5 describes that obligation as a "SHOULD". "MUST" is correct, and the inconsistent "SHOULD" in Section 7.5 is an error.

-- Verifier (Eric Vyncke) note --

The short discussion on the DPRIVE WG list has indicated that 2 authors are in favour of verifying this errata.
```

## Explanation

The erratum highlights an inconsistency between sections 5.4 and 7.5 of RFC 9250. Section 5.4 mandates the use of padding mechanisms ("MUST"), while Section 7.5 only recommends it ("SHOULD"). This contradiction creates an inconsistent requirement, directly affecting implementation.  The correction ensures consistent and mandatory implementation of the security measure, resolving the inconsistency. Therefore it is classified as INCONSISTENT.
