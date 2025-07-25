# Errata 7173 - RFC 8520

- **RFC Title:** Manufacturer Usage Description Specification
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid7173](https://www.rfc-editor.org/errata/eid7173)

```
Section 9 says:


Within each access list, access is permitted to packets flowing to or from the Thing that can be mapped to the domain name of "service.bms.example.com".

It should say:

Within each access list, access is permitted to packets flowing to or from the Thing that can be mapped to the domain name of "test.example.com".

Notes:

The subdomain in the Figure does not correspond to the one in the text.
```

## Explanation

The text describes access control for "service.bms.example.com", which is inconsistent with the diagram showing "test.example.com".  This discrepancy affects the understanding of the example and its implementation.
