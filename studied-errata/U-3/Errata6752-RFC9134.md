# Errata 6752 - RFC 9134

- **RFC Title:** RTP Payload Format for ISO/IEC 21122 (JPEG XS)
- **RFC Publication Date:** October 2021
- Link to original errata report: [rfc-editor.org/errata/eid6752](https://www.rfc-editor.org/errata/eid6752)

```
Section 4.2 says:


As specified in [RFC3550] and [RFC4175], the RTP timestamp
designates the sampling instant of the first octet of the video
frame to which the RTP packet belongs.  Packets SHALL NOT include
data from multiple video frames, and all packets belonging to the
same video frame SHALL have the same timestamp.  Several
successive RTP packets will consequently have equal timestamps if
they belong to the same video frame (that is until the marker bit
is set to 1, marking the last packet of the video frame), and the
timestamp is only increased when a new video frame begins.

It should say:

As specified in [RFC3550] and [RFC4175], the RTP timestamp
designates the sampling instant of the first octet of the video
frame/field to which the RTP packet belongs.  Packets SHALL NOT include
data from multiple video frames/fields, and all packets belonging to the
same video frame/field SHALL have the same timestamp.  Several
successive RTP packets will consequently have equal timestamps if
they belong to the same video frame/field (that is until the marker bit
is set to 1, marking the last packet of the video frame/field), and the
timestamp is only increased when a new video frame/field begins.

Notes:

This RFC follows RFC4175 (and also SMPTE2110) for timestamping RTP packets. The intent has always been to have unique timestamps per progressive video frame and/or per interlaced video field (two fields of a frame MUST be allowed to have different timestamps). This is correctly reflected by the marker bit (M) that is used to indicate the last packet of a frame/field (which is correctly explained in this RFC). However, the accompanied text about the timestamp in section 4.2 does not properly formulate this for the interlaced mode case (it was an editorial oversight), which can cause confusion to implementers of this RFC.
```

## Explanation

The original text is unclear about whether the RTP timestamp applies to video frames or fields. The correction clarifies that it applies to both, thus addressing the ambiguity and ensuring that implementations correctly handle both progressive and interlaced video.
