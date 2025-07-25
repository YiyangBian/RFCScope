# Errata 4949 - RFC 7252

- **RFC Title:** The Constrained Application Protocol (CoAP)
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4949](https://www.rfc-editor.org/errata/eid4949)

```
Section 5.10.7 says:


If any
of these reserved option numbers occurs in addition to Location-Path
and/or Location-Query and are not supported, then a 4.02 (Bad Option)
error MUST be returned.

It should say:

If any
of these reserved option numbers occurs in addition to Location-Path
and/or Location-Query and are not supported, then the response MUST
be rejected (Sections 4.2 and 4.3).

Notes:

The Location-* options are used in responses. A client cannot return a 4.02 (Bad Option) response in reply to a response. The correct behavior is to reject the response.
```

## Explanation

The errata report corrects the handling of unsupported reserved option numbers in responses.  The original specification incorrectly states that a 4.02 (Bad Option) error MUST be returned, which is not possible for a client responding to a server. The correct behavior is to reject the response. This inconsistency impacts implementations that rely on the original specification to handle these responses correctly.
