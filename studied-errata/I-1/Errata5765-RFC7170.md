# Errata 5765 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5765](https://www.rfc-editor.org/errata/eid5765)

```
Section 4.2.2 says:


   M

      Mandatory, set to one (1)


It should say:

   M

      0 (Optional)


Notes:

Authority-ID TLV is used only as an Outer TLV (in TEAP/Start) and Section 4.3.1 mandates all Outer TLVs to be marked as optional ("Outer TLVs MUST be marked as optional"). As such, Section 4.2.2 is incorrect in claiming the Authority-ID TLV to use M=1.
```

## Explanation

The errata highlights a contradiction between Section 4.2.2 and Section 4.3.1 regarding the mandatory/optional status of the Authority-ID TLV.  Section 4.3.1 mandates all Outer TLVs to be optional, while Section 4.2.2 incorrectly states the Authority-ID TLV as mandatory. This directly impacts implementation as it provides conflicting instructions on how to handle this specific TLV.
