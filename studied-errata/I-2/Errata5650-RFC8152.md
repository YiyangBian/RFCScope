# Errata 5650 - RFC 8152

- **RFC Title:** CBOR Object Signing and Encryption (COSE)
- **RFC Publication Date:** July 2017
- Link to original errata report: [rfc-editor.org/errata/eid5650](https://www.rfc-editor.org/errata/eid5650)

```
Section Section 13.2 says:


   | crv  | 1     | -1    | int /  | EC identifier - Taken from the    |
   |      |       |       | tstr   | "COSE Key Common Parameters"      |
   |      |       |       |        | registry                          |

It should say:

   | crv  | 1     | -1    | int /  | EC identifier - Taken from the    |
   |      |       |       | tstr   | "COSE Elliptic Curves" registry   |

Notes:

The set of curve identifiers lives in the COSE Elliptic Curves registry and not in the COSE Key Common Parameters registry.
```

## Explanation

The original text points to the wrong registry for EC identifiers. The correct registry is the "COSE Elliptic Curves" registry, not the "COSE Key Common Parameters" registry. This inconsistency could lead to incorrect interpretation and implementation.
