# Errata 7176 - RFC 9167

- **RFC Title:** Registry Maintenance Notification for the Extensible Provisioning Protocol (EPP)
- **RFC Publication Date:** December 2021
- Link to original errata report: [rfc-editor.org/errata/eid7176](https://www.rfc-editor.org/errata/eid7176)

```
Section 5.1 says:


xmlns="https://www.w3.org/2001/XMLSchema"

It should say:

xmlns="http://www.w3.org/2001/XMLSchema"

Notes:

XML Schema standard https://www.w3.org/TR/xmlschema-1/ "The XML representation of schema components uses a vocabulary identified by the namespace name http://www.w3.org/2001/XMLSchema. "
```

## Explanation

The namespace URI for XML Schema is incorrectly specified as "https://www.w3.org/2001/XMLSchema"; the correct URI is "http://www.w3.org/2001/XMLSchema", creating an inconsistency with the XML Schema standard.
