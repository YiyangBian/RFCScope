# Errata 5066 - RFC 8152

- **RFC Title:** CBOR Object Signing and Encryption (COSE)
- **RFC Publication Date:** July 2017
- Link to original errata report: [rfc-editor.org/errata/eid5066](https://www.rfc-editor.org/errata/eid5066)

```
Section 14 says:


   o  The restriction applies to the encoding of the Sig_structure, the
      Enc_structure, and the MAC_structure.

It should say:

   o  The restriction applies to the encoding of the COSE_KDF_Context, 
      Sig_structure, the Enc_structure, and the MAC_structure.


Notes:

When listing the set of structure that need to be canonically encoded, I missed this one.

Verifier Notes: this is being fixed in draft-ietf-cose-rfc8152bis-algs.
```

## Explanation

The original text omits COSE_KDF_Context from the list of structures that require canonical encoding. The correction includes COSE_KDF_Context, making the description consistent with the actual requirement. This inconsistency would affect implementations that do not canonically encode the COSE_KDF_Context structure.
