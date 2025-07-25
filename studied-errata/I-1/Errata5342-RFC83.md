# Errata 5342 - RFC 83

- **RFC Title:** Protocol Independent Multicast - Sparse Mode (PIM-SM): Protocol Specification (Revised)
- **RFC Publication Date:** March 2016
- Link to original errata report: [rfc-editor.org/errata/eid5342](https://www.rfc-editor.org/errata/eid5342)

```
Section 4.4.2 says:


set KeepaliveTimer(S,G) to RP_Keepalive_Period;

It should say:

set KeepaliveTimer(S,G) to max(Keepalive_Period, RP_Keepalive_Period);

Notes:

The normal keepalive period for the KAT(S,G) defaults to 210 seconds. However, at the RP, the keepalive period must be at least the Register_Suppression_Time, or the RP may time out the (S,G) state before the next Null-Register arrives. Thus, the KAT(S,G) is set to max(Keepalive_Period, RP_Keepalive_Period) when a Register-Stop is sent.

====
Note that the text above comes from §4.11.
```

## Explanation

The original specification sets the KeepaliveTimer to RP_Keepalive_Period, which may be shorter than the actual keepalive period. This inconsistency can lead to premature timeouts. The corrected specification uses the maximum of Keepalive_Period and RP_Keepalive_Period, ensuring that the timer is long enough to avoid premature timeouts.
