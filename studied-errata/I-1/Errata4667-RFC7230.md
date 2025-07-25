# Errata 4667 - RFC 7230

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4667](https://www.rfc-editor.org/errata/eid4667)

```
Section 4.1.1 says:


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
accept-ext, t-ranking, and other constructs with similar syntax.
```

## Explanation

The erratum points to an inconsistency between RFC 7230's definition of `chunk-ext` and the actual practices and implementations observed in HTTP agents and ICAP.  The original specification's lack of allowance for whitespace around semicolons and the equals sign is inconsistent with the common practice and RFC 2616's implicit allowance for whitespace.  This inconsistency creates interoperability issues because HTTP agents might generate whitespace in a way that RFC 7230 does not permit, while parsers adhering strictly to RFC 7230 might fail to parse valid HTTP messages. The proposed correction improves consistency and interoperability with older systems.
