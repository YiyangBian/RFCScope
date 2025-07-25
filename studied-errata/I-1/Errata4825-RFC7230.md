# Errata 4825 - RFC 7230

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4825](https://www.rfc-editor.org/errata/eid4825)

```
Section Appendix B says:


chunk-ext      = *( ";" chunk-ext-name [ "=" chunk-ext-val ] )


It should say:

chunk-ext      = *( BWS  ";" BWS chunk-ext-name
                    [ BWS  "=" BWS chunk-ext-val ] )

Notes:

The infamous "implicit *LWS" syntax rule in RFC 2616 allowed whitespace between
";" and chunk-ext-name in chunk-ext. Some HTTP agents generate that whitespace.
In my experience, HTTP agents that can parse chunk extensions usually can handle
that whitespace. Moreover, ICAP, which generally relies on HTTP/1 for its message
syntax, uses that whitespace when defining the "ieof" chunk extension in RFC 3507
Section 4.5:

      \r\n
      0; ieof\r\n\r\n

IMHO, RFC 7230 should either allow BWS before chunk-ext-name or at the very least
explicitly document the HTTP/1 syntax change and its effect on parsers used for both
ICAP and HTTP/1 messages (a very common case for ICAP-supporting HTTP
intermediaries and ICAP services).

I also recommend adding BWS around "=", for consistency and RFC 2616 backward
compatibility reasons. HTTPbis RFCs already do that for transfer-parameter and
auth-param that have similar syntax.

Please also consider adding BWS _before_ ";" for consistency and RFC 2616 backward
compatibility reasons. HTTPbis RFCs already do that for transfer-extension,
accept-ext,  t-ranking, and other constructs with similar syntax.
```

## Explanation

The erratum highlights an inconsistency between the ABNF rule for `chunk-ext` in Appendix B of RFC 7230 and the actual practices observed in HTTP and ICAP implementations. The original specification does not allow whitespace around semicolons and equals signs within `chunk-ext`, while some HTTP agents generate and parse such whitespace, and RFC 2616 implicitly allowed this.  This inconsistency affects interoperability. The proposed change to include optional whitespace improves compatibility with existing implementations and clarifies the specification, addressing a conflict between the RFC and practical implementations.
