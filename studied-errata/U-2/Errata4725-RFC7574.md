# Errata 4725 - RFC 7574

- **RFC Title:** Peer-to-Peer Streaming Peer Protocol (PPSPP)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid4725](https://www.rfc-editor.org/errata/eid4725)

```
Section 5 says:


PPSPP can use different methods for protecting the integrity of the
content while it is being distributed via the peer-to-peer network.
More specifically, PPSPP can use different methods for receiving
peers to detect whether a requested chunk has been maliciously
modified by the sending peer. In benign environments, content
integrity protection can be disabled.

For static content, PPSPP currently defines one method for protecting
integrity, called the Merkle Hash Tree scheme. If PPSPP operates
over the Internet, this scheme MUST be used. If PPSPP operates in a
benign environment, this scheme MAY be used. So the scheme is
mandatory to implement, to satisfy the requirement of strong security
for an IETF protocol [RFC3365]. An extended version of the scheme is
used to efficiently protect dynamically generated content (live
streams), as explained below and in Section 6.1.

It should say:

PPSPP can use different methods for protecting the integrity of the
content while it is being distributed via the peer-to-peer network.
More specifically, PPSPP can use different methods for receiving
peers to detect whether a requested chunk has been maliciously
modified by the sending peer.

For static content, PPSPP currently defines one method for protecting
integrity, called the Merkle Hash Tree scheme.
The scheme is mandatory to implement, to satisfy the requirement of 
strong security for an IETF protocol [RFC3365]. An extended version
of the scheme is used to efficiently protect dynamically generated
content (live streams), as explained below and in Section 6.1.

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
