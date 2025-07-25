# Errata 4724 - RFC 7574

- **RFC Title:** Peer-to-Peer Streaming Peer Protocol (PPSPP)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid4724](https://www.rfc-editor.org/errata/eid4724)

```
Section 1.3 says:


swarm ID
Unique identifier for a swarm of peers, in PPSPP a sequence of
bytes. For video on demand with content integrity protection
enabled, the identifier is the so-called root hash of a Merkle
hash tree over the content. For live streaming, the swarm ID is
a public key.

It should say:

swarm ID
Unique identifier for a swarm of peers, in PPSPP a sequence of
bytes. For video on demand, the identifier is the so-called root hash
of a Merkle hash tree over the content. For live streaming, the 
swarm ID is a public key.

Notes:

According to chapter 5 and chapter 6.1, it seems that it is not mandatory to use content integrity protection scheme.
The definition of swarm ID in the original text does not define how the ID is used in environment with the content integrity protection disabled.
It is possible to add new description on how swarm ID is defined in the content integrity protection scheme is disabled. 
Or, it is possible to remove the parts regarding content integrity protection.

We propose to remove "with content integrity protection enabled" part.

Spencer: confirmed in conversations with Victor Grishchenko <victor.grishchenko@gmail.com> on the PPSP mailing list.
```

## Explanation

The original description of swarm ID is inconsistent with the specification in chapters 5 and 6.1, which do not mandate content integrity protection.  The original text implies that the swarm ID is only defined when content integrity protection is enabled, while it should be defined regardless. The corrected description removes the reference to content integrity protection, addressing this inconsistency.
