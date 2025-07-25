# Errata 7389 - RFC 8824

- **RFC Title:** Static Context Header Compression (SCHC) for the Constrained Application Protocol (CoAP)
- **RFC Publication Date:** June 2021
- Link to original errata report: [rfc-editor.org/errata/eid7389](https://www.rfc-editor.org/errata/eid7389)

```
Section 3.1 says:


For example, the Uri-Path option is
mandatory in the request, and it might not be present in the
response.

It should say:

For example, the Uri-Path option can
be used in the request, while it is not used in the response.

Notes:

The Uri-Path option is not mandatory in a CoAP request, and it is not supposed to be used in a CoAP response.
```

## Explanation

The original text incorrectly states that the Uri-Path option is mandatory in CoAP requests and implies it might be present in responses. The correction clarifies that Uri-Path is not mandatory in requests and is not used in responses, thus resolving the inconsistencies.
