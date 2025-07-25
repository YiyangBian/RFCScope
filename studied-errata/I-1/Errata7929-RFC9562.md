# Errata 7929 - RFC 9562

- **RFC Title:** Universally Unique IDentifiers (UUIDs)
- **RFC Publication Date:** May 2024
- Link to original errata report: [rfc-editor.org/errata/eid7929](https://www.rfc-editor.org/errata/eid7929)

```
Section B.2 says:


custom_c  62   0b00, 0x38a375d0df1fbf6

It should say:

custom_c  62   0b01, 0x38a375d0df1fbf6

Notes:

As shown as -938a- in Figure 30.

B: xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
C: 5c146b14-3c52-8afd-938a-375d0df1fbf6

See also: https://mailarchive.ietf.org/arch/msg/uuidrev/2wJLek182NMv4xQZf8TIos6XrD0/
```

## Explanation

The original example uses an incorrect value for the custom_c variant.  The correction provides the correct value, which is consistent with Figure 30.  This inconsistency would affect implementations that rely on the correct values for UUID variants.
