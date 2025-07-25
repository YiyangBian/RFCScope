# Errata 7334 - RFC 8727

- **RFC Title:** JSON Binding of the Incident Object Description Exchange Format
- **RFC Publication Date:** August 2020
- Link to original errata report: [rfc-editor.org/errata/eid7334](https://www.rfc-editor.org/errata/eid7334)

```
Section 6 says:


          {iodef-BusinessImpact => BusinessImpact /


It should say:

          {iodef-BusinessImpact => BusinessImpact} /


Notes:

A closing brace is missing in this line of the rule for "Assessment".
```

## Explanation

The original rule for "Assessment" is missing a closing brace, which makes it syntactically incorrect and impacts the processing of the JSON binding.  The correction adds the missing brace to ensure that the rule is correctly parsed.
