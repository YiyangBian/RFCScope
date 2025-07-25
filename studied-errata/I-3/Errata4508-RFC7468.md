# Errata 4508 - RFC 7468

- **RFC Title:** Textual Encodings of PKIX, PKCS, and CMS Structures
- **RFC Publication Date:** April 2015
- Link to original errata report: [rfc-editor.org/errata/eid4508](https://www.rfc-editor.org/errata/eid4508)

```
Section 3 says:


  preeb      = "-----BEGIN " label "-----" ; unlike [RFC1421] (A)BNF,
                                           ; eol is not required (but
  posteb     = "-----END " label "-----"   ; see [RFC1421], Section 4.4)


It should say:

  preeb      = "-----" %x42.45.47.49.4E " " label "-----" 

  posteb     = "-----" %x45.4E.44 " " label"-----"
                         ; unlike [RFC1421] (A)BNF, eol is not required
                         ; (but see [RFC1421], Section 4.4)

OR:

  preeb      = %s"-----BEGIN " label "-----" ; unlike [RFC1421] (A)BNF,
                                             ; eol is not required (but
  posteb     = %s"-----END " label "-----"   ; see [RFC1421],
                                             ; Section 4.4)

...with reference to RFC 7405.

Notes:

The encapsulation boundaries are case-sensitive, including (especially) the BEGIN and END characters. Nearly all implementations enforce the case sensitivity of BEGIN and END on input, and all surveyed implementations output all-caps.
```

## Explanation

The original ABNF for preeb and posteb does not correctly enforce the case sensitivity of the BEGIN and END keywords. The correction uses hexadecimal notation to explicitly specify the uppercase characters, ensuring that implementations correctly handle case sensitivity.  The original ABNF is inconsistent with the actual behavior of implementations and the case sensitivity requirements of the specified encoding.
