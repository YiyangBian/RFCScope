# Errata 6684 - RFC 8572

- **RFC Title:** Secure Zero Touch Provisioning (SZTP)
- **RFC Publication Date:** April 2019
- Link to original errata report: [rfc-editor.org/errata/eid6684](https://www.rfc-editor.org/errata/eid6684)

```
Section 8.1 says:


   The DHCPv4 server MAY include a single instance of the
   OPTION_V4_SZTP_REDIRECT option in DHCP messages it sends.  Servers
   MUST NOT send more than one instance of the OPTION_V4_SZTP_REDIRECT
   option.

It should say:

   The DHCPv4 server MAY include OPTION_V4_SZTP_REDIRECT in DHCP messages it sends.

Notes:

The original text contradicts the statement in the same section:
   "If the length of the 'bootstrap-server-list' field is too large to
   fit into a single option, then OPTION_V4_SZTP_REDIRECT MUST be split
   into multiple instances of the option according to the process
   described in [RFC3396]."
```

## Explanation

The original specification contains conflicting statements regarding the number of OPTION_V4_SZTP_REDIRECT options allowed in DHCP messages. The corrected version removes the restriction on the number of options, aligning with the text in the same section that allows for multiple instances of the option when necessary.
