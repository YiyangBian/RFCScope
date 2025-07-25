# Errata 6178 - RFC 7807

- **RFC Title:** Problem Details for HTTP APIs
- **RFC Publication Date:** March 2016
- Link to original errata report: [rfc-editor.org/errata/eid6178](https://www.rfc-editor.org/errata/eid6178)

```
Section 3 says:


   The ability to convey problem-specific extensions allows more than
   one problem to be conveyed.  For example:

   HTTP/1.1 400 Bad Request
   Content-Type: application/problem+json
   Content-Language: en

   {
   "type": "https://example.net/validation-error",
   "title": "Your request parameters didn't validate.",
   "invalid-params": [ {
                         "name": "age",
                         "reason": "must be a positive integer"
                       },
                       {
                         "name": "color",
                         "reason": "must be 'green', 'red' or 'blue'"}
                     ]
   }


It should say:

   The ability to convey problem-specific extensions allows more than
   one problem to be conveyed.  For example:

   HTTP/1.1 400 Bad Request
   Content-Type: application/problem+json
   Content-Language: en

   {
   "type": "https://example.net/validation-error",
   "title": "Your request parameters didn't validate.",
   "invalid_params": [ {
                         "name": "age",
                         "reason": "must be a positive integer"
                       },
                       {
                         "name": "color",
                         "reason": "must be 'green', 'red' or 'blue'"}
                     ]
   }


Notes:

The "invalid-params" member in the example is named incorrectly. According to Section 4, it should contain an "_" rather than a "-" in its name:

>   If such additional members are defined, their names SHOULD start with
>   a letter (ALPHA, as per [RFC5234], Appendix B.1) and SHOULD consist
>   of characters from ALPHA, DIGIT ([RFC5234], Appendix B.1), and "_"
>   (so that it can be serialized in formats other than JSON), and they
>   SHOULD be three characters or longer.
```

## Explanation

The example in Section 3 uses the member name "invalid-params", which is inconsistent with the naming guidelines specified in Section 4.  Section 4 recommends using underscores instead of hyphens in member names for better interoperability and serialization in various formats. This inconsistency affects the interoperability and correctness of problem details implementations. The corrected example uses "invalid_params", which adheres to the guidelines in Section 4.
