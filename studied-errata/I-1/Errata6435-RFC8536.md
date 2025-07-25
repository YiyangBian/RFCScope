# Errata 6435 - RFC 8536

- **RFC Title:** The Time Zone Information Format (TZif)
- **RFC Publication Date:** February 2019
- Link to original errata report: [rfc-editor.org/errata/eid6435](https://www.rfc-editor.org/errata/eid6435)

```
Section 5.2 says:


   >> Response <<

   HTTP/1.1 200 OK
   Date: Fri, 01 Jun 2018 14:52:23 GMT
   Content-Type: application/json; charset="utf-8"
   Content-Length: xxxx

It should say:

   >> Response <<

   HTTP/1.1 200 OK
   Date: Fri, 01 Jun 2018 14:52:23 GMT
   Content-Type: application/json
   Content-Length: xxxx

Notes:

There is no charset parameter on application/json. See https://tools.ietf.org/html/rfc8259#section-11 (last sentence).
```

## Explanation

The original response includes a charset parameter in the Content-Type header for application/json, which is incorrect according to RFC 8259. The correction removes the charset parameter, making the response consistent with the specification.
