# Errata 6385 - RFC 8007

- **RFC Title:** Content Delivery Network Interconnection (CDNI) Control Interface / Triggers
- **RFC Publication Date:** December 2016
- Link to original errata report: [rfc-editor.org/errata/eid6385](https://www.rfc-editor.org/errata/eid6385)

```
Section 4.1 says:


   When a CI/T Trigger Command is accepted, the uCDN MUST create a new
   Trigger Status Resource that will convey a specification of the CI/T
   Command and its current status.  The HTTP response to the dCDN MUST
   have status code 201 and MUST convey the URI of the Trigger Status
   Resource in the Location header field [RFC7231].

It should say:

   When a CI/T Trigger Command is accepted, the dCDN MUST create a new
   Trigger Status Resource that will convey a specification of the CI/T
   Command and its current status.  The HTTP response to the uCDN MUST
   have status code 201 and MUST convey the URI of the Trigger Status
   Resource in the Location header field [RFC7231].

Notes:

There has been an accidental switch between "uCDN" and "dCDN" terms in this statement. If my understanding is correct, when the uCDN post a CI/T command to the dCDN, the latter must create a trigger status resource and returns in the response (HTTP code 201) “Location” header the URI of that status resource.
```

## Explanation

The original text incorrectly describes the roles of the uCDN and dCDN when a CI/T Trigger Command is accepted.  The corrected text swaps the roles, accurately reflecting that the dCDN creates the Trigger Status Resource and sends its URI to the uCDN. This inconsistency affects the understanding of the protocol's operation and the correct implementation of the interaction between the two CDNs.
