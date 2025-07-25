# Errata 6364 - RFC 8555

- **RFC Title:** Automatic Certificate Management Environment (ACME)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid6364](https://www.rfc-editor.org/errata/eid6364)

```
Section 7.1.4 says:


   wildcard (optional, boolean):  This field MUST be present and true
      for authorizations created as a result of a newOrder request
      containing a DNS identifier with a value that was a wildcard
      domain name.  For other authorizations, it MUST be absent.
      Wildcard domain names are described in Section 7.1.3.

It should say:

   wildcard (optional, boolean):  This field MUST be present and true
      for authorizations created as a result of a newOrder request
      containing a DNS identifier with a value that was a wildcard
      domain name.  For other authorizations, it MUST be absent or
      false.  For pre-authorizations, it MUST be absent or false.
      Wildcard domain names are described in Section 7.1.3.

Notes:

This section states that the wildcard field must be absent for other authorizations, but the example in this section has an explicitly set wildcard field with value false. The proposed change allows both options, either omitting it or explicitly setting it to false. Also a sentence has been added to explicitly describe the behavior for pre-authorizations.
```

## Explanation

The description of the `wildcard` field states it MUST be absent for non-wildcard authorizations, while the example shows it explicitly set to `false`. This creates an inconsistency, making it unclear whether omitting the field or setting it to `false` is the correct approach for non-wildcard authorizations. The proposed change clarifies this, allowing both approaches for non-wildcard and pre-authorizations.
