# Errata 8104 - RFC 7684

- **RFC Title:** OSPFv2 Prefix/Link Attribute Advertisement
- **RFC Publication Date:** November 2015
- Link to original errata report: [rfc-editor.org/errata/eid8104](https://www.rfc-editor.org/errata/eid8104)

```
Section 2.1 says:


   Route Type
      The type of the OSPFv2 route.  If the route type is 0
      (Unspecified), the information inside the OSPFv2 External Prefix
      TLV applies to the prefix regardless of prefix's route type.  This
      is useful when prefix-specific attributes are advertised by an
      external entity that is not aware of the route type associated
      with the prefix.  Supported types are:

It should say:

   Route Type
      The type of the OSPFv2 route.  If the route type is 0
      (Unspecified), the information inside the OSPFv2 Extended Prefix
      TLV applies to the prefix regardless of prefix's route type.  This
      is useful when prefix-specific attributes are advertised by an
      external entity that is not aware of the route type associated
      with the prefix.  Supported types are:

Notes:

s/External Prefix/Extended Prefix/
```

## Explanation

The original text incorrectly refers to "OSPFv2 External Prefix TLV", while the correct term is "OSPFv2 Extended Prefix TLV". This inconsistency creates a mismatch between the description and the actual TLV used, affecting the correct interpretation and implementation of the specification.
