# Errata 4212 - RFC 7366

- **RFC Title:** Encrypt-then-MAC for Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)
- **RFC Publication Date:** September 2014
- Link to original errata report: [rfc-editor.org/errata/eid4212](https://www.rfc-editor.org/errata/eid4212)

```
Section 3 says:


   In TLS [2] notation, the MAC calculation for TLS 1.0 without
   the explicit Initialization Vector (IV) is:

   MAC(MAC_write_key, seq_num +
       TLSCipherText.type +
       TLSCipherText.version +
       TLSCipherText.length +
       ENC(content + padding + padding_length));

   and for TLS 1.1 and greater with an explicit IV is:

   MAC(MAC_write_key, seq_num +
       TLSCipherText.type +
       TLSCipherText.version +
       TLSCipherText.length +
       IV +
       ENC(content + padding + padding_length));


It should say:

Note that the length value used for the MAC computation differs from 
the value of the 'uint16 length' field in the TLSCiphertext record as 
encoded on the wire.  The encoded TLSCiphertext record contains both 
the ciphtertext and the MAC, while the MAC calculation is performed 
only over the ciphertext.  The length value encoded in the 
TLSCiphertext record is therefore 'length' while the length value 
used in the MAC calculation is 'length - SecurityParameters.mac_length'.

More formally, if:

  TLSCiphertext.enc_content = ENC(content + padding + padding_length)

then in TLS notation the MAC calculation for TLS 1.0 without the 
explicit Initialization Vector (IV) is:

   MAC(MAC_write_key, seq_num +
       TLSCipherText.type +
       TLSCipherText.version +
       length of (TLSCiphertext.enc_content) +
       TLSCiphertext.enc_content);

and for TLS 1.1 and greater with an explicit IV is:

   MAC(MAC_write_key, seq_num +
       TLSCipherText.type +
       TLSCipherText.version +
       length of (IV + TLSCiphertext.enc_content) +
       IV +
       TLSCiphertext.enc_content);


Notes:

After the RFC was published a new set of implementers (who hadn't been part of the pre-publication interop testing) pointed out that the text covering the use of length values could be interpreted in two different ways.  This correction attempts to remove the ambiguity by making explicit what's MACd vs. what's encoded on the wire.
```

## Explanation

The errata corrects the description of the length value used in the MAC calculation for TLS. The original description used the length of the entire TLSCipherText record, which includes both the ciphertext and the MAC, whereas the MAC calculation should only include the ciphertext length. This inconsistency could lead to incorrect MAC calculations. The corrected description clarifies that the length used for MAC calculation is the length of the ciphertext only, resolving the ambiguity.
