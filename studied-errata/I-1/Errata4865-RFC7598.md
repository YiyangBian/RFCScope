# Errata 4865 - RFC 7598

- **RFC Title:** DHCPv6 Options for Configuration of Softwire Address and Port-Mapped Clients
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid4865](https://www.rfc-editor.org/errata/eid4865)

```
Section 4.3 says:


dmr-prefix6-len: 8 bits long; expresses the bitmask length of the 
IPv6 prefix specified in the dmr-ipv6-prefix field.  Allowed
values range from 0 to 128.

It should say:

dmr-prefix6-len: 8 bits long; expresses the bitmask length of the 
IPv6 prefix specified in the dmr-ipv6-prefix field.  Allowed
values range from 0 to 96.

Notes:

This field is used to provision the default mapping rule prefix length, which is defined in section 5.1 of RFC7599:
The DMR IPv6 prefix length SHOULD be 64 bits long by default and in any case MUST NOT exceed 96 bits.
```

## Explanation

The original specification allows values up to 128 for the `dmr-prefix6-len` field, while RFC 7599 limits the maximum length to 96. This inconsistency needs to be resolved to ensure that implementations conform to both specifications. The corrected range is consistent with RFC 7599.
