# Errata 6231 - RFC 8231

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Extensions for Stateful PCE
- **RFC Publication Date:** September 2017
- Link to original errata report: [rfc-editor.org/errata/eid6231](https://www.rfc-editor.org/errata/eid6231)

```
Section 8.5 says:


      20       LSP State Synchronization Error

                Error-value
                1:   A PCE indicates to a PCC that it cannot process (an
                     otherwise valid) LSP State Report.  The PCEP-ERROR
                     object is followed by the LSP object that
                     identifies the LSP.

It should say:

      20       LSP State Synchronization Error

                Error-value
                1:   A PCE indicates to a PCC that it cannot process (an
                     otherwise valid) LSP State Report.  

Notes:

This is a companion errata to https://www.rfc-editor.org/errata/eid5970 which identified the issue in Error-type 19 Error-value 1. The same issue exists for Error-type 20 Error-value 1 i.e. LSP Object is not part of the PCErr message.
```

## Explanation

The original text incorrectly states that the LSP object is included in the PCErr message for error-value 1. The corrected text removes the reference to the LSP object, as it is not part of the PCErr message. This inconsistency affects the interpretation and implementation of error reporting in stateful PCE.
