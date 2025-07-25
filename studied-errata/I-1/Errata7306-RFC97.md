# Errata 7306 - RFC 97

- **RFC Title:** HTTP Semantics
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7306](https://www.rfc-editor.org/errata/eid7306)

```
Section 14.1.1 says:


  ranges-specifier = range-unit "=" range-set
  range-set        = 1#range-spec
  range-spec       = int-range
                   / suffix-range
                   / other-range

It should say:

  ranges-specifier = range-unit "=" OWS range-set
  range-set        = 1#range-spec
  range-spec       = int-range
                   / suffix-range
                   / other-range

Notes:

The ABNF is inconsistent with one of the examples given in 14.1.2

   bytes= 0-999, 4500-5499, -1000

The bug in the ABNF was likely introduced when converting away from "implied linear whitespace".

See also <https://github.com/whatwg/fetch/issues/1070#issuecomment-1361800123>.
```

## Explanation

The ABNF for ranges-specifier in Section 14.1.1 is inconsistent with the example provided in Section 14.1.2.  The example shows optional whitespace between the "=" and the range-set, which is not reflected in the ABNF. This inconsistency makes the ABNF less permissive than the actual usage shown in the examples, potentially causing issues for implementations that strictly adhere to the original ABNF.
