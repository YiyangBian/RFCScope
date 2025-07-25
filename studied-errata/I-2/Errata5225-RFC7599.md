# Errata 5225 - RFC 7599

- **RFC Title:** Mapping of Address and Port using Translation (MAP-T)
- **RFC Publication Date:** July 2015
- Link to original errata report: [rfc-editor.org/errata/eid5225](https://www.rfc-editor.org/errata/eid5225)

```
Section 6 says:


In the case of an IPv4 prefix, the IPv4 address field is right-padded
with zeros up to 32 bits.  The PSID is left-padded with zeros to
create a 16-bit field.  For an IPv4 prefix or a complete IPv4
address, the PSID field is zero.

It should say:

The PSID is left-padded with zeros to
create a 16-bit field.  For an IPv4 prefix or a complete IPv4
address, the PSID field is zero.

Notes:

This text has been copied from RFC7597 (MAP-E). While it is correct in the context of MAP-E, for MAP-T the complete IPv4 source address must be embedded in the interface-identifier for correct translation in the case of an IPv4 prefix. Right padding the prefix with zeroes would lead to the translated packet having all zeroes in its source address.
```

## Explanation

The original description for MAP-T incorrectly states that the IPv4 address field is right-padded with zeros, while the correct behavior is to embed the complete IPv4 source address in the interface-identifier. This inconsistency is due to the text being copied from MAP-E where it is correct, but incorrect for MAP-T.  This inconsistency would lead to incorrect translation of IPv4 packets.
