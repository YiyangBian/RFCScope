# Errata 5324 - RFC 7599

- **RFC Title:** Mapping of Address and Port using Translation (MAP-T)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid5324](https://www.rfc-editor.org/errata/eid5324)

```
Section Appendix A says:


Example 5:

PSID:                    0x20 (provisioned with DHCPv6)

It should say:

Example 5:

PSID:                    0x34 (provisioned with DHCPv6)

Notes:

In IPv4, IPv6 and port ranges presented in the example the PSID matches to 0x34 and not 0x20:

   PSID:                    0x34
   Available ports (63 ranges): 1232-1235, 2256-2259, ...... ,
                                63696-63699, 64720-64723
   IPv6 address of MAP CE:  2001:db8:0012:3400:0000:c000:0212:0034
```

## Explanation

The original example uses an incorrect PSID value (0x20). The correction provides the correct PSID value (0x34), making the example consistent with the provided IPv6 address and port ranges. This inconsistency would lead to confusion in interpreting the example and implementing the specification correctly.
