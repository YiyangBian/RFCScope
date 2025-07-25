# Errata 8134 - RFC 9656

- **RFC Title:** A YANG Data Model for Microwave Topology
- **RFC Publication Date:** September 2024
- Link to original errata report: [rfc-editor.org/errata/eid8134](https://www.rfc-editor.org/errata/eid8134)

```
Section B.2 says:


            "node-id": "mw-N1",

It should say:

            "node-id": "example:mw-N1",

Notes:

Fixed URI name to follow RFC8407bis guidelines.

See also https://mailarchive.ietf.org/arch/msg/ccamp/OQ-oLx2smsmdC4dcn6aB9i-hWE8/
```

## Explanation

The original example omits prefixes for network and node identifiers, which is inconsistent with the data model. The correction adds the prefixes, resolving the inconsistency.
