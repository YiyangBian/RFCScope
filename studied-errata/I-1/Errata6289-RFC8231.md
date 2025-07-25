# Errata 6289 - RFC 8231

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Extensions for Stateful PCE
- **RFC Publication Date:** September 2017
- Link to original errata report: [rfc-editor.org/errata/eid6289](https://www.rfc-editor.org/errata/eid6289)

```
Section 7.3.2 says:


   Length (16 bits): indicates the total length of the TLV in octets and
   MUST be greater than 0.  The TLV MUST be zero-padded so that the TLV
   is 4-octet aligned.

It should say:

   Length (16 bits): indicates the length of the value portion of the 
   TLV in octets and MUST be greater than 0.  The TLV MUST be zero-
   padded so that the TLV is 4-octet aligned.


Notes:

The "total length of the TLV" is incorrect, as in PCEP the TLV formatting is as per RFC 5440 which requires the length to be of the value portion only. The other text such as "MUST be greater than 0", the padding rules along with "without a NULL terminator" also point to the fact that the intention of the authors/WG was not "total" (and it is simply a mistake).
```

## Explanation

The original text defines the Length field as the total length of the TLV, including the type and length fields.  This is inconsistent with RFC 5440, which specifies that the length field represents only the length of the value portion of the TLV. The correction clarifies that the length field represents the length of the value portion only, resolving the inconsistency.
