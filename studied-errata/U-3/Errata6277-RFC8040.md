# Errata 6277 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid6277](https://www.rfc-editor.org/errata/eid6277)

```
Section 4.8.5 says:


The default value is "last".

It should say:

The default value is “last”, except when used with PUT 
and the target resource already exists, in which case the 
default is to replace the target resource without altering
its position in the "ordered-by user” list or leaf-list.


Notes:

The "last" default is intended for when creating a new element.  

A PUT operation that replaces a list or leaf-list entry should not move the entry unless the "insert" parameter is explicitly passed.
```

## Explanation

The description of the default value for the insertion position in Section 4.8.5 is incomplete and inconsistent. It only specifies "last" as the default, neglecting the different behavior when used with a PUT operation on an existing resource. This omission leads to an incorrect understanding of the default behavior for PUT requests, potentially causing unintended modifications to the list's order.  The correction clarifies the behavior for both creating a new element and replacing an existing one, resolving the inconsistency.
