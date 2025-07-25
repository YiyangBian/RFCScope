# Errata 5768 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5768](https://www.rfc-editor.org/errata/eid5768)

```
Section 5. says:


   The Compound MAC computation is as follows:

      CMK = CMK[j]
      Compound-MAC = MAC( CMK, BUFFER )

   where j is the number of the last successfully executed inner EAP
   method, MAC is the MAC function negotiated in TLS 1.2 [RFC5246], and
   BUFFER is created after concatenating these fields in the following
   order:


It should say:

The Compound MAC computation is as follows:

    Compound-MAC = the first 20 octets of MAC( CMK[n], BUFFER )

where n is the number of the last successfully executed inner method, MAC is the MAC function negotiated in TLS (e.g. TLS 1.2 in [RFC5246]), and BUFFER is created after concatenating these fields in the following order:


Notes:

This definition of how Compound MAC is computed is not compatible with the definition of Compound MAC fields in the Crypto-Binding TLV. Those fields have a fixed length of 20 octets based on Section 4.2.13 (and that TLV is claimed to have a fixed length of 76 octets). However, the MAC function negotiated in TLS have variable mac_length (e.g., MAC=SHA256 used HMAC-SHA256 with mac_length=32).

How is this supposed to work? Is Section 4.2.13 wrong in claiming that the Compound MAC fields are 20 octets? Or is Section 5.3 wrong in not specifying MAC() function to truncate the output to 20 octets? One of those need to be changed since the current design would work only with the mac_length=20 case (i.e., MAC=SHA with HMAC-SHA1).

Furthermore, that "TLS 1.2" part should not be hardcoding this to not allow TLS 1.3 or newer versions from being used.

It is also a bit strange to see the BUFFER include "The EAP Type sent by the other party in the first TEAP message." since that can only be EAP Type=TEAP, i.e., 55. If that is indeed a fixed value, it does not seem to add any protection for a negotiated parameter as a part of the crypto binding. Regardless, it would be good to be clearer in the text on how this "EAP Type" is to be encoded here (assumable it is a single octet field with value 0x37).

Paul Wouters(AD): Corrected Text provided by the WG and in 7170bis
```

## Explanation

The errata points out a discrepancy between the length of the Compound MAC (20 octets as defined in Section 4.2.13) and the potentially variable length of the MAC function output in Section 5.  This inconsistency would cause implementations to fail unless the MAC output is truncated to 20 octets, which is not explicitly stated in the original specification. The correction clarifies that only the first 20 octets of the MAC function output are used, thus resolving the inconsistency between Section 4.2.13 and Section 5. The updated version also addresses the limitations in the original text relating to TLS version and EAP type encoding. 
