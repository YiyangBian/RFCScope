# Errata 4252 - RFC 7230

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4252](https://www.rfc-editor.org/errata/eid4252)

```
Section 2.7.2. says:


     https-URI = "https:" "//" authority path-abempty [ "?" query ]
                 [ "#" fragment ]


It should say:

     https-URI = "https:" "//" authority path-abempty [ "?" query ]


Notes:

See erratum 4251 on the same document.
```

## Explanation

This erratum, referencing erratum 4251, highlights an inconsistency similar to erratum 4250.  The inclusion of the optional fragment identifier in the definition of `https-URI` in Section 2.7.2 contradicts RFC 3986.  This affects the correct implementation of HTTPS URI parsing and generation, potentially leading to interoperability issues.  The correction ensures consistency with the URI syntax defined in RFC 3986.
