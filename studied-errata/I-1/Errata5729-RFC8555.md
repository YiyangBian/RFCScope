# Errata 5729 - RFC 8555

- **RFC Title:** Automatic Certificate Management Environment (ACME)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid5729](https://www.rfc-editor.org/errata/eid5729)

```
Section 7.5.1 says:


The client indicates to the server that it is ready for the challenge
validation by sending an empty JSON body ("{}") carried in a POST
request to the challenge URL (not the authorization URL).

It should say:

The client indicates to the server that it is ready for the challenge
validation by sending a POST request to the challenge URL (not the
authorization URL), where the body of the POST request is a JWS object
whose JSON payload is a response object (see Section 8).  For all
challenge types defined in this document, the response object is the
empty JSON object ("{}").

Notes:

It's clear from other text in section 7.5.1 that the "empty JSON body" is interpreted by the ACME server as a "response object".  (The first function of this erratum is to clarify this point).

Section 8 says that "The definition of a challenge type includes...Contents of response objects", and section 7.5.1 notes that "the challenges in this document do not define any response fields, but future specifications might define them".  (The second function of this erratum is to permit clients to send response objects that contain response fields).
```

## Explanation

The description of the challenge validation process in Section 7.5.1 is inconsistent with the requirement for a JWS-signed response object as defined in Section 8.  The original text incorrectly describes the request body as simply an empty JSON object, while the full specification requires it to be a JWS object containing an empty JSON object. This inconsistency affects client implementation which must correctly construct and sign the JWS object for challenge validation.
