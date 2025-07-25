# Errata 5844 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5844](https://www.rfc-editor.org/errata/eid5844)

```
Section C.1 says:


                            <- Crypto-Binding TLV (Request),
                                Result TLV (Success),
                                (Optional PAC TLV)

       Crypto-Binding TLV(Response),
       Result TLV (Success),
       (PAC-Acknowledgement TLV) ->


It should say:

                            <- Intermediate-Result-TLV (Success),
                                Crypto-Binding TLV (Request),
                                Result TLV (Success),
                                (Optional PAC TLV)

       Intermediate-Result-TLV (Success),
       Crypto-Binding TLV(Response),
       Result TLV (Success),
       (PAC-Acknowledgement TLV) ->


Notes:

Section 3.3.2 implies that Intermediate-Result TLV is used after each round of Basic-Password-Auth-Req/Resp TLVs. However, the example sequence in C.1 does not show this. The proposed change in this errata adds the Intermediate-Result TLV indication here. Similar change should be done in C.2 (i.e., add Intermediate-Result TLV (Failure) to the messages that include Result TLV) since the language in 3.3.2 describe the indication to be used for both success and failure cases.

In addition to this change in C.1, it would be good to clarify the specification globally to avoid confusion about this case since almost all discussion regarding Intermediate-Result TLV currently is in the context of inner EAP authentication. 3.3.2 should have a MUST statement similar to 3.3.1. 3.6 should cover success or failure indications of basic password auth like it does EAP methods. 4.2.11 should note Intermediate-Result TLV is used with both inner EAP and basic password auth. 4.2.13 should mention basic password auth in the "regardless of whether there is an inner EAP method authentication or not" sentence.
```

## Explanation

The errata report points out that the example message sequence in Section C.1 does not include the Intermediate-Result TLV, which is implied to be used in Section 3.3.2.  This omission creates an inconsistency between the example and the specification.  This inconsistency affects implementations that follow the example sequence literally but must also follow section 3.3.2. The errata proposes to add the missing TLV to correct this inconsistency, which is required to ensure correct implementation.
