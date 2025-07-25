# Errata 4408 - RFC 7401

- **RFC Title:** Host Identity Protocol Version 2 (HIPv2)
- **RFC Publication Date:** April 2015
- Link to original errata report: [rfc-editor.org/errata/eid4408](https://www.rfc-editor.org/errata/eid4408)

```
Section 4.4.4 says:


     .   +---------+  recv I2, send R2                       |         |
   +---->| I1-SENT |--------------------------------------+  |         |
   |     +---------+            +----------------------+  |  |         |
   |          | recv R2,        | recv I2, send R2     |  |  |         |
   |          v send I2         |                      v  v  v         |
   |       +---------+          |                    +---------+       |
   |  +--->| I2-SENT |----------+     +--------------| R2-SENT |<---+  |
   |  |    +---------+                |              +---------+    |  |

It should say:

     .   +---------+  recv I2, send R2                       |         |
   +---->| I1-SENT |--------------------------------------+  |         |
   |     +---------+            +----------------------+  |  |         |
   |          | recv R1,        | recv I2, send R2     |  |  |         |
   |          v send I2         |                      v  v  v         |
   |       +---------+          |                    +---------+       |
   |  +--->| I2-SENT |----------+     +--------------| R2-SENT |<---+  |
   |  |    +---------+                |              +---------+    |  |

Notes:

This state machine figure is informative.  Normative (correct) specification for the I1-SENT to I2-SENT state transition (due to recv R1 event) is in Section 6.8.
```

## Explanation

The errata corrects a state machine diagram, showing an incorrect transition from I1-SENT to I2-SENT.  The original diagram incorrectly shows a transition upon reception of R2, while the correct behavior is a transition upon reception of R1 (as specified in Section 6.8). This inconsistency affects the understanding and implementation of the HIPv2 state machine.
