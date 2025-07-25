# Errata 7148 - RFC 9260

- **RFC Title:** Stream Control Transmission Protocol
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7148](https://www.rfc-editor.org/errata/eid7148)

```
Section 3.3.3 says:


A receiver of an INIT ACK chunk with the a_rwnd value set to a
value smaller than 1500 MUST discard the packet, SHOULD send a
packet in response containing an ABORT chunk and using the
Initiate Tag as the Verification Tag, and MUST NOT change the
state of any existing association.


It should say:

If an endpoint in the COOKIE-WAIT state receives an INIT ACK chunk
with the a_rwnd value set to a value smaller than 1500, it MUST
destroy the TCB and SHOULD send an ABORT chunk.  If such an
INIT ACK chunk is received in any state other than CLOSED or
COOKIE-WAIT, it SHOULD be discarded silently (see Section 5.2.3).


Notes:

The handling of a_rwnd < 1500 should be similar to the handling of OS = 0 or MIS = 0.
```

## Explanation

The original specification for handling an INIT ACK chunk with a_rwnd less than 1500 is inconsistent with the handling of other error conditions.  The correction aligns the handling with other error conditions, ensuring consistent behavior across different scenarios.
