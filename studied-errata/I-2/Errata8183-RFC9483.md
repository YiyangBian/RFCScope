# Errata 8183 - RFC 9483

- **RFC Title:** Lightweight Certificate Management Protocol (CMP) Profile
- **RFC Publication Date:** November 2023
- Link to original errata report: [rfc-editor.org/errata/eid8183](https://www.rfc-editor.org/errata/eid8183)

```
Section 4.1.6.1 says:


              rid             REQUIRED
    -- MUST contain the subjectKeyIdentifier of the CMP protection
    --   certificate, if available, in the rKeyId choice, and the
    --   subjectKeyIdentifier MUST equal the senderKID in the
    --   PKIHeader.
    -- If the CMP protection certificate does not contain a
    --   subjectKeyIdentifier, the issuerAndSerialNumber choice MUST
    --   be used.


It should say:

              rid             REQUIRED	
-- MUST contain the subjectKeyIdentifier of the CMP protection
--   certificate of the request message, if available. The
--   subjectKeyIdentifier is equal the senderKID in the
--   PKIHeader of that message.
-- If the CMP protection certificate of the request message does
--   not contain a subjectKeyIdentifier, the issuerAndSerialNumber
--   choice MUST be used.



Notes:

1. rKeyId choice is wrongly used here as Section 6.2.1 of RFC 5652 does not have rKeyId choice. 
2. rid value must be taken from CMP protection certificate of request message as it is used to specify the recipient.
```

## Explanation

The original text refers to the incorrect method for specifying the recipient identifier (rid), using the rKeyId choice which is not defined in RFC 5652. The correction clarifies that the subjectKeyIdentifier from the request's protection certificate should be used, or issuerAndSerialNumber if subjectKeyIdentifier is absent, resolving the inconsistency.
