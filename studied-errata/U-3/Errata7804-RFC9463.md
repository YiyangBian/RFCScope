# Errata 7804 - RFC 9463

- **RFC Title:** DHCP and Router Advertisement Options for the Discovery of Network-designated Resolvers (DNR)
- **RFC Publication Date:** November 2023
- Link to original errata report: [rfc-editor.org/errata/eid7804](https://www.rfc-editor.org/errata/eid7804)

```
Section 6.1 says:


Note that the "Addr Length", "ipv6-address(es)", and "Service 
Parameters (SvcParams)" fields are not present if the ADN-only mode 
is used (Section 3.1.6).

It should say:

Note that the "Addr Length", "ipv6-address(es)", "SvcParams 
Length", and "Service Parameters (SvcParams)" fields are not 
present if the ADN-only mode is used (Section 3.1.6).

Notes:

The paragraph is presumably copied from section 4.1 (DHCPv6 Encrypted DNS Option), and omits the "SvcParams Length" field, which is only present in the IPv6 RA Encrypted DNS Option. Mandating the presence of a superfluous length field when using the ADN-only mode seems like an oversight.
```

## Explanation

The erratum points out an omission in Section 6.1 of RFC 9463.  The original text incorrectly states that only "Addr Length", "ipv6-address(es)", and "Service Parameters (SvcParams)" fields are absent in ADN-only mode. The correction adds "SvcParams Length", which is a necessary field.  This omission creates an inconsistency between the description in Section 6.1 and the actual specification of the ADN-only mode, directly impacting implementation.
