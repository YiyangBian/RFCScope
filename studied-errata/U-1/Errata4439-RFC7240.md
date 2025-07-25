# Errata 4439 - RFC 7240

- **RFC Title:** Prefer Header for HTTP
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4439](https://www.rfc-editor.org/errata/eid4439)

```
Section 2 says:


     preference = token [ BWS "=" BWS word ]
                  *( OWS ";" [ OWS parameter ] )
     parameter  = token [ BWS "=" BWS word ]

It should say:

     preference = preference-parameter *( OWS ";" [ OWS
                  preference-parameter ] )
     preference-parameter = parameter / token


Notes:

Section 1.1 incorrectly states that "word" is defined in RFC 7230.  It is not.  Therefore, the syntax is completely under-specified.

The "parameter" rule, as defined in RFC 7231, is used in lots of other header field definitions successfully.  The only drawback is that "parameter" doesn't permit the use of "OWS" either side of the "=" character.

This change would also require changes to Section 1.1.
```

## Explanation

The erratum points out that the original specification uses an undefined term "word" in the definition of `preference` and `parameter`, rendering the syntax incomplete and making it impossible to unambiguously implement support for the Prefer header. The lack of a clear definition for "word" and the suggested replacement using the more precisely defined `parameter` rule from RFC 7231 directly addresses this underspecification, impacting the correct implementation of parsing and handling of the Prefer header.
