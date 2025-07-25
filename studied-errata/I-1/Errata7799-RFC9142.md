# Errata 7799 - RFC 9142

- **RFC Title:** Key Exchange (KEX) Method Updates and Recommendations for Secure Shell (SSH)
- **RFC Publication Date:** January 2022
- Link to original errata report: [rfc-editor.org/errata/eid7799](https://www.rfc-editor.org/errata/eid7799)

```
Section 1.2.1 says:


+============+=============================+
| Curve Name | Estimated Security Strength |
+============+=============================+
| nistp256   | 128 bits                    |
+------------+-----------------------------+
| nistp384   | 192 bits                    |
+------------+-----------------------------+
| nistp521   | 512 bits                    |
+------------+-----------------------------+
| curve25519 | 128 bits                    |
+------------+-----------------------------+
| curve448   | 224 bits                    |
+------------+-----------------------------+

It should say:

+============+=============================+
| Curve Name | Estimated Security Strength |
+============+=============================+
| nistp256   | 128 bits                    |
+------------+-----------------------------+
| nistp384   | 192 bits                    |
+------------+-----------------------------+
| nistp521   | 256 bits                    |
+------------+-----------------------------+
| curve25519 | 128 bits                    |
+------------+-----------------------------+
| curve448   | 224 bits                    |
+------------+-----------------------------+

Notes:

P-521 has approximately 256 bits of security (rather than 512), as per Table 1 of Section 6.1.1 of FIPS 186-5, and Section 9 Paragraph 5 of RFC 5656.
```

## Explanation

The estimated security strength for nistp521 is incorrectly listed as 512 bits. The correct value is 256 bits, creating an inconsistency with other references that specify the correct security strength.
