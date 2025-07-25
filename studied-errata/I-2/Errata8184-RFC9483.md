# Errata 8184 - RFC 9483

- **RFC Title:** Lightweight Certificate Management Protocol (CMP) Profile
- **RFC Publication Date:** November 2023
- Link to original errata report: [rfc-editor.org/errata/eid8184](https://www.rfc-editor.org/errata/eid8184)

```
Section 4.1.6.2 says:


          rid           REQUIRED
-- MUST contain the subjectKeyIdentifier of the CMP protection
--   certificate, if available, in the rKeyId choice, and the
--   subjectKeyIdentifier MUST equal the senderKID in the
--   PKIHeader.
-- If the CMP protection certificate does not contain a
--   subjectKeyIdentifier, the issuerAndSerialNumber choice MUST
--   be used


It should say:

          rid           REQUIRED
-- MUST contain the subjectKeyIdentifier of the CMP protection
--   certificate of the request message, if available, in the
--   rKeyId choice. The subjectKeyIdentifier is equal
--   the senderKID in the PKIHeader of that message.
-- If the CMP protection certificate of the request message does
--   not contain a subjectKeyIdentifier, the issuerAndSerialNumber
--   choice MUST be used.


Notes:

1. rid value must be taken from CMP protection certificate of request message as it is used to identify the recipient using key agreement.
2. senderKID refer to value in request message, and here we are preparing the response message. So MUST is removed.
```

## Explanation

The original text uses the term "rKeyId choice", which is not defined in RFC 5652, and incorrectly implies a requirement that the subjectKeyIdentifier MUST equal the senderKID in the PKIHeader of the response message. The correction clarifies that the subjectKeyIdentifier from the CMP protection certificate of the request message should be used, and removes the MUST condition, aligning with the intended behavior. This inconsistency could lead to implementations incorrectly handling the rid parameter.
