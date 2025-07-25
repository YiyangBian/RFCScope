# Errata 6842 - RFC 8561

- **RFC Title:** A YANG Data Model for Microwave Radio Link
- **RFC Publication Date:** June 2019
- Link to original errata report: [rfc-editor.org/errata/eid6842](https://www.rfc-editor.org/errata/eid6842)

```
Section Annex A.3 says:


 "name": "RLT-A:CT-2",
...
           "tx-frequency": 10618000,


It should say:

 "name": "RLT-A:CT-2",
...
           "tx-frequency": 10728000,


Notes:

A.3 describes the XPIC configuration. The tx-frequency for the two CTs under XPIC configuration should be the same, both should be 10728000.

This should be a copy&paste error from A.2 2+0 configuration.

See also the ccamp mailing list: https://mailarchive.ietf.org/arch/msg/ccamp/_VITOVYwAGg_4M2FHntaLpRTHKs/
```

## Explanation

The original example has an incorrect tx-frequency value for the XPIC configuration. The correction provides the correct value, ensuring consistency within the example. This inconsistency would lead to implementations misinterpreting the example configuration.
