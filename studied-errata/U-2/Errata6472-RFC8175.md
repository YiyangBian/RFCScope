# Errata 6472 - RFC 8175

- **RFC Title:** Dynamic Link Exchange Protocol (DLEP)
- **RFC Publication Date:** June 2017
- Link to original errata report: [rfc-editor.org/errata/eid6472](https://www.rfc-editor.org/errata/eid6472)

```
Section 12.4, para 2 says:


A Peer Offer Signal MUST be encoded within a UDP packet.  The IP source and destination fields in the packet MUST be set by swapping the values received in the Peer Discovery Signal.  The Peer Offer Signal completes the discovery process; see Section 7.1.

It should say:

A Peer Offer Signal MUST be encoded within a UDP packet. The IP source and destination fields (addresses and ports) in the packet MUST be set by swapping the values received in the Peer Discovery Signal, with the exception that the new source address on the Offer Signal, which was the well-known destination address, becomes a local IP from the DLEP modem. The source port remains the well-known port from the Peer Discovery Signal. The Peer Offer signal contains zero or more connection points as described in 13.2 and 13.3 completes the discovery process; see Section 7.1 

Notes:

The original text will not result in a valid unicast IP packet.

=====
AD Note:  The original text is clearly wrong.  There has been discussion in the WG about the proper wording for the "corrected text".  Given that the current text results in an invalid packet, I am marking this report as Verified.

https://mailarchive.ietf.org/arch/msg/manet/h8Sa924gn6ZmAZ7XNp-5UUrZlAY/
```

## Explanation

The original text describes swapping IP source and destination addresses without specifying how to handle the source address in the Peer Offer Signal, resulting in an invalid packet. The correction clarifies that the source address should be set to a local IP address from the DLEP modem instead of simply swapping with the destination address, resolving the inconsistency.
