# Errata 7539 - RFC 9002

- **RFC Title:** QUIC Loss Detection and Congestion Control
- **RFC Publication Date:** May 2021
- Link to original errata report: [rfc-editor.org/errata/eid7539](https://www.rfc-editor.org/errata/eid7539)

```
Section 5. says:


smoothed_rtt = 7/8 * smoothed_rtt + 1/8 * adjusted_rtt
rttvar_sample = abs(smoothed_rtt - adjusted_rtt)
rttvar = 3/4 * rttvar + 1/4 * rttvar_sample


It should say:

rttvar_sample = abs(smoothed_rtt - adjusted_rtt)
rttvar = 3/4 * rttvar + 1/4 * rttvar_sample
smoothed_rtt = 7/8 * smoothed_rtt + 1/8 * adjusted_rtt


Notes:

Per Appendix A.7 of this RFC and Section 2 of the referred RFC 6298,
rttvar should be computed before updating smoothed_rtt itself.
```

## Explanation

The original order of calculations for smoothed_rtt and rttvar is incorrect. The correction places the calculation of rttvar before the update of smoothed_rtt, which is consistent with RFC 6298. This inconsistency would result in incorrect RTT and RTT variance calculations.
