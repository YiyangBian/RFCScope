# Errata 4503 - RFC 7483

- **RFC Title:** JSON Responses for the Registration Data Access Protocol (RDAP)
- **RFC Publication Date:** March 2015
- Link to original errata report: [rfc-editor.org/errata/eid4503](https://www.rfc-editor.org/errata/eid4503)

```
Section 5.2 and 5.3 says:


In Section 5.2:

"ldhName" : "ns1.xn--fo-5ja.example",
"unicodeName" : "ns1.foo.example",

In Section 5.3:

"ldhName" : "xn--fo-5ja.example",
"unicodeName" : "foo.example",

"ldhName" : "xn--fo-cka.example",
"unicodeName" : "foo.example"

"ldhName" : "xn--fo-fka.example",
"unicodeName" : "foo.example"

"ldhName": "xn--fo-8ja.example",
"unicodeName" : "foo.example"

It should say:

In Section 5.2:

"ldhName" : "ns1.xn--fo-5ja.example",
"unicodeName" : "ns1.fóo.example",

In Section 5.3:

"ldhName" : "xn--fo-5ja.example",
"unicodeName" : "fóo.example",

"ldhName" : "xn--fo-cka.example",
"unicodeName" : "fõo.example"

"ldhName" : "xn--fo-fka.example",
"unicodeName" : "föo.example"

"ldhName" : "xn--fo-8ja.example",
"unicodeName" : "fôo.example"

Notes:

The unicodeName examples in RFC 7483 are invalid per RFC 5890. Here's an example from Section 5.2 on page 23:

"unicodeName" : "ns1.foo.example",

Section 3 of 7483 says this about Unicode names:

"Unicode names: Textual representations of DNS names where one or more of the labels are U-labels as described by [RFC5890]."

5890 says: "A "U-label" is an IDNA-valid string of Unicode characters, in Normalization Form C (NFC) and including at least one non-ASCII character, expressed in a standard Unicode Encoding Form (such as UTF-8)."

The examples in 7483 contain all ASCII characters. Syntactically valid examples are shown in the corrected text.
```

## Explanation

The original examples for unicodeName in sections 5.2 and 5.3 use only ASCII characters, which contradicts the definition in Section 3 and RFC 5890, requiring at least one non-ASCII character. The correction provides examples that correctly include non-ASCII characters, resolving the inconsistency.  This inconsistency would lead to implementations that incorrectly handle unicodeName values containing non-ASCII characters.
