# Errata 5775 - RFC 7170

- **RFC Title:** Tunnel Extensible Authentication Protocol (TEAP) Version 1
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5775](https://www.rfc-editor.org/errata/eid5775)

```
Section 5. says:


   For authentication methods that generate keying material, further
   protection against man-in-the-middle attacks is provided through
   cryptographically binding keying material established by both TEAP
   Phase 1 and TEAP Phase 2 conversations.  After each successful inner
   EAP authentication, EAP EMSK and/or MSKs are cryptographically
   combined with key material from TEAP Phase 1 to generate a Compound
   Session Key (CMK).  The CMK is used to calculate the Compound MAC as
   part of the Crypto-Binding TLV described in Section 4.2.13, which
   helps provide assurance that the same entities are involved in all
   communications in TEAP.  During the calculation of the Compound MAC,
   the MAC field is filled with zeros.

   The Compound MAC computation is as follows:

      CMK = CMK[j]
      Compound-MAC = MAC( CMK, BUFFER )

   where j is the number of the last successfully executed inner EAP
   method, MAC is the MAC function negotiated in TLS 1.2 [RFC5246], and
   BUFFER is created after concatenating these fields in the following
   order:


It should say:

[Append to the end of section 5.3] 

If no key generating inner method is run then no EMSK or MSK will be generated. If an IMSK needs to be generated then the MSK and therefore the IMSK is set to all zeroes (i.e., IMSK = MSK = 32 octets of 0x00s).

Notes:

Section 5.3 does not describe how CMK is derived for the case where not inner EAP authentication method is executed (e.g., when Basic-Password-Auth is used at TLV level). Section 5.4 seems to address that case by implying that S-IMCK = session_key_seed (S-IMCK[0] does indeed have that value, but MSK/EMSK derivation uses S-IMCK[j], so use of S-IMCK here is slightly misleading). This seems to imply that MSK/EMSK derivation uses S-IMCK[0] and as such, Compound MAC derivation might use CMK[0], but CMK[0] is not defined (Section 5.2 defines CMK[j] for j=1..n-1, but not for j=0.

Furthermore, Section 4.2.13 is not clear on what Flags should be used in Crypto-Binding TLV when no inner EAP authentication method is executed. The only three values defined for Flags (1..3) all imply that either EMSK or MSK (or both) based Compound MAC is present, but there is no inner EAP method MSK/EMSK in this case since no such inner EAP method was executed. Maybe a new Flags value should be defined or alternatively, the MSK Compound MAC case could be extended to cover this no inner-EAP case with CMK[0] defined as proposed above to calculate the MSK Compound MAC.

Paul Wouters(AD): Corrected Text provided by the WG and in 7170bis
```

## Explanation

The erratum points out that Section 5 does not specify how the CMK is derived when no inner EAP authentication method is executed. This omission makes the specification incomplete and ambiguous for implementations that need to handle cases where no key-generating inner method is used.  The lack of clear guidance on CMK derivation in this scenario directly affects the implementation's ability to generate correct Compound MAC values.
