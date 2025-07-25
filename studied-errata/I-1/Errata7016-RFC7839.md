# Errata 7016 - RFC 7839

- **RFC Title:** Access-Network-Identifier Option in DHCP
- **RFC Publication Date:** June 2016
- Link to original errata report: [rfc-editor.org/errata/eid7016](https://www.rfc-editor.org/errata/eid7016)

```
Section 4.4.1 says:


   Length
      4

   Operator-Identifier
      The Operator-Identifier is a variable-length Private Enterprise
      Number (PEN) ...

It should say:

   Length
      4

   Operator-Identifier
      The Operator-Identifier is a 32-bit Private Enterprise
      Number (PEN) ...

Notes:

Either the length is 4, and the contents are 32-bits.  Or the length is >1, and the length is variable.

My guess is that the intention is to have a fixed length.  The variable-length encoding from RFC 6757 is likely not needed here.


*** verifier note ***
See Bernie Volz's reply in https://mailarchive.ietf.org/arch/msg/dhcwg/Y4yaYwaqxS0B2nWw5f4xER2fSMk/
```

## Explanation

The description of the Operator-Identifier field is inconsistent. The length is specified as 4 bytes, while the description indicates that it is a variable-length PEN. This inconsistency should be resolved by either changing the length description to reflect that the PEN is encoded as 32 bits or by changing the description to indicate a variable length.
