# Errata 5566 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid5566](https://www.rfc-editor.org/errata/eid5566)

```
Section B.3.2 says:


          "player" : {
            "gap" : 0.5
          }


It should say:

          "player" : {
            "gap" : "0.5"
          }


Notes:

The quoted text occurs twice; p 128 and p 130.

The leaf "gap" is defined as type decimal64 in A.1.  According to RFC 7951, section 6.1, a decimal64 type is represented as a string in JSON.
```

## Explanation

The example in Section B.3.2 incorrectly represents the "gap" leaf, which is defined as type decimal64, as a numerical value instead of a string.  This contradicts RFC 7951, section 6.1, that specifies decimal64 values should be represented as strings in JSON.  This inconsistency affects the correct implementation of JSON serialization for decimal64 types. Therefore it is classified as INCONSISTENT.
