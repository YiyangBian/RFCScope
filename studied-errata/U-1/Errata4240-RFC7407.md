# Errata 4240 - RFC 7407

- **RFC Title:** A YANG Data Model for SNMP Configuration
- **RFC Publication Date:** December 2014
- Link to original errata report: [rfc-editor.org/errata/eid4240](https://www.rfc-editor.org/errata/eid4240)

```
Section 4.8 says:


     augment /snmp:snmp/snmp:target {
       when "snmp:v1 or snmp:v2c";

It should say:

     augment /snmp:snmp/snmp:target {

Notes:

The nodes refered to in the "when" expression do not exist.
(They were there in an early draft version, but when they were moved, we forgot to fix the "when" expression).
```

## Explanation

The original text includes a "when" expression that refers to non-existent nodes. This inconsistency makes the augment statement invalid and will lead to incorrect configuration processing. The correction removes the invalid "when" expression, fixing the inconsistency.
