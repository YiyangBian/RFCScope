# Errata 6654 - RFC 7401

- **RFC Title:** Host Identity Protocol Version 2 (HIPv2)
- **RFC Publication Date:** April 2015
- Link to original errata report: [rfc-editor.org/errata/eid6654](https://www.rfc-editor.org/errata/eid6654)

```
Section 5.3.3 says:


   If present in the I1 packet, the Initiator MUST include an unmodified
   copy of the R1_COUNTER parameter received in the corresponding R1
   packet into the I2 packet.


It should say:

   If present in the R1 packet, the Initiator MUST include an unmodified
   copy of the R1_COUNTER parameter received in the corresponding R1
   packet into the I2 packet.


Notes:

Packet name error, must be R1
```

## Explanation

The errata corrects a statement about the source of the R1_COUNTER parameter. The original text incorrectly stated that the parameter must be included in the I2 packet if it was present in the I1 packet. The correct source for the R1_COUNTER parameter is the R1 packet. This inconsistency affects the implementation of the HIPv2 protocol.
