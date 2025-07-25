# Errata 7997 - RFC 7344

- **RFC Title:** Automating DNSSEC Delegation Trust Maintenance
- **RFC Publication Date:** September 2014
- Link to original errata report: [rfc-editor.org/errata/eid7997](https://www.rfc-editor.org/errata/eid7997)

```
Section 6.2.1 says:


When a Parent operates in "calculate DS" mode, it can operate in one
   of two sub-modes:

   full:  The Parent only publishes DS records it calculates from DNSKEY
      records.

It should say:

When a Parent operates in "calculate DS" mode, it can operate in one
   of two sub-modes:

   full:  The Parent only publishes DS records it calculates from CDNSKEY
      records.

Notes:

In the last sentence, "DNSKEY" should be "CDNSKEY".  That is, the Parent calculates DS records from the CDNSKEY records, not from the DNSKEY records.

Paul Wouters (AD): Verifying as the regular AD is an author on the doc :)
```

## Explanation

The erratum points out an incorrect technical detail in Section 6.2.1 of RFC 7344, specifically regarding the record type used for DS record calculation.  The original text states that the Parent calculates DS records from DNSKEY records, while the correction specifies that it should be CDNSKEY records. This is an inconsistency that directly affects the implementation of the specification.
