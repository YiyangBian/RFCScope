# Errata 6609 - RFC 8684

- **RFC Title:** TCP Extensions for Multipath Operation with Multiple Addresses
- **RFC Publication Date:** March 2020
- Link to original errata report: [rfc-editor.org/errata/eid6609](https://www.rfc-editor.org/errata/eid6609)

```
Section B.3 says:


   initiator                                                    listener
       |                                                           |
       |    S  0(20) <MP_CAPABLE>, <TFO cookie>                    |
       | --------------------------------------------------------> |
       |                                                           |
       |    S. 0(0) ack 21 <MP_CAPABLE>                            |
       | <-------------------------------------------------------- |
       |                                                           |
       |    .  1(100) ack 21 <DSS ack=1 seq=1 ssn=1 dlen=100>      |
       | <-------------------------------------------------------- |
       |                                                           |
       |    .  21(0) ack 1 <MP_CAPABLE>                            |
       | --------------------------------------------------------> |
       |                                                           |
       |    .  21(20) ack 101 <DSS ack=101 seq=1 ssn=1 dlen=20>    |
       | --------------------------------------------------------> |
       |                                                           |

                    Figure 19: The Listener Supports TFO

It should say:

initiator                                                    listener
       |                                                           |
       |    S  0(20) <MP_CAPABLE>, <TFO cookie>                    |
       | --------------------------------------------------------> |
       |                                                           |
       |    S. 0(0) ack 21 <MP_CAPABLE>                            |
       | <-------------------------------------------------------- |
       |                                                           |
       |    .  1(100) ack 21 <DSS seq=1 ssn=1 dlen=100, M=1, A=0>  |
       | <-------------------------------------------------------- |
       |                                                           |
       |    .  21(0) ack 1 <MP_CAPABLE>                            |
       | --------------------------------------------------------> |
       |                                                           |
       |    .  21(20) ack 101 <DSS ack=101 seq=1 ssn=1 dlen=20>    |
       | --------------------------------------------------------> |
       |                                                           |

                    Figure 19: The Listener Supports TFO

Notes:

The example for TCP Fastopen with MPTCPv1 in RFC8684, Appendix-B.3 shows the listener sending an incorrect data-ack in its first data packet to the initiator sent immediately after its SYN-ACK.
At this point, the listener has not received the initiator's key, so it cannot generate the data-ack in it's response packets.
The correct behaviour would be to set flag 'A' to 0 and exclude sending data-ack until the initiator's key is received.
```

## Explanation

The example in Figure 19 shows the listener sending a DSS packet with the ack field set to 1, which is incorrect because the initiator's key is not yet received. The correction sets the A flag to 0 and removes the data-ack until the key is received, resolving the inconsistency.
