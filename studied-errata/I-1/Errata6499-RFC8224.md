# Errata 6499 - RFC 8224

- **RFC Title:** Authenticated Identity Management in the Session Initiation Protocol (SIP)
- **RFC Publication Date:** February 2018
- Link to original errata report: [rfc-editor.org/errata/eid6499](https://www.rfc-editor.org/errata/eid6499)

```
Section 4 says:


Identity = "Identity" HCOLON signed-identity-digest SEMI
          ident-info *( SEMI ident-info-params )
signed-identity-digest = 1*(base64-char / ".")
ident-info = "info" EQUAL ident-info-uri
ident-info-uri = LAQUOT absoluteURI RAQUOT
ident-info-params = ident-info-alg / ident-type /
    ident-info-extension
ident-info-alg = "alg" EQUAL token
ident-type = "ppt" EQUAL token
ident-info-extension = generic-param

base64-char = ALPHA / DIGIT / "/" / "+"


It should say:

Identity = "Identity" HCOLON signed-identity-digest SEMI
          ident-info *( SEMI ident-info-params )
signed-identity-digest = 1*(base64url-char / ".")
ident-info = "info" EQUAL ident-info-uri
ident-info-uri = LAQUOT absoluteURI RAQUOT
ident-info-params = ident-info-alg / ident-type /
    ident-info-extension
ident-info-alg = "alg" EQUAL token
ident-type = "ppt" EQUAL token
ident-info-extension = generic-param

base64url-char = ALPHA / DIGIT / "-" / "_"


Notes:

RFC 8225 makes it clear that the encoding is BASE4URL, not the standard BASE64 encoding.

See also:
- https://datatracker.ietf.org/doc/html/rfc8224#section-4.1.1
- https://datatracker.ietf.org/doc/html/rfc7515#appendix-F
- https://datatracker.ietf.org/doc/html/rfc7515#appendix-C
- https://datatracker.ietf.org/doc/html/rfc4648#section-5
```

## Explanation

The original ABNF uses base64-char, which is not appropriate for the application. The correction uses base64url-char, which is consistent with RFC 8225 and the intended use of base64url encoding for the signed-identity-digest.
