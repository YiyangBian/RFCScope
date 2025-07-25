# Errata 5436 - RFC 7208

- **RFC Title:** Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1
- **RFC Publication Date:** April 2014
- Link to original errata report: [rfc-editor.org/errata/eid5436](https://www.rfc-editor.org/errata/eid5436)

```
Throughout the document, when it says:


    header-field     = "Received-SPF:" [CFWS] result FWS [comment FWS]
                       [ key-value-list ] CRLF

It should say:

    header-field     = "Received-SPF:" [CFWS] result [ FWS comment ]
                       [ FWS key-value-list ] [FWS] CRLF

Notes:

As specified, this ABNF doesn't allow a header field value like result-FWS-comment with no FWS or key-value-list following it, a header field value which occurs very often in Received-SPF header fields I see in practice.  (Note that FWS must contain at least one white space.)  The corrected ABNF better follows practice in implementations.
```

## Explanation

The erratum corrects the ABNF for the header-field, addressing a mismatch between the specification and observed implementations. The original ABNF is too restrictive, preventing valid header field values from being parsed. This inconsistency impacts implementations that parse Received-SPF header fields, leading to potential errors in processing.
