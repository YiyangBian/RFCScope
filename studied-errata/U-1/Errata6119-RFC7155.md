# Errata 6119 - RFC 7155

- **RFC Title:** Diameter Network Access Server Application
- **RFC Publication Date:** April 2014
- Link to original errata report: [rfc-editor.org/errata/eid6119](https://www.rfc-editor.org/errata/eid6119)

```
Throughout the document, when it says:


[Missing sections when RFC 4005 was obsoleted by RFC 7155]

It should say:

4.7 AVPs Used Only for Compatibility

   The AVPs defined in this section SHOULD only be used for backwards
   compatibility when a Diameter/RADIUS translation function is invoked
   and are not typically originated by Diameter systems during normal
   operations.

                                            +----------+
                                            | AVP Flag |
                                            |  Rules   |
                                            |----+-----|
                                            |MUST| MUST|
   Attribute Name           Section Defined |    |  NOT|
   -----------------------------------------|----+-----|
   Origin-AAA-Protocol      4.7.1           | M  |  V  |
   -----------------------------------------|----+-----|

4.7.1.  Origin-AAA-Protocol

   The Origin-AAA-Protocol AVP (AVP Code 408) is of the type Enumerated
   and should be inserted in a Diameter message translated by a gateway
   system from another AAA protocol, such as RADIUS.  It identifies the
   source protocol of the message to the Diameter system receiving the
   message.

   The supported values are:

         1       RADIUS


Notes:

The description of Origin-AAA-Protocol (AVP Code 408) is missing from RFC 7155. The AVP is documented in RFC 4005 section 9.3.6.

The proposed corrected text contains RFC 4005 section 9.3 as RFC 7155 section 4.7, and RFC 4005 section 9.3.6 as RFC 7155 section 4.7.1. All other AVPs in RFC 4005 section 9.3.x are not listed because they are documented in their relevant standards already.

RFC 7155 is listed as the Reference for Origin-AAA-Protocol in multiple locations in https://www.iana.org/assignments/aaa-parameters/aaa-parameters.xhtml

It appears that there may be an accidental omission of Origin-AAA-Protocol when RFC 7155 obsoleted RFC 4005.

The Origin-AAA-Protocol AVP is referenced in other sections in RFC 7155:
- 3.1.  AA-Request (AAR) Command
- 3.2.  AA-Answer (AAA) Command
- 3.3.  Re-Auth-Request (RAR) Command
- 3.4.  Re-Auth-Answer (RAA) Command
- 3.5.  Session-Termination-Request (STR) Command
- 3.6.  Session-Termination-Answer (STA) Command
- 3.7.  Abort-Session-Request (ASR) Command
- 3.8.  Abort-Session-Answer (ASA) Command
- 3.9.  Accounting-Request (ACR) Command
- 3.10.  Accounting-Answer (ACA) Command
- 5.1.  AA-Request / AA-Answer AVP Table
- 5.2.1.  Framed Access Accounting AVP Table
- 5.2.2.  Non-Framed Access Accounting AVP Table
```

## Explanation

The erratum highlights a missing section in RFC 7155 related to the Origin-AAA-Protocol AVP.  The omission renders the specification incomplete because implementations would lack the necessary information to correctly handle this AVP, which is referenced in multiple sections of RFC 7155.  The reference to this AVP in other sections of RFC 7155 makes it crucial to the overall implementation.
