# Errata 4169 - RFC 7230

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4169](https://www.rfc-editor.org/errata/eid4169)

```
Section 7 says:


     #element => [ ( "," / element ) *( OWS "," [ OWS element ] ) ]

     1#element => *( "," OWS ) element *( OWS "," [ OWS element ] )

   Empty elements do not contribute to the count of elements present.
   For example, given these ABNF productions:

     example-list      = 1#example-list-elmt
     example-list-elmt = token ; see Section 3.2.6

   Then the following are valid values for example-list (not including
   the double quotes, which are present for delimitation only):

     "foo,bar"
     "foo ,bar,"
     "foo , ,bar,charlie   "

It should say:

     #element => [ ( "," / element ) *( OWS "," [ OWS element ] ) ]

     1#element => *( "," OWS ) element *( OWS "," [ OWS element ] )

   Empty elements do not contribute to the count of elements present.
   For example, given these ABNF productions:

     example-list      = 1#example-list-elmt
     example-list-elmt = token ; see Section 3.2.6

   Then the following are valid values for example-list (not including
   the double quotes, which are present for delimitation only):

     "foo,bar"
     "foo ,bar,"
     "foo , ,bar,charlie"

Notes:

"foo , ,bar,charlie   " cannot be derived from 1#token (legacy list rule)
"foo , ,bar,charlie" can be derived from 1#token (legacy list rule)
```

## Explanation

The errata report points out an inconsistency in the ABNF rules provided in Section 7 of RFC 7230.  The original specification allows for trailing whitespace in a way that is not consistent with how 1#element is defined, which affects the implementation of HTTP message parsing. The correction clarifies the valid values for the example-list, directly impacting how applications should parse and handle lists of elements in HTTP messages.  This is a technical error affecting the implementation of the specification.
