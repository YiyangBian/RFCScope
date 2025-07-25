# Errata 7955 - RFC 9562

- **RFC Title:** Universally Unique IDentifiers (UUIDs)
- **RFC Publication Date:** May 2024
- Link to original errata report: [rfc-editor.org/errata/eid7955](https://www.rfc-editor.org/errata/eid7955)

```
Section 5.1 says:


time_high:
    The least significant 12 bits from the 60-bit starting timestamp.
    Occupies bits 52 through 63 (octets 6-7).

It should say:

time_high:
    The most significant 12 bits from the 60-bit starting timestamp.
    Occupies bits 52 through 63 (octets 6-7).

Notes:

The original text has the least significant 12 bits from the 60-bit starting timestamp duplicated in the UUID. Once as the least significant 12 bits of time_low and again as time_high. The most significant 12 bits of the starting timestamp are omitted from the UUID.

The corrected text gives the self-evident intention of the committee.
```

## Explanation

The original text incorrectly describes the time_high field as containing the least significant bits of the timestamp. The correction clarifies that it contains the most significant bits, which is the intended behavior. This inconsistency could lead to incorrect generation of UUIDs.
