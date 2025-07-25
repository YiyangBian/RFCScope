# Errata 5540 - RFC 7728

- **RFC Title:** RTP Stream Pause and Resume
- **RFC Publication Date:** February 2016
- Link to original errata report: [rfc-editor.org/errata/eid5540](https://www.rfc-editor.org/errata/eid5540)

```
Section 8.2.  PAUSED says:


   PAUSED SHALL contain a fixed-length 32-bit parameter at the start of
   the Type Specific field with the extended RTP sequence number of the
   last RTP packet sent before the RTP stream was paused, in the same
   format as the extended highest sequence number received
   (Section 6.4.1 of [RFC3550]).

It should say:

   PAUSED SHALL contain a fixed-length 32-bit parameter at the start of
   the Type Specific field with the extended RTP sequence number of the
   last RTP packet sent before the RTP stream was paused, in the same
   format as the extended highest sequence number received
   (Section 6.4.1 of [RFC3550]), or, if no packet has been sent, the
   value one less than the sequence number that will be chosen for the
   next packet sent (modulo 2^32).

Notes:

The paragraph leaves the value of the parameter undefined when the stream is paused before any data has been sent.
```

## Explanation

The original specification does not define the value of the 32-bit parameter in the PAUSED message when no RTP packets have been sent before pausing.  This under-specification leads to ambiguity in implementations and potential interoperability issues. The correction clarifies the value to be used in this scenario.
