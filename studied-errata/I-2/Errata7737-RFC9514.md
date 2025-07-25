# Errata 7737 - RFC 9514

- **RFC Title:** Border Gateway Protocol - Link State (BGP-LS) Extensions for Segment Routing over IPv6 (SRv6)
- **RFC Publication Date:** December 2023
- Link to original errata report: [rfc-editor.org/errata/eid7737](https://www.rfc-editor.org/errata/eid7737)

```
Section 5.1 says:


   The IPv6 Prefix matching the locator may also be advertised as prefix
   reachability by the underlying routing protocol.  In this case, the
   Prefix NLRI would also be associated with the Prefix Metric TLV
   [RFC7752] that carries the routing metric for this prefix.  A Prefix
   NLRI that has been advertised with a SRv6 Locator TLV is also
   considered a normal routing prefix (i.e., prefix reachability) only
   when there is also an IGP Metric TLV (TLV 1095) associated it.
   Otherwise, it is only considered an SRv6 Locator advertisement.

It should say:

   The IPv6 Prefix matching the locator may also be advertised as prefix
   reachability by the underlying routing protocol.  In this case, the
   Prefix NLRI would also be associated with the Prefix Metric TLV
   [RFC7752] that carries the routing metric for this prefix.  A Prefix
   NLRI that has been advertised with a SRv6 Locator TLV is also
   considered a normal routing prefix (i.e., prefix reachability) only
   when there is also a Prefix Metric TLV (TLV 1155) associated with it.
   Otherwise, it is only considered an SRv6 Locator advertisement.

Notes:

The current text is referring to the wrong BGP-LS TLV. Since the SRv6 Locator TLV is associated with a Prefix NLRI, the "Prefix Metric TLV (TLV 1155)" should be referenced here since the "IGP metric TLV (TLV 1095)" is associated with a Link NLRI.

Verifier note: In addition to the fix proposed by Ketan, I added a preposition: "associated with it".
```

## Explanation

The original text refers to the incorrect TLV (IGP metric TLV, TLV 1095) for Prefix NLRIs. The correction uses the correct TLV (Prefix Metric TLV, TLV 1155), which is consistent with the specification. This inconsistency could affect implementations that rely on the correct TLV to identify normal routing prefixes.
