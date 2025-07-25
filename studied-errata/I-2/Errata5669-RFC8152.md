# Errata 5669 - RFC 8152

- **RFC Title:** CBOR Object Signing and Encryption (COSE)
- **RFC Publication Date:** July 2017
- Link to original errata report: [rfc-editor.org/errata/eid5669](https://www.rfc-editor.org/errata/eid5669)

```
Section 16.7 says:


Value:  This is the value used to identify the curve.  These values
   MUST be unique.  The value can be a positive integer, a negative
   integer, or a string.

Description:  This field contains a brief description of the curve.

References:  This contains a pointer to the public specification for
   the curve if one exists.

It should say:

Value:  This is the value used to identify the key type.  These values
   MUST be unique.  The values are positive integers.

Description:  This field contains a brief description of the key type.

References:  This contains a pointer to the public specification for
   the key type if one exists.

Notes:

This Registry is about Key Types, but the current text refers to curves.

The value identifying a key type can be only a positive integer.
```

## Explanation

The original description of the registry entries incorrectly refers to curves when the registry is for key types. The corrected description specifies that the values identify key types, using positive integers and providing descriptions and references accordingly. This inconsistency affects the interpretation and use of the key type registry.
