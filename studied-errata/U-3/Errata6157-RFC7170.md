# Errata 6157 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid6157](https://www.rfc-editor.org/errata/eid6157)

```
Section 4.2.9 says:


  Status

      The Status field is one octet.  This indicates the result if the
      server does not process the action requested by the peer.

It should say:

  Status

      The Status field is one octet.  This indicates the result if the
      party who receives this TLV does not process the action.

Notes:

The status field is carried in the "Request-Action" frame.  As is stated at the start of the section, the frame can be sent either by the server or the peer.
```

## Explanation

The original description of the Status field is ambiguous because it only refers to the server's processing. The correction clarifies that the Status field indicates the result if either the server or the peer does not process the action. This ambiguity impacts implementation, as developers may only consider server-side processing for the Status field, potentially leading to incorrect handling of the field when the peer does not process the action.
