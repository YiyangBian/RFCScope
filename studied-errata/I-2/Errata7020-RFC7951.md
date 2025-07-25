# Errata 7020 - RFC 7951

- **RFC Title:** JSON Encoding of Data Modeled with YANG
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid7020](https://www.rfc-editor.org/errata/eid7020)

```
Section 6.8 says:


An "identityref" value is represented as a string -- the name of an
identity.  If the identity is defined in a module other than the leaf
node containing the identityref value, the namespace-qualified form
(Section 4) MUST be used.  Otherwise, both the simple and namespace-
qualified forms are permitted.

It should say:

An "identityref" value is represented as a string -- the name of an
identity.  If the identity is defined in a module other than the leaf or
leaf-list node containing the identityref value, the namespace-qualified
form (Section 4) MUST be used.  Otherwise, both the simple and namespace-
qualified forms are permitted.

Notes:

The original text omitted leaf-list nodes, which may also be of "identityref" type.
```

## Explanation

The original text incorrectly limits the description to only leaf nodes when describing the usage of namespace-qualified forms for identityref values. The correction extends this to include leaf-list nodes as well, which can also be of the identityref type.  This omission creates an inconsistency between the description and the actual permissible usage.
