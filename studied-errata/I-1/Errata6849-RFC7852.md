# Errata 6849 - RFC 7852

- **RFC Title:** Additional Data Related to an Emergency Call
- **RFC Publication Date:** July 2016
- Link to original errata report: [rfc-editor.org/errata/eid6849](https://www.rfc-editor.org/errata/eid6849)

```
Section 11.7 says:


Example(s):  TEL;VALUE=uri;TYPE="main,voice";PREF=1:tel:+1-418-656-90
      00

It should say:

Example(s):  TEL;VALUE=uri;TYPE="main-number,voice";PREF=1:tel:+1-418-656-90
      00

Notes:

The type value is specified as "main-number" but in the example is simply "main".
```

## Explanation

The example provided for the TYPE parameter uses "main" while the specification indicates that it should be "main-number".  This inconsistency between the specification and the example could lead to misinterpretations and incorrect implementations.
