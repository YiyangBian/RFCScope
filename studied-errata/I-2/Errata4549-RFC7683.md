# Errata 4549 - RFC 7683

- **RFC Title:** Diameter Overload Indication Conveyance
- **RFC Publication Date:** October 2015
- Link to original errata report: [rfc-editor.org/errata/eid4549](https://www.rfc-editor.org/errata/eid4549)

```
Section 4.3 says:


The overloaded realm is identified by the Destination-Realm AVP 
of the message containing the OLR.

It should say:

The overloaded realm is identified by the Origin-Realm AVP
of the message containing the OLR.

Notes:

When the overload report is of type "REALM_REPORT", the overloaded realm is identified by the Origin-Realm AVP of the Diameter command i.e. the realm of the originator of the Diameter command with the overload report.
```

## Explanation

The original text incorrectly identifies the Destination-Realm AVP as the identifier of the overloaded realm in an Overload Indication message. The correct AVP to identify the overloaded realm is the Origin-Realm AVP.  This inconsistency affects the interpretation and implementation of the Diameter Overload Indication Conveyance mechanism.
