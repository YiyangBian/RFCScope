# Errata 7093 - RFC 95

- **RFC Title:** JSON Responses for the Registration Data Access Protocol (RDAP)
- **RFC Publication Date:** June 2021
- Link to original errata report: [rfc-editor.org/errata/eid7093](https://www.rfc-editor.org/errata/eid7093)

```
Section 4.1 says:


The data structure named "rdapConformance" is an array of strings,
each providing a hint as to the specifications used in the construction
of the response.

It should say:

The data structure named "rdapConformance" is an array of strings,
each identifying a registered specification used in the construction
of the response.


Notes:

The original text uses the word "hint", which some people have interpreted to mean "not normative" and/or "can be ignored". This misinterpretation will likely cause significant misunderstanding of the technical specification and might result in faulty implementations if not corrected. The intention and meaning of this sentence is more clearly specified with the corrected text, noting that the array of string identifiers is directly associated with the set of specifications used to construct an RDAP response.
```

## Explanation

The use of the word "hint" in the original description is ambiguous and allows for misinterpretations of the rdapConformance data structure.  The corrected text clarifies that the strings identify registered specifications, removing the ambiguity and ensuring that implementations correctly process this data structure.
