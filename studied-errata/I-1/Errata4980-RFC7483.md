# Errata 4980 - RFC 7483

- **RFC Title:** JSON Responses for the Registration Data Access Protocol (RDAP)
- **RFC Publication Date:** March 2015
- Link to original errata report: [rfc-editor.org/errata/eid4980](https://www.rfc-editor.org/errata/eid4980)

```
Section 5.5 says:


country -- a string containing the name of the two-character
country code of the autnum

It should say:

country -- a string containing the two-character country
code of the autnum


Notes:

As described in Section 3, country codes should consistently be represented as two-character string values. Note that this differs from the "full name" format used in jCard representations of entity objects.
```

## Explanation

The errata corrects the description of the `country` field. The original description referred to a "two-character country code" as a string containing the name of the country code, which is inconsistent. The corrected description clarifies that `country` should be a two-character string representing the country code, matching the definition in section 3.
