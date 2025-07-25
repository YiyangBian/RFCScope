# Errata 5078 - RFC 7252

- **RFC Title:** The Constrained Application Protocol (CoAP)
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid5078](https://www.rfc-editor.org/errata/eid5078)

```
Section 7.2.1 says:


The Content-Format code
attribute MAY include a space-separated sequence of Content-Format
codes, indicating that multiple content-formats are available.  The
syntax of the attribute value is summarized in the production "ct-
value" in Figure 12, where "cardinal", "SP", and "DQUOTE" are defined
as in [RFC6690].

It should say:

The Content-Format code
attribute MAY include a space-separated sequence of Content-Format
codes, indicating that multiple content-formats are available.
The Content-Format code attribute MUST NOT appear more than once in a 
link.  The syntax of the attribute value is summarized in the 
production "ct-value" in Figure 12, where "cardinal", "SP", and 
"DQUOTE" are defined as in [RFC6690].

Notes:

Insert a sentence that says that the code MUST NOT appear more than once.  This appears to be what was intended, but not stated, by the authors since it supports the space separated values to appear in a single attribute value.
```

## Explanation

The original text does not explicitly prohibit multiple occurrences of the Content-Format attribute within a single link, while the space-separated sequence implies that multiple content formats can be specified within a single attribute value. This creates an inconsistency and ambiguity in how the Content-Format attribute should be used. The correction clarifies that the attribute MUST NOT appear more than once, resolving the ambiguity.
