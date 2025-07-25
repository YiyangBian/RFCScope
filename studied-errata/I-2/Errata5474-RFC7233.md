# Errata 5474 - RFC 7233

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Range Requests
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid5474](https://www.rfc-editor.org/errata/eid5474)

```
Section 4.4. says:


For byte ranges, failing to overlap the current extent means that the
   first-byte-pos of all of the byte-range-spec values were greater than
   the current length of the selected representation.

It should say:

For byte ranges, failing to overlap the current extent means that the
   first-byte-pos of all of the byte-range-spec values were greater than
   or equal to the current length of the selected representation.
   ^^^^^^^^^^^

Notes:

If the length of the representation is 500 bytes, then the range of the entire representation is 0-499. Then a range starting at byte position 500 fails to overlap the representation.
```

## Explanation

The erratum points out an inconsistency in the description of byte range overlap in Section 4.4. The original description incorrectly states that only ranges with `first-byte-pos` values strictly greater than the representation length fail to overlap.  A range starting exactly at the length should also be considered non-overlapping. This error directly impacts the implementation of range request handling, potentially causing servers to incorrectly accept or reject valid or invalid ranges.
