# Errata 7780 - RFC 9114

- **RFC Title:** HTTP/3
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7780](https://www.rfc-editor.org/errata/eid7780)

```
Section 7.2.6 says:


The GOAWAY frame applies to the entire connection,
not a specific stream. A client MUST treat a
GOAWAY frame on a stream other than the control
stream as a connection error of type
H3_FRAME_UNEXPECTED.

It should say:

The GOAWAY frame applies to the entire connection,
not a specific stream. An endpoint MUST treat a
GOAWAY frame on a stream other than the control
stream as a connection error of type
H3_FRAME_UNEXPECTED.

Notes:

HTTP/3 originally only supported GOAWAY from server to client. In this PR we added the ability to also send GOAWAY from client to server https://github.com/quicwg/base-drafts/pull/3129/files. Unfortunately we didn't update the highlighted text to cover the situation where a server receives a GOAWAY on a different stream. 

FWIW the implementation I am responsible for already applies the rule to request streams.
```

## Explanation

The original specification in Section 7.2.6 incorrectly states that only a client MUST treat a GOAWAY frame on a non-control stream as a connection error.  The updated specification correctly states that both client and server endpoints MUST handle this situation, reflecting the change to allow bidirectional GOAWAY frames. This inconsistency affects the implementation of both clients and servers that must correctly handle GOAWAY frames on streams other than the control stream.
