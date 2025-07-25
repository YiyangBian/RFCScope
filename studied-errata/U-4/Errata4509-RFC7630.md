# Errata 4509 - RFC 7630

- **RFC Title:** HMAC-SHA-2 Authentication Protocols in the User-based Security Model (USM) for SNMPv3
- **RFC Publication Date:** October 2015
- Link to original errata report: [rfc-editor.org/errata/eid4509](https://www.rfc-editor.org/errata/eid4509)

```
Section 8 and 10 says:


snmpModules 235

It should say:

mib-2 235

Notes:

IANA registered snmpUsmHmacSha2MIB under mib-2.235 (as advised by the MIB doctors), but the document mentions snmpModules.235
```

## Explanation

The original text uses the incorrect module name `snmpModules` when referring to the IANA-registered MIB. The correct module name should be `mib-2`, reflecting the actual location of the MIB in the IANA registry. This inconsistency between the text and the actual MIB location could lead to incorrect implementation.
