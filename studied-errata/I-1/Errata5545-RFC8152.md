# Errata 5545 - RFC 8152

- **RFC Title:** CBOR Object Signing and Encryption (COSE)
- **RFC Publication Date:** July 2017
- Link to original errata report: [rfc-editor.org/errata/eid5545](https://www.rfc-editor.org/errata/eid5545)

```
Section 7.1 says:


   +---------+-------+----------------+------------+-------------------+
   | Name    | Label | CBOR Type      | Value      | Description       |
   |         |       |                | Registry   |                   |
   +---------+-------+----------------+------------+-------------------+
   | kty     | 1     | tstr / int     | COSE Key   | Identification of |
   |         |       |                | Common     | the key type      |
   |         |       |                | Parameters |                   |
   |         |       |                |            |                   |
   | kid     | 2     | bstr           |            | Key               |
   |         |       |                |            | identification    |
   |         |       |                |            | value -- match to |
   |         |       |                |            | kid in message    |
   |         |       |                |            |                   |
   | alg     | 3     | tstr / int     | COSE       | Key usage         |
   |         |       |                | Algorithms | restriction to    |
   |         |       |                |            | this algorithm    |
   |         |       |                |            |                   |
   | key_ops | 4     | [+ (tstr/int)] |            | Restrict set of   |
   |         |       |                |            | permissible       |
   |         |       |                |            | operations        |
   |         |       |                |            |                   |
   | Base IV | 5     | bstr           |            | Base IV to be     |
   |         |       |                |            | xor-ed with       |
   |         |       |                |            | Partial IVs       |
   +---------+-------+----------------+------------+-------------------+

                          Table 3: Key Map Labels

It should say:

   +---------+-------+----------------+------------+-------------------+
   | Name    | Label | CBOR Type      | Value      | Description       |
   |         |       |                | Registry   |                   |
   +---------+-------+----------------+------------+-------------------+
   | kty     | 1     | tstr / int     | COSE Key   | Identification of |
   |         |       |                | Types      | the key type      |
   |         |       |                |            |                   |
   |         |       |                |            |                   |
   | kid     | 2     | bstr           |            | Key               |
   |         |       |                |            | identification    |
   |         |       |                |            | value -- match to |
   |         |       |                |            | kid in message    |
   |         |       |                |            |                   |
   | alg     | 3     | tstr / int     | COSE       | Key usage         |
   |         |       |                | Algorithms | restriction to    |
   |         |       |                |            | this algorithm    |
   |         |       |                |            |                   |
   | key_ops | 4     | [+ (tstr/int)] |            | Restrict set of   |
   |         |       |                |            | permissible       |
   |         |       |                |            | operations        |
   |         |       |                |            |                   |
   | Base IV | 5     | bstr           |            | Base IV to be     |
   |         |       |                |            | xor-ed with       |
   |         |       |                |            | Partial IVs       |
   +---------+-------+----------------+------------+-------------------+

                          Table 3: Key Map Labels

Notes:

The value registry for kty should be COSE Key Types, as indicated in the text following Table 3. This change affects the IANA registry: https://www.iana.org/assignments/cose/cose.xhtml#key-common-parameters
```

## Explanation

The original table incorrectly describes the value registry for the kty parameter as "COSE Key Common Parameters." The correction uses the correct term "COSE Key Types", resolving the inconsistency between the table and the text following it.
