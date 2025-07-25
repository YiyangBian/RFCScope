# Errata 6570 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid6570](https://www.rfc-editor.org/errata/eid6570)

```
Section 11 says:


   o  New typedefs, groupings, rpcs, notifications, extensions,
      features, and identities may be added.

It should say:

   o  New typedefs, groupings, rpcs, actions, notifications,
      extensions, features, and identities may be added.

Notes:

The original text unintentionally fails to mention actions. A definition in a published module may be revised by adding actions to this definition.
```

## Explanation

The original text omits actions from the list of YANG constructs that can be added to a module. This omission creates an inconsistency because actions are valid constructs that can be added. The correction adds actions to the list, resolving the inconsistency.
