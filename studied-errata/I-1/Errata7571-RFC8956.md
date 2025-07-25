# Errata 7571 - RFC 8956

- **RFC Title:** Dissemination of Flow Specification Rules for IPv6
- **RFC Publication Date:** December 2020
- Link to original errata report: [rfc-editor.org/errata/eid7571](https://www.rfc-editor.org/errata/eid7571)

```
Section 3.8.1 says:


+======+======================+=========================+==========+
| len  | destination          | source                  | ul-proto |
+======+======================+=========================+==========+
| 0x12 | 01 20 00 20 01 0d bb | 02 68 40 12 34 56 78 9a | 03 81 06 |
+------+----------------------+-------------------------+----------+
                                 Table 1

It should say:

+======+======================+=========================+==========+
| len  | destination          | source                  | ul-proto |
+======+======================+=========================+==========+
| 0x12 | 01 20 00 20 01 0d b8 | 02 68 40 12 34 56 78 9a | 03 81 06 |
+------+----------------------+-------------------------+----------+
                                 Table 1

Notes:

The last byte in the "destination" column of Table 1 in 3.8.1 should be "b8", not "bb".
```

## Explanation

The example in Table 1 contains an incorrect byte value ("bb" instead of "b8") in the destination field, creating an inconsistency between the example and the correct representation.
