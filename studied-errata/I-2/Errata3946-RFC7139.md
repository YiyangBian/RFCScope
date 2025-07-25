# Errata 3946 - RFC 7139

- **RFC Title:** GMPLS Signaling Extensions for Control of Evolving G.709 Optical Transport Networks
- **RFC Publication Date:** March 2014
- Link to original errata report: [rfc-editor.org/errata/eid3946](https://www.rfc-editor.org/errata/eid3946)

```
Section 7 says:


After decreasing the bandwidth, the ingress node
SHOULD send a ResvErr message to tear down the old control state.

It should say:

After decreasing the bandwidth, the ingress node
SHOULD send a PathTear message to tear down the old control state.

Notes:

PathTear is the usual mechanism to teardown old control state. This is would also make the bandwidth decreasing procedure consistent with the bandwidth increasing procedure (bandwidth increasing procedure uses PathTear to teardown old control state.)

This change looks like a change of substance, but the authors confirm that their intent was to use the same process for both the increase and decrease in bandwidth.
```

## Explanation

The erratum corrects the message type used to tear down the old control state after decreasing bandwidth. The original text suggests using a ResvErr message, while the correction specifies PathTear.  This inconsistency creates ambiguity in implementation, as ResvErr and PathTear have different meanings and functions within the protocol. Maintaining consistency between the bandwidth increase and decrease procedures is crucial for correct implementation.
