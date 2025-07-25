# Errata 6753 - RFC 8664

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Extensions for Segment Routing
- **RFC Publication Date:** December 2019
- Link to original errata report: [rfc-editor.org/errata/eid6753](https://www.rfc-editor.org/errata/eid6753)

```
Section 4.3.1 says:


If the F bit is set to zero
      (see below), then the NT field has no meaning and MUST be ignored
      by the receiver. 

It should say:

If the F bit is set to one
      (see below), then the NT field has no meaning and MUST be ignored
      by the receiver. 

Notes:

Later it says, when this F bit is set to 1, the NAI value is absent, so the NT field has no meaning. 
     F:   When this bit is set to 1, the NAI value in the subobject
           body is absent.  The F bit MUST be set to 1 if NT=0;
           otherwise, it MUST be set to zero.  The S and F bits MUST NOT
           both be set to 1.
```

## Explanation

The original text incorrectly states that the NT field should be ignored when the F bit is zero. The correction clarifies that the NT field is ignored when the F bit is one, which is consistent with the later description of the F bit. This inconsistency would lead to incorrect interpretation and handling of the NT field.
