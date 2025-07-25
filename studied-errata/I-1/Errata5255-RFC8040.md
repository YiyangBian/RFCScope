# Errata 5255 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid5255](https://www.rfc-editor.org/errata/eid5255)

```
Section 3.5.3. says:


If there are multiple key leaf values, the path 
segment is constructed by having the list name, 
followed by the value of each leaf identified 
in the "key" statement, encoded in the order
specified in the YANG "key" statement.  Each key 
leaf value except the last one is followed by 
a comma character.

It should say:

If there are multiple key leaf values, the path 
segment is constructed by having the list name,  
followed by an "=" character, 
followed by the value of each leaf identified 
in the "key" statement, encoded in the order
specified in the YANG "key" statement.  Each key 
leaf value except the last one is followed by 
a comma character.

Notes:

When describing the encoding of key values for a list, in the case of multiple keys the "=" equal sign is not mentioned although it is used in the examples.
```

## Explanation

The description of key value encoding in Section 3.5.3 is inconsistent with the examples provided. The description omits the '=' character used to separate the key name and its value in the path segment, while the examples correctly include it. This inconsistency could lead to incorrect implementation of key value encoding in RESTCONF clients and servers.
