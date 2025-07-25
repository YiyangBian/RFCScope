# Errata 7949 - RFC 9568

- **RFC Title:** Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6
- **RFC Publication Date:** April 2024
- Link to original errata report: [rfc-editor.org/errata/eid7949](https://www.rfc-editor.org/errata/eid7949)

```
Section 6.4.2 says:


         o  For each IPv4 address associated with the Virtual Router,
            broadcast a gratuitous ARP message containing the Virtual
            Router MAC address and with the target link-layer address
            set to the Virtual Router MAC address.


It should say:

         o  For each IPv4 address associated with the Virtual Router,
            broadcast a gratuitous ARP message containing the Virtual
            Router IPv4 address and with the target link-layer address
            set to the Virtual Router MAC address.


Notes:

The MAC address is specified instead of the IPv4 address.
```

## Explanation

The original text incorrectly specifies the MAC address in the gratuitous ARP message. The correction uses the IPv4 address, which is consistent with the gratuitous ARP protocol. This inconsistency would lead to implementations generating incorrect gratuitous ARP messages.
