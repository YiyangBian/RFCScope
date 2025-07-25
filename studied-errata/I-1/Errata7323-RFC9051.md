# Errata 7323 - RFC 9051

- **RFC Title:** Internet Message Access Protocol (IMAP) - Version 4rev2
- **RFC Publication Date:** August 2021
- Link to original errata report: [rfc-editor.org/errata/eid7323](https://www.rfc-editor.org/errata/eid7323)

```
Section 6.4.4.4. says:


        S: B283 NO [BADCHARSET UTF-8] KOI8-R is not supported


It should say:

        S: B283 NO [BADCHARSET (KOI8-R)] KOI8-R is not supported


Notes:

The BADCHARSET response code is described in 7.1 as "Optionally followed by a parenthesized list of charsets", and in the formal syntax as:

   resp-text-code =/ "BADCHARSET" [SP "(" charset *(SP charset) ")" ]

Although a client's parser might use a generic resp-text-code (atom [SP 1*<any TEXT-CHAR except "]">]) as a fallback, the server should parenthesize even when only one charset is sent.
```

## Explanation

The original BADCHARSET response code is missing the required parentheses around the charset. The correction adds the parentheses, making the response consistent with the specification.
