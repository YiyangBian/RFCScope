# Errata 8256 - RFC 9639

- **RFC Title:** Free Lossless Audio Codec (FLAC)
- **RFC Publication Date:** December 2024
- Link to original errata report: [rfc-editor.org/errata/eid8256](https://www.rfc-editor.org/errata/eid8256)

```
Section 8.2 says:


   SSAAAAAASSBBBBBBSSCCCCCC
   ^   ^   ^   ^   ^   ^
   |   |   |   |   |  Bits of 2nd sample of 1st channel
   |   |   |   |  Sign extension bits of 2nd sample of 2nd channel
   |   |   |  Bits of 1st sample of 2nd channel
   |   |  Sign extension bits of 1st sample of 2nd channel
   |  Bits of 1st sample of 1st channel
   Sign extension bits of 1st sample of 1st channel

It should say:

   SSAAAAAASSBBBBBBSSCCCCCC
   ^   ^   ^   ^   ^   ^
   |   |   |   |   |  Bits of 2nd sample of 1st channel
   |   |   |   |  Sign extension bits of 2nd sample of 1st channel
   |   |   |  Bits of 1st sample of 2nd channel
   |   |  Sign extension bits of 1st sample of 2nd channel
   |  Bits of 1st sample of 1st channel
   Sign extension bits of 1st sample of 1st channel

Notes:

One of the diagram labels appears to contradict the sign-extension + interleaving method described in the preceding paragraph.
```

## Explanation

The diagram incorrectly labels the sign extension bits for the second sample of the second channel. The correction uses the correct channel for the sign extension bits, aligning the diagram with the described interleaving and sign-extension method.
