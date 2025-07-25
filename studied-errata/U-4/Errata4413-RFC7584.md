# Errata 4413 - RFC 7584

- **RFC Title:** Session Traversal Utilities for NAT (STUN) Message Handling for SIP Back-to-Back User Agents (B2BUAs)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid4413](https://www.rfc-editor.org/errata/eid4413)

```
Section 4.4 says:


   Because of forking, a B2BUA might receive multiple answers for a
   single outbound INVITE.  When this occurs, the B2BUA SHOULD follow
   Sections 3.2 or 3.3 for all of those received answers.

It should say:

   Because of forking, a B2BUA might receive multiple answers for a
   single outbound INVITE.  When this occurs, the B2BUA SHOULD follow
   Sections 4.2 or 4.3 for all of those received answers.

Notes:

Sections 3.2 and 3.3 do not exist.  The normative statement should indicate sections 4.2 and 4.3.
```

## Explanation

The original text refers to non-existent sections (3.2 and 3.3) for handling multiple INVITE answers. The correction points to the correct sections (4.2 and 4.3), resolving the inconsistency. This inconsistency would mislead implementations attempting to correctly handle multiple INVITE answers.
