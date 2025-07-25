# Errata 4297 - RFC 7394

- **RFC Title:** Definition of Time to Live TLV for LSP-Ping Mechanisms
- **RFC Publication Date:** November 2014
- Link to original errata report: [rfc-editor.org/errata/eid4297](https://www.rfc-editor.org/errata/eid4297)

```
Section 3.1 says:


3.1. TTL TLV Format


   0                   1                   2                   3
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Type = 32769                 |   Length = 8                  |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |   Value       |   Reserved    |   Flags                       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                  Figure 1: Time To Live TLV Format

It should say:

3.1. TTL TLV Format


   0                   1                   2                   3
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Type = 32769                 |   Length = 4                  |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |   Value       |   Reserved    |   Flags                       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                  Figure 1: Time To Live TLV Format

Notes:

In an LSP Ping TTL, Length value should show length of the value fields only. See RFC 4379 section 3.
```

## Explanation

The original specification incorrectly defines the Length field as 8 octets. The correction sets it to 4 octets, aligning with RFC 4379, which mandates that the Length field in TLVs only includes the size of the value. This inconsistency would lead to incorrect interpretation and processing of the Time To Live TLV.
