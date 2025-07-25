# Errata 5996 - RFC 8163

- **RFC Title:** Transmission of IPv6 over Master-Slave/Token-Passing (MS/TP) Networks
- **RFC Publication Date:** May 2017
- Link to original errata report: [rfc-editor.org/errata/eid5996](https://www.rfc-editor.org/errata/eid5996)

```
Section Appendix B. says:


       /*
        * Sanity check the encoding to prevent the while() loop below
        * from overrunning the output buffer.
        */
       if (read_index + code > length)
         return 0;


It should say:

       /*
        * Sanity check the encoding to prevent the while() loop below
        * from overrunning the output buffer.
        */
       if (code == 0 || read_index + code > length)
         return 0;


Notes:

This was submitted as a change to [BACnet], Annex T, by James Butler.  The normative procedure for decoding COBS is correct in [BACnet], 9.10.3.2(a) but this bug appears in the informative example in Annex T.  Since the purpose of COBS encoding is to eliminate all zero bytes from the data, the presence of a zero indicates an error.
```

## Explanation

The original code lacks a check for a zero code value, which is an error condition in COBS encoding.  The correction adds this check, making the example code consistent with the normative decoding procedure. This inconsistency would lead to implementations failing to detect errors in COBS encoded data.
