# Errata 6517 - RFC 8214

- **RFC Title:** Virtual Private Wire Service Support in Ethernet VPN
- **RFC Publication Date:** August 2017
- Link to original errata report: [rfc-editor.org/errata/eid6517](https://www.rfc-editor.org/errata/eid6517)

```
Section 5 says:


   Finally, EVPN may employ data-plane egress link protection mechanisms
   not available in VPWS.  This can be done by the primary PE (on local
   AC down) using the label advertised in the per-EVI Ethernet A-D route
   by the backup PE to encapsulate the traffic and direct it to the
   backup PE.

It should say:

   Finally, EVPN may employ data-plane egress link protection mechanisms.
   This can be done by the primary PE (on local AC down) using the label 
   advertised in the per-EVI Ethernet A-D route by the backup PE to
   encapsulate the traffic and direct it to the backup PE.  Similar behavior
   for LDP-signaled PWs can be achieved using LDP extensions defined in RFC 8104, 
   but the EVPN-based solution is simpler to implement (e.g., does not require 
   context-specific label spaces) and operate.





Notes:

RFC 8104 "Pseudowire (PW) Endpoint Fast Failure Protection" defines a solution for egress PW endpoint protection that provides fast local protection against failure of the primary egress PE and failure of the Attachment Circuit of this PE, so that the claim that the data-plane egress link protection mechanisms are not available for LDP-signaled PWs is factually inaccurate. However, the solution defined in RFC 8104is much more complicated both from the POV of implementation and from the operational POV, while the EVPN-based solution is quite straightforward.
```

## Explanation

The original text incorrectly states that data-plane egress link protection mechanisms are not available in LDP-signaled PWs.  The corrected text acknowledges that such mechanisms exist (as defined in RFC 8104) but points out that the EVPN-based solution is simpler.  The original text's factual inaccuracy makes it inconsistent.
