# Errata 7311 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid7311](https://www.rfc-editor.org/errata/eid7311)

```
Section 7 says:


              +-------------------------+------------------+
              | error-tag               | status code      |
              +-------------------------+------------------+
(...)
              | unknown-attribute       | 400              |
              |                         |                  |
              | bad-element             | 400              |
(...)

It should say:

              +-------------------------+------------------+
              | error-tag               | status code      |
              +-------------------------+------------------+
(...)
              | unknown-attribute       | 400              |
              |                         |                  |
              | missing-element         | 400              |
              |                         |                  |
              | bad-element             | 400              |
(...)

Notes:

Add missing-element to the table Mapping from <error-tag> to Status Code
in Section 7.

The NETCONF error-tag missing-element is not listed in the table mapping
error-tag to HTTP status code. This seems to be a mistake since all other
error-tags are listed (even the obsolete partial-operation which should not
be used according to RFC 6241).
```

## Explanation

The table in Section 7 mapping error tags to HTTP status codes is missing the entry for "missing-element", which is a valid NETCONF error tag. This omission is inconsistent with the inclusion of other error tags, including an obsolete one. The inconsistency could lead to incorrect implementation of error handling in RESTCONF servers that do not map the missing-element error tag to an appropriate HTTP status code.
