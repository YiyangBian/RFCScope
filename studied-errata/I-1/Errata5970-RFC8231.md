# Errata 5970 - RFC 8231

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Extensions for Stateful PCE
- **RFC Publication Date:** September 2017
- Link to original errata report: [rfc-editor.org/errata/eid5970](https://www.rfc-editor.org/errata/eid5970)

```
Section 8.5 says:


19       Invalid Operation

                Error-value
                1:   Attempted LSP Update Request for a non-delegated
                     LSP.  The PCEP-ERROR object is followed by the LSP
                     object that identifies the LSP.

It should say:

19       Invalid Operation

                Error-value
                1:   Attempted LSP Update Request for a non-delegated
                     LSP.

Notes:

RFC 8231 Section 6.3 - LSP Object is not part of PCErr message.
```

## Explanation

The original text incorrectly states that the LSP object is included in the PCErr message for error-value 1. The corrected text removes the reference to the LSP object, as it is not part of the PCErr message. This inconsistency affects the interpretation and implementation of error reporting in stateful PCE.
