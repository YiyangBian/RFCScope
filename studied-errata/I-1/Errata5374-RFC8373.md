# Errata 5374 - RFC 8373

- **RFC Title:** Negotiating Human Language in Real-Time Communications
- **RFC Publication Date:** May 2018
- Link to original errata report: [rfc-editor.org/errata/eid5374](https://www.rfc-editor.org/errata/eid5374)

```
Section 5.4. says:


   An offer or answer indicating written Greek both ways:

      m=text 45020 RTP/AVP 103 104
      a=hlang-send:gr
      a=hlang-recv:gr

It should say:

   An offer or answer indicating written Greek both ways:

      m=text 45020 RTP/AVP 103 104
      a=hlang-send:el
      a=hlang-recv:el

Notes:

The language tag to represent Greek is "el" per BCP 47.

The IANA language subtag registry has the following entry for Greek:

Type: language
Subtag: el
Description: Modern Greek (1453-)
Added: 2005-10-16

https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry
```

## Explanation

The original example uses the incorrect language tag "gr" for Greek. The correct tag is "el", as defined in BCP 47 and the IANA language subtag registry.  This inconsistency affects the interoperability of implementations that rely on the example to represent the Greek language.
