# Errata 5622 - RFC 8306

- **RFC Title:** Extensions to the Path Computation Element Communication Protocol (PCEP) for Point-to-Multipoint Traffic Engineering Label Switched Paths
- **RFC Publication Date:** November 2017
- Link to original errata report: [rfc-editor.org/errata/eid5622](https://www.rfc-editor.org/errata/eid5622)

```
Section 3.13 says:


   The total PCEP message length, including the common header, is
   16 bytes.

It should say:

   The total PCEP message length, including the common header, is
   (2^16)-1 bytes.

Notes:

The message length field is 16 bits, so the maximum message length is (2^16)-1.
```

## Explanation

The original text incorrectly states a fixed message length of 16 bytes, while the message length field is actually 16 bits, allowing for a much larger maximum length.  This inconsistency would lead to implementations incorrectly limiting the maximum PCEP message size. For reference, check Section 6.1 of RFC5440.
