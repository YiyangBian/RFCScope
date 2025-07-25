# Errata 8166 - RFC 8888

- **RFC Title:** RTP Control Protocol (RTCP) Feedback for Congestion Control
- **RFC Publication Date:** January 2021
- Link to original errata report: [rfc-editor.org/errata/eid8166](https://www.rfc-editor.org/errata/eid8166)

```
Section 3.1 says:


         Following this, the report block contains a
   16-bit packet metric block for each RTP packet that has a sequence
   number in the range begin_seq to begin_seq+num_reports inclusive
   (calculated using arithmetic modulo 65536 to account for possible
   sequence number wrap-around).

It should say:

         Following this, the report block contains a
   16-bit packet metric block for each RTP packet that has a sequence
   number in the range begin_seq up to, but not including,
   begin_seq+num_reports
   (calculated using arithmetic modulo 65536 to account for possible
   sequence number wrap-around).

Notes:

The text can be read as the range being [begin_seq, begin_seq+num_reports].

If "begin_seq" is taken as the first sequence number you are reporting on, the original text means that you would have to have num_reports be 0 when you are reporting on a single packet. This seems very strange.

Alternatively, if "begin_seq" is taken as the sequence number before the one you are reporting on, the num_reports is consistent, but you are then reporting on the range <begin_seq, begin_seq+num_reports], which also seems strange.

The suggested clarification would report on the sequence [begin_seq, begin_seq + num_reports>, which seems like the most natural interpretation.

This is also consistent with the format of an empty report, which is explicit that begin_seq is the sequence number of the last RTP packet received.
```

## Explanation

The meaning of num_reports intended later in the text contradicts with the fact that the range is inclusive.
