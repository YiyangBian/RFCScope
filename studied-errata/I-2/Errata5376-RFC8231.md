# Errata 5376 - RFC 8231

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Extensions for Stateful PCE
- **RFC Publication Date:** September 2017
- Link to original errata report: [rfc-editor.org/errata/eid5376](https://www.rfc-editor.org/errata/eid5376)

```
Section 7.2 says:


In case of SRP-ID-number wrapping, the last
   SRP-ID-number before the wrapping MUST be explicitly acknowledged, to
   avoid a situation where SRP-ID-numbers remain unacknowledged after
   the wrap.  This means that the PCC may need to issue two PCUpd
   messages on detecting a wrap.

It should say:

In case of SRP-ID-number wrapping, the last
   SRP-ID-number before the wrapping MUST be explicitly acknowledged, to
   avoid a situation where SRP-ID-numbers remain unacknowledged after
   the wrap.  This means that the PCC may need to issue two PCRpt
   messages on detecting a wrap.

Notes:

incase of srp id wrap, once PCC detects it, PCC needs to issue PCRpt message not PCUpd message.
```

## Explanation

The original text incorrectly states that the PCC should issue PCUpd messages to acknowledge SRP-ID-number wrapping. The correction specifies that PCRpt messages should be used instead, which is consistent with the protocol's operation. This inconsistency would affect the handling of SRP-ID-number wrapping and could lead to unacknowledged SRP-ID-numbers.
