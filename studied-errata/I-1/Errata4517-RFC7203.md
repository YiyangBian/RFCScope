# Errata 4517 - RFC 7203

- **RFC Title:** An Incident Object Description Exchange Format (IODEF) Extension for Structured Cybersecurity Information
- **RFC Publication Date:** April 2014
- Link to original errata report: [rfc-editor.org/errata/eid4517](https://www.rfc-editor.org/errata/eid4517)

```
Section 5.2 says:


The schema has the <sequence> </sequence> tags.

It should say:

The tags should be <xsd:sequence></xsd:sequence>.

Notes:

The schema is invalid without the correction.

The examples use <xsd:sequence>, but the actual schema just has <sequence> and does need to be fixed.  With this errata update, the hope is the IANA registered schema can be updated.
```

## Explanation

The erratum corrects an error in the schema definition. The original schema is invalid due to the missing namespace prefix "xsd:" in the <sequence> tags. This inconsistency directly impacts the usability of the schema as it cannot be parsed by schema validators, affecting implementations that rely on schema validation.
