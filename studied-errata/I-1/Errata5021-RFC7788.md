# Errata 5021 - RFC 7788

- **RFC Title:** Home Networking Control Protocol
- **RFC Publication Date:** April 2016
- Link to original errata report: [rfc-editor.org/errata/eid5021](https://www.rfc-editor.org/errata/eid5021)

```
RFC 7787 (DNCP) in section 9 defines DNCP_NODE_IDENTIFIER_LENGTH as being bytes, not bits.

-- Verifier note --
Indeed, section 9 of RFC 7787 clearly specifies "DNCP_NODE_IDENTIFIER_LENGTH: The fixed length of a node identifier (in bytes)."
```

## Explanation

RFC 7788 incorrectly describes DNCP_NODE_IDENTIFIER_LENGTH as bits when RFC 7787 defines it as bytes. This inconsistency creates a conflict between the two specifications, leading to potential incompatibility between implementations.
