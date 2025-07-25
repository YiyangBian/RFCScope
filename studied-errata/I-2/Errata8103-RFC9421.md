# Errata 8103 - RFC 9421

- **RFC Title:** HTTP Message Signatures
- **RFC Publication Date:** February 2024
- Link to original errata report: [rfc-editor.org/errata/eid8103](https://www.rfc-editor.org/errata/eid8103)

```
Section 7.5.3 says:


Several parts of this specification rely on the parsing of Structured
Field values [STRUCTURED-FIELDS] -- in particular, strict
serialization of HTTP Structured Field values (Section 2.1.1),
referencing members of a Dictionary Structured Field (Section 2.1.2),
and processing the @signature-input value when verifying a signature
(Section 3.2).  While Structured Field values are designed to be
relatively simple to parse, a naive or broken implementation of such
a parser could lead to subtle attack surfaces being exposed in the
implementation.

For example, if a buggy parser of the @signature-input value does not
enforce proper closing of quotes around string values within the list
of component identifiers, an attacker could take advantage of this
and inject additional content into the signature base through
manipulating the Signature-Input field value on a message.

It should say:

Several parts of this specification rely on the parsing of Structured
Field values [STRUCTURED-FIELDS] -- in particular, strict
serialization of HTTP Structured Field values (Section 2.1.1),
referencing members of a Dictionary Structured Field (Section 2.1.2),
and processing the @signature-params value when verifying a signature
(Section 3.2).  While Structured Field values are designed to be
relatively simple to parse, a naive or broken implementation of such
a parser could lead to subtle attack surfaces being exposed in the
implementation.

For example, if a buggy parser of the @signature-params value does not
enforce proper closing of quotes around string values within the list
of component identifiers, an attacker could take advantage of this
and inject additional content into the signature base through
manipulating the Signature-Input field value on a message.

Notes:

"@signature-input" should be changed to "@signature-params". There is one such error in both the first and second paragraphs of Section 7.5.3.
```

## Explanation

The text in Section 7.5.3 incorrectly refers to "@signature-input" in two places where it should refer to "@signature-params". This inconsistency could lead to misunderstandings of how the specification should be implemented and affect security, because the correct handling of the @signature-params field is critical for signature verification.
