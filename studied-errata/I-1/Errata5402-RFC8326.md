# Errata 5402 - RFC 8326

- **RFC Title:** Graceful BGP Session Shutdown
- **RFC Publication Date:** March 2018
- Link to original errata report: [rfc-editor.org/errata/eid5402](https://www.rfc-editor.org/errata/eid5402)

```
Section C.2.2. says:


      4.  If, for any reason, RR3 processes the withdraw generated in
          step 3 before processing the update generated in step 2, RR3
          transiently suffers from unreachability for the affected
          prefix.

It should say:

      4.  If, for any reason, RR2 processes the withdraw generated in
          step 3 before processing the update generated in step 2, RR2
          transiently suffers from unreachability for the affected
          prefix.

Notes:

The original text names RR3, but it should be RR2. This becomes evident when one works through the example using a diagram.
```

## Explanation

The original text refers to RR3, when it should refer to RR2.  This inconsistency affects the accuracy of the example and could lead to misinterpretations of the graceful BGP session shutdown procedure.
