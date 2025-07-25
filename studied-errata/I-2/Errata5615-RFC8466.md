# Errata 5615 - RFC 8466

- **RFC Title:** A YANG Data Model for Layer 2 Virtual Private Network (L2VPN) Service Delivery
- **RFC Publication Date:** October 2018
- Link to original errata report: [rfc-editor.org/errata/eid5615](https://www.rfc-editor.org/errata/eid5615)

```
Section 5.10.1 says:


   The svc-bandwidth parameter must include a "cos-id" parameter if the
   "type" is set to "bw-per-cos".  The cos-id can be assigned based on
   either (1) the IEEE 802.1p value [IEEE-802-1D] in the C-tag or
   (2) the Differentiated Services Code Point (DSCP) in the Ethernet
   frame header.  Service frames are metered against the bandwidth
   profile based on the cos-id.

It should say:

   The svc-bandwidth parameter must include a "cos-id" parameter if the
   "type" is set to "bw-per-cos".  The cos-id can be assigned based on
   either (1) the IEEE 802.1p value [IEEE-802-1D] in the C-tag or
   (2) the Differentiated Services Code Point (DSCP) in the IP
   header.  Service frames are metered against the bandwidth
   profile based on the cos-id.

Notes:

The DSCP field is part of the IP packet header, not the Ethernet frame руфвук.
```

## Explanation

The original text incorrectly states that the DSCP value is located in the Ethernet frame header. The correction identifies the IP header as the correct location, resolving the inconsistency. This inconsistency would affect implementations that incorrectly attempt to extract the DSCP value from the Ethernet header.
