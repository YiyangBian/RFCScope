# Errata 7654 - RFC 8955

- **RFC Title:** Dissemination of Flow Specification Rules
- **RFC Publication Date:** December 2020
- Link to original errata report: [rfc-editor.org/errata/eid7654](https://www.rfc-editor.org/errata/eid7654)

```
Section 4 says:


   This NLRI information is encoded using MP_REACH_NLRI and
   MP_UNREACH_NLRI attributes, as defined in [RFC4760].  When
   advertising Flow Specifications, the Length of the Next-Hop Network
   Address MUST be set to 0.  The Network Address of the Next-Hop field
   MUST be ignored.


It should say:

   This NLRI information is encoded using MP_REACH_NLRI and
   MP_UNREACH_NLRI attributes, as defined in [RFC4760].  When
   advertising Flow Specifications, the "Length of Next Hop Network 
   Address" field MUST be set to 0.  The "Network Address of Next Hop" 
   field MUST be ignored.

Notes:

The fields are named incorrectly in the original text -- they don't match the field names they're referencing in RFC 4760. Most importantly there's no hyphen in the RFC 4760 field definitions, but there are other differences too.
```

## Explanation

The original text uses incorrect field names for the Next Hop Network Address attributes.  The correction uses the correct field names from RFC 4760, resolving the inconsistency.  This inconsistency could lead to implementations incorrectly handling the Next Hop Network Address attributes when advertising Flow Specifications.
