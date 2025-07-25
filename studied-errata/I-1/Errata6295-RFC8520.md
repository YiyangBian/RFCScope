# Errata 6295 - RFC 8520

- **RFC Title:** Manufacturer Usage Description Specification
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid6295](https://www.rfc-editor.org/errata/eid6295)

```
Section 4.1 says:


For example, if one saw the line "manufacturer" : "flobbidy.example.com",
then all Things that registered with a MUD URL that contained flobbity.example.com in its authority section would match.

It should say:

For example, if one saw the line "manufacturer" : "flobbity.example.com",
then all Things that registered with a MUD URL that contained flobbity.example.com in its authority section would match.

Notes:

Taken at face value it implies somehow a MUD Manager knows about a relationship between two different names flobbidy.example.com and flobbity.example.com in an unexplained way, the correction removes this confusion.
```

## Explanation

The erratum corrects a simple typographical error ("flobbidy" to "flobbity") in an example. However, this error creates an inconsistency within the example.
