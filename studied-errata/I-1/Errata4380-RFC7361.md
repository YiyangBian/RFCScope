# Errata 4380 - RFC 7361

- **RFC Title:** LDP Extensions for Optimized MAC Address Withdrawal in a Hierarchical Virtual Private LAN Service (H-VPLS)
- **RFC Publication Date:** September 2014
- Link to original errata report: [rfc-editor.org/errata/eid4380](https://www.rfc-editor.org/errata/eid4380)

```
Section 5.2 says:


   At least one of the following sub-TLVs MUST be included in the MAC
   Flush Parameters TLV if the C-flag is set to 1:

   o  PBB B-MAC List Sub-TLV:

      Type: 0x0407

      Length: Value length in octets.  At least one B-MAC address MUST
      be present in the list.

      Value: One or a list of 48-bit B-MAC addresses.  These are the
      source B-MAC addresses associated with the B-VPLS instance that
      originated the MAC withdraw message.  It will be used to identify
      the C-MAC(s) mapped to the B-MAC(s) listed in the sub-TLV.

   o  PBB I-SID List Sub-TLV:

      Type: 0x0408

      Length: Value length in octets.  Zero indicates an empty I-SID
      list.  An empty I-SID list means that the flushing applies to all
      the I-SIDs mapped to the B-VPLS indicated by the FEC TLV.

      Value: One or a list of 24-bit I-SIDs that represent the
      I-component FIB(s) where the MAC flushing needs to take place.

It should say:

   At least one of the following sub-TLVs MUST be included in the MAC
   Flush Parameters TLV if the C-flag is set to 1:

   o  PBB B-MAC List Sub-TLV:

      Type: 0x01
      Length: Value length in octets.  At least one B-MAC address MUST
      be present in the list.

      Value: One or a list of 48-bit B-MAC addresses.  These are the
      source B-MAC addresses associated with the B-VPLS instance that
      originated the MAC withdraw message.  It will be used to identify
      the C-MAC(s) mapped to the B-MAC(s) listed in the sub-TLV.

   o  PBB I-SID List Sub-TLV:

      Type: 0x02
      Length: Value length in octets.  Zero indicates an empty I-SID
      list.  An empty I-SID list means that the flushing applies to all
      the I-SIDs mapped to the B-VPLS indicated by the FEC TLV.

      Value: One or a list of 24-bit I-SIDs that represent the
      I-component FIB(s) where the MAC flushing needs to take place.

Notes:

Type definition was error. The PBB B-MAC List Sub-TLV abd I-SID List Sub-TLV are only support for one byte, as defined in section 5.1.1 MAC flush parameters TLV.
This error was imported from draft-ietf-l2vpn-vpls-ldp-mac-opt-12. For this version, it submit the 2 sub-tlv to IANA for alloc id. But the two kinds tlv were sub-tlv, not LDP TLV
```

## Explanation

The original text uses incorrect Type values (0x0407 and 0x0408) for the PBB sub-TLVs. The correction provides the correct Type values (0x01 and 0x02), resolving the inconsistency.  This inconsistency would directly affect implementations that rely on the original, incorrect Type values, rendering them unable to correctly interpret and process the PBB sub-TLVs.
