# Errata 5845 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5845](https://www.rfc-editor.org/errata/eid5845)

```
Section 3.3.1 says:


   EAP method messages are carried within EAP-Payload TLVs defined in
   Section 4.2.10.  If more than one method is going to be executed in
   the tunnel, then upon method completion, the server MUST send an
   Intermediate-Result TLV indicating the result.


It should say:

   EAP method messages are carried within EAP-Payload TLVs defined in
   Section 4.2.10.  Upon method completion, the server MUST send an
   Intermediate-Result TLV indicating the result.


Notes:

Description of whether Intermediate-Result TLV is supposed to be used in the case where only a single inner EAP authentication method is used. Section 3.3.1 says "more than one method is going to be executed in the tunnel, then upon method completion, the server MUST send an Intermediate-Result TLV indicating the result", Section 3.3.3 says "The Crypto-Binding TLV and Intermediate-Result TLV MUST be included to perform cryptographic binding after each successful EAP method in a sequence of one or more EAP methods", 4.2.13 says "It MUST be included with the Intermediate-Result TLV to perform cryptographic binding after each successful EAP method in a sequence of EAP methods", Annex C.3 shows an example exchange with a single inner EAP authentication method with use of Intermediate-Result TLV.

It looks like the majority of the places discussion this topic implies that there is going to be an Intermediate-Result TLV after each inner EAP authentication method and the text in 3.3.1 is the only clear case of conflicting (or well, at least misleading if one were to claim it does not explicitly say MUST NOT for the one inner EAP authentication method case). As such, I'd conclude the Intermediate-Result TLV is indeed going to be exchanged after each EAP authentication method and the proposed text change to 3.3.1 covers that.
```

## Explanation

The errata clarifies the use of Intermediate-Result TLVs. The original text in section 3.3.1 implied that Intermediate-Result TLVs are only required when multiple EAP methods are used. However, other sections and examples suggest that these TLVs are required after each EAP method, regardless of the number of methods. This inconsistency is corrected by removing the condition of 'more than one method' from section 3.3.1, making the requirement consistent across the specification.
