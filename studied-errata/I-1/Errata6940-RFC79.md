# Errata 6940 - RFC 79

- **RFC Title:** Internet Key Exchange Protocol Version 2 (IKEv2)
- **RFC Publication Date:** October 2014
- Link to original errata report: [rfc-editor.org/errata/eid6940](https://www.rfc-editor.org/errata/eid6940)

```
Section .10 says:


o SPI Size (1 octet) - Length in octets of the SPI as defined by the
 IPsec protocol ID or zero if no SPI is applicable. For a
 notification concerning the IKE SA, the SPI Size MUST be zero and
 the field must be empty.


It should say:

o SPI Size (1 octet) - Length in octets of the SPI as defined by the
 IPsec protocol ID or zero if no SPI is applicable. For a
 notification concerning the IKE SA, the SPI Size MUST be zero and
 the SPI field must be empty.


Notes:

the field must be empty -> the SPI field must be empty

additional question: so for a notification concerning the IKE SA, the Protocol ID field still shall be zero?

Yes, for IKE SA notifications the SPI can be seen from the header, thus there is no point of repeating the SPIs in notify payload. The Protocol ID field of the notification payload indicates which type of SPI is inside the notification payload, thus if there is no SPI in there, then there is no point of having Protocol ID either.
```

## Explanation

The original text states that the SPI field must be empty for IKE SA notifications but doesn't explicitly mention the SPI Size field. The correction clarifies that the SPI field MUST be empty for IKE SA notifications, resolving the inconsistency and ensuring that both the SPI Size and SPI fields are correctly handled. The original description leaves room for misinterpretation of whether only the SPI field or both the SPI and SPI Size fields should be handled in the IKE SA notification.
