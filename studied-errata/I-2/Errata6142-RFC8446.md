# Errata 6142 - RFC 8446

- **RFC Title:** The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid6142](https://www.rfc-editor.org/errata/eid6142)

```
Section 4.6.1. says:


Clients MUST NOT cache tickets for longer than 7 days

It should say:

Clients MUST NOT use tickets for longer than 7 days

Notes:

"MUST NOT cache" is surely overly zealous and may unnecessarily result in non-compliant implementations
```

## Explanation

The original wording is overly restrictive. While it is recommended to limit ticket usage to 7 days, strictly prohibiting caching is unnecessarily strict. The corrected wording focuses on usage duration rather than caching, which offers more flexibility to implementations without compromising security.
