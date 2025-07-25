# Errata 6656 - RFC 8588

- **RFC Title:** Personal Assertion Token (PaSSporT) Extension for Signature-based Handling of Asserted information using toKENs (SHAKEN)
- **RFC Publication Date:** May 2019
- Link to original errata report: [rfc-editor.org/errata/eid6656](https://www.rfc-editor.org/errata/eid6656)

```
Section 6 says:


Protected Header
   {
      "alg":"ES256",
      "typ":"passport",
      "ppt":"shaken",
      "x5u":"https://cert.example.org/passport.cer"
   }
   Payload
   {
      "attest":"A"
      "dest":{"tn":["12155550131"]}
      "iat":"1443208345",
      "orig":{"tn":"12155550121"},
      "origid":"123e4567-e89b-12d3-a456-426655440000"
   }

It should say:

Protected Header
   {
      "alg":"ES256",
      "typ":"passport",
      "ppt":"shaken",
      "x5u":"https://cert.example.org/passport.cer"
   }
   Payload
   {
      "attest":"A"
      "dest":{"tn":["12155550131"]}
      "iat":1443208345,
      "orig":{"tn":"12155550121"},
      "origid":"123e4567-e89b-12d3-a456-426655440000"
   }

Notes:

As per RFC8225 (5.1.1), 'iat' is a NumericDate format, which is a number (commonly referred to as a utime). Section 9.4 also specifies that anything that is numeric must be encoded as a number.
```

## Explanation

The original example uses quotes around the "iat" value, which represents a number and should not have quotes according to RFC 8225 and the JSON specification. This inconsistency needs to be corrected to ensure that the example correctly reflects the JSON encoding of numeric values.
