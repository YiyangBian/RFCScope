# Errata 4726 - RFC 7574

- **RFC Title:** Peer-to-Peer Streaming Peer Protocol (PPSPP)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid4726](https://www.rfc-editor.org/errata/eid4726)

```
Section 6.1 says:


In the "Unified Merkle Tree" method, PPSPP combines the Merkle Hash
Tree scheme for static content with signatures to unify the video-on-
demand and live streaming scenarios. The use of Merkle hash trees
reduces the number of signing and verification operations, hence
providing a similar signature amortization to the approach described
in [SIGMCAST]. If PPSPP operates over the Internet, the "Unified
Merkle Tree" method MUST be used. If the protocol operates in a
benign environment, the "Unified Merkle Tree" method MAY be used. So
this method is mandatory to implement.

It should say:

In the "Unified Merkle Tree" method, PPSPP combines the Merkle Hash
Tree scheme for static content with signatures to unify the video-on-
demand and live streaming scenarios. The use of Merkle hash trees
reduces the number of signing and verification operations, hence
providing a similar signature amortization to the approach described
in [SIGMCAST].

Notes:

RFC 7574 (PPSP-PP) defines how the peers exchange chunks regarding content integrity protection scheme. It describes the relationship of the DATA and INTEGRITY messages.
But, it does not describes how peers exchange chunks when the content integrity protection scheme is disabled.
Thus, to the readers, it seems that content integrity protection scheme is very important part of PPSP-PP and must be used in order to implement PPSP-PP.
I think the RFC 7574 (PPSP-PP) should be changed to clearly express that the content integrity protection scheme must be used in PPSP-PP.
The proposed changes is to remove options regarding the use of content integrity protection.

Spencer: confirmed in conversations with Victor Grishchenko <victor.grishchenko@gmail.com> on the PPSP mailing list.
```

## Explanation

The RFC does not mention what has to be done in cases other than the two cases mentioned. The clarification states that there is no other case by mandating the scheme.
