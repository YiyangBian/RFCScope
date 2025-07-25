# Errata 7866 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid7866](https://www.rfc-editor.org/errata/eid7866)

```
Section Multiple says:


Text occurs in three places

1)    Section 3.5.3

      The leaf-list value is specified as a string, using the canonical
      representation for the YANG data type.  Any reserved characters
      MUST be percent-encoded, according to Sections 2.1 and 2.5 of
      [RFC3986].


2)    Section 3.5.3

      The key value is specified as a string, using the canonical
      representation for the YANG data type.  Any reserved characters
      MUST be percent-encoded, according to Sections 2.1 and 2.5 of
      [RFC3986]. 


3)    Section 5.1

      The contents of any query parameter value MUST be encoded according
      to Section 3.4 of [RFC3986].  Any reserved characters MUST be
      percent-encoded, according to Sections 2.1 and 2.5 of [RFC3986].

It should say:

1)    Section 3.5.3

      The leaf-list value is specified as a string, using the canonical
      representation for the YANG data type.  Any reserved characters
      MUST be percent-encoded, according to Sections 2.1, 2.2, and 2.5 of
      [RFC3986].

2)    Section 3.5.3

      The key value is specified as a string, using the canonical
      representation for the YANG data type.  Any reserved characters
      MUST be percent-encoded, according to Sections 2.1, 2.2, and 2.5 of
      [RFC3986]. 

3)    Section 5.1
      
      The contents of any query parameter value MUST be encoded according
      to Section 3.4 of [RFC3986].  Any reserved characters MUST be
      percent-encoded, according to Sections 2.1, 2.2, and 2.5 of [RFC3986].


Notes:

The reserved character list is defined in section 2.2 of RFC 3986
```

## Explanation

The specification inconsistently refers to sections of RFC3986 for percent-encoding rules.  While Sections 2.1 and 2.5 are mentioned in multiple places, Section 2.2 is omitted but is relevant to defining reserved characters.  This inconsistency creates ambiguity in the implementation of percent-encoding, as implementers may not include all necessary reserved characters specified in Section 2.2.  Therefore, it is classified as INCONSISTENT.
