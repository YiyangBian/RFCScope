# Errata 7894 - RFC 8888

- **RFC Title:** RTP Control Protocol (RTCP) Feedback for Congestion Control
- **RFC Publication Date:** January 2021
- Link to original errata report: [rfc-editor.org/errata/eid7894](https://www.rfc-editor.org/errata/eid7894)

```
Section 3.1 says:


   RTCP Congestion Control Feedback Packets SHOULD include a report
   block for every active SSRC.

It should say:

   RTCP Congestion Control Feedback Packets SHOULD include a report
   block for every SSRC where packets have been received since the
   previous report was generated.

Notes:

The term "active" is ambiguous. Discussion on the avtcore mailing list indicates that this is the intended meaning.
```

## Explanation

The original text uses the term "active SSRC", which is ambiguous. The correction clarifies that a report block should be included for each SSRC where packets have been received since the last report, providing a more precise definition.
