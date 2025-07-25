# Errata 4839 - RFC 7230

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4839](https://www.rfc-editor.org/errata/eid4839)

```
Section 4 says:


   Parameters are in the form of a name or name=value pair.

     transfer-parameter = token BWS "=" BWS ( token / quoted-string )

It should say:

   Parameters are in the form of a name=value pair.

     transfer-parameter = token BWS "=" BWS ( token / quoted-string )

Notes:

The ABNF does not allow the form of a name.
```

## Explanation

The errata highlights a contradiction. The text states that parameters can be in the form of a name or name=value pair, but the ABNF only allows the name=value pair form. This inconsistency affects how implementations will parse and handle parameters, making it unclear whether a parameter should always have a value or if a name-only parameter is valid.
