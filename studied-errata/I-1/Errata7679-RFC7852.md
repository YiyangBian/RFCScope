# Errata 7679 - RFC 7852

- **RFC Title:** Additional Data Related to an Emergency Call
- **RFC Publication Date:** July 2016
- Link to original errata report: [rfc-editor.org/errata/eid7679](https://www.rfc-editor.org/errata/eid7679)

```
Section 6.1 says:


An example
   Call-Info header field for this would be:

   Call-Info:  https://www.example.com/23sedde3;
       purpose="EmergencyCallData.ProviderInfo"

It should say:

An example
   Call-Info header field for this would be:

   Call-Info:  https://www.example.com/23sedde3;
       purpose=EmergencyCallData.ProviderInfo

Notes:

Remove double quote on purpose attribute. It's a token type instead of "String" type.
```

## Explanation

The original example includes double quotes around the purpose attribute, which is a token type and should not be quoted. This inconsistency between the example and the specification of the attribute type affects the interpretation and correct implementation of the Call-Info header field.
