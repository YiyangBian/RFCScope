# Errata 7145 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid7145](https://www.rfc-editor.org/errata/eid7145)

```
Section 3.3.3 says:


   The Crypto-Binding TLV MUST be exchanged and verified
   before the final Result TLV exchange, regardless of whether or not
   there is an inner EAP method authentication.

It should say:

   Except as noted below, the Crypto-Binding TLV MUST be exchanged and verified
   before the final Result TLV exchange, regardless of whether or not
   there is an inner EAP method authentication

Notes:

The text contradicts itself in the same paragraph, because it goes on to say:

   The server may send the final Result TLV along with an
   Intermediate-Result TLV and a Crypto-Binding TLV to indicate its
   intention to end the conversation.  If the peer requires nothing more
   from the server, it will respond with a Result TLV indicating success
   accompanied by a Crypto-Binding TLV and Intermediate-Result TLV if
   necessary.

So there are actually several legal combinations here:

1. Server and peer perform a crypto-binding exchange in anticipation of later sending Result TLVs
2. The server and peer combine their crypto-binding and Result TLV in the same message.
3. One side initiates a crypto-binding TLV and the OTHER responds with both crypto-binding and Result TLV.

The practice seems to be to include the crypto-binding TLVs alongside Result TLVs.
```

## Explanation

The errata highlights a contradiction within Section 3.3.3.  The initial statement mandates a Crypto-Binding TLV exchange before the final Result TLV, regardless of inner EAP method authentication. However, a subsequent sentence describes scenarios where this order is not followed (Result and Crypto-Binding TLVs sent together). This inconsistency creates ambiguity in the specification, impacting implementation.  The proposed addition of 'Except as noted below' resolves this conflict, improving consistency and clarity for implementers.
