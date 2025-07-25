# Errata 7132 - RFC 8851

- **RFC Title:** RTP Payload Format Restrictions
- **RFC Publication Date:** January 2021
- Link to original errata report: [rfc-editor.org/errata/eid7132](https://www.rfc-editor.org/errata/eid7132)

```
Section 10 says:


rid-id            = 1*(alpha-numeric / "-" / "_")

It should say:

rid-id            = 1*255(alpha-numeric)

Notes:

The BNF should be consistent with the rules for the RtpStreamId/RepairedRtpStreamId SDES from RFC 8852 section 3:

"As with all SDES items, RtpStreamId and RepairedRtpStreamId are limited to a total of 255 octets in length. RtpStreamId and RepairedRtpStreamId are constrained to contain only alphanumeric characters. For avoidance of doubt, the only allowed byte values for these IDs are decimal 48 through 57, 65 through 90, and 97 through 122."
```

## Explanation

The original ABNF for rid-id allows hyphens and underscores, which is inconsistent with RFC 8852's restriction to only alphanumeric characters. The correction limits rid-id to alphanumeric characters and restricts the maximum length to 255 octets, ensuring consistency with RFC 8852.
