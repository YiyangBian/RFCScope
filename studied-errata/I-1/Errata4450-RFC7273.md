# Errata 4450 - RFC 7273

- **RFC Title:** RTP Clock Source Signalling
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4450](https://www.rfc-editor.org/errata/eid4450)

```
Section 4.8 says:


  ; PTP domain allowed characters: 0x21-0x7E (IEEE 1588-2002)
   ptp-domain-name = "domain-name=" 1*16ptp-domain-char
   ptp-domain-char = %x21-7E

   ; PTP domain allowed number range: 0-127 (IEEE 1588-2008)
   ptp-domain-nmbr = "domain-nmbr=" ptp-domain-dgts
   ptp-domain-dgts = ptp-domain-n1 / ptp-domain-n2 / ptp-domain-n3
   ptp-domain-n1   = DIGIT             ; 0-9
   ptp-domain-n2   = POS-DIGIT DIGIT   ; 10-99
   ptp-domain-n3   = ("10"/"11") DIGIT ; 100-119
                   / "12" %x30-37      ; 120-127


It should say:

   ; PTP domain allowed characters: 0x21-0x7E (IEEE 1588-2002)
   ptp-domain-name = 1*16ptp-domain-char
   ptp-domain-char = %x21-7E

   ; PTP domain allowed number range: 0-127 (IEEE 1588-2008)
   ptp-domain-nmbr = ptp-domain-dgts
   ptp-domain-dgts = ptp-domain-n1 / ptp-domain-n2 / ptp-domain-n3
   ptp-domain-n1   = DIGIT             ; 0-9
   ptp-domain-n2   = POS-DIGIT DIGIT   ; 10-99
   ptp-domain-n3   = ("10"/"11") DIGIT ; 100-119
                   / "12" %x30-37      ; 120-127


Notes:

There is an inconsistency between ABNF in section 4.8 and examples in section 5.5. Due to evidence that current implementations are working to what is shown in the examples, this is resolved by updating the ABNF specification.
```

## Explanation

The original ABNF for ptp-domain-name and ptp-domain-nmbr includes unnecessary prefixes ("domain-name=" and "domain-nmbr="). The correction removes these prefixes, making the ABNF consistent with the examples provided in Section 5.5 and the actual practice of implementations. This inconsistency would affect parsers that strictly adhere to the original ABNF.
