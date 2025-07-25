# Errata 4880 - RFC 7574

- **RFC Title:** Peer-to-Peer Streaming Peer Protocol (PPSPP)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid4880](https://www.rfc-editor.org/errata/eid4880)

```
Section 7.5 says:


   A peer MUST include the content integrity method used by a swarm.
   The code for this option is 3.  Defined values are listed in Table 4.

                   +--------+-------------------------+
                   | Method | Description             |
                   +--------+-------------------------+
                   | 0      | No integrity protection |
                   | 1      | Merkle Hash Tree        |
                   | 2      | Sign All                |
                   | 3      | Unified Merkle Tree     |
                   | 4-255  | Unassigned              |
                   +--------+-------------------------+

            Table 4: PPSPP Content Integrity Protection Methods

It should say:

   A peer MUST include the content integrity method used by a swarm.
   The code for this option is 3.  Defined values are listed in Table 4.

                   +--------+-------------------------+
                   | Method | Description             |
                   +--------+-------------------------+
                   | 0      | Unassigned              |
                   | 1      | Merkle Hash Tree        |
                   | 2      | Sign All                |
                   | 3      | Unified Merkle Tree     |
                   | 4-255  | Unassigned              |
                   +--------+-------------------------+

            Table 4: PPSPP Content Integrity Protection Methods

Notes:

As stated in the first sentence of chapter 7.5, “A peer MUST include the content integrity method used by a swarm.”, “No integrity protection” must not be one of the option for PPSPP content integrity protection method. Or, IETF 7574 must define PPSP-PP that does not use the integrity protection method.

The proposed is to remove option of “No integrity protection”  in Table 4.

Spencer: confirmed in conversations with Victor Grishchenko <victor.grishchenko@gmail.com> on the PPSP mailing list.
```

## Explanation

The original text includes "No integrity protection" as a defined content integrity method, while the requirement that a peer MUST include the content integrity method used by a swarm makes this option contradictory.  The correction removes this option, resolving the inconsistency. This inconsistency would lead to implementations allowing for undefined behavior.
