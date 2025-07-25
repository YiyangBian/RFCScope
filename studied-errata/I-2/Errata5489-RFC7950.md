# Errata 5489 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid5489](https://www.rfc-editor.org/errata/eid5489)

```
Section 7.20.3.2 says:


The argument "delete" deletes properties from the target node.  The
   properties to delete are identified by substatements to the "delete"
   statement. 

It should say:

The argument "delete" deletes properties from the target node.  The
   properties to delete are identified by substatements to the "deviate"
   statement.
```

## Explanation

The errata points out that Section 7.20.3.2 incorrectly states that properties are deleted using substatements to the "delete" statement.  The correction indicates that it should refer to substatements of the "deviate" statement. This is a direct contradiction within the specification impacting implementation. The text instructs the use of a non-existent mechanism, resulting in an inconsistent specification.
