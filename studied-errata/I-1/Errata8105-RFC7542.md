# Errata 8105 - RFC 7542

- **RFC Title:** The Network Access Identifier
- **RFC Publication Date:** May 2015
- Link to original errata report: [rfc-editor.org/errata/eid8105](https://www.rfc-editor.org/errata/eid8105)

```
Section 3.4 says:


Examples of valid Network Access Identifiers include the following:
[...]
        \(user\)@example.net

It should say:

Examples of invalid Network Access Identifiers include the following:
[...]
        \(user\)@example.net

Notes:

\(user\)@example.net is listed as a valid example, but neither backslashes nor parentheses are allowed in the ABNF rules (sections 2.1 and 2.2).  Obsoleted RFC 4282 had ABNF rules to allow for backslash escapes, but RFC 7542 does not.  These are the only backslashes in the entire document.

Perhaps this example should be moved to the invalid examples list?

Or perhaps the ABNF rules should be extended to allow some forms of backslash escapes, although probably not to the same wide-open extent as RFC 4282?
```

## Explanation

The errata report identifies an example of a NAI that is listed as valid but violates the ABNF rules specified in sections 2.1 and 2.2. This inconsistency between the examples and the ABNF rules could lead to incorrect implementations. The inconsistency needs to be resolved either by correcting the example or updating the ABNF rules.
