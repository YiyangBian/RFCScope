# Errata 4664 - RFC 7233

- **RFC Title:** Hypertext Transfer Protocol (HTTP/1.1): Range Requests
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4664](https://www.rfc-editor.org/errata/eid4664)

```
Section 4.4 says:


The 416 (Range Not Satisfiable) status code indicates that none of
the ranges in the request's Range header field (Section 3.1) overlap
the current extent of the selected resource or that the set of ranges
requested has been rejected due to invalid ranges or an excessive
request of small or overlapping ranges.

It should say:

The 416 (Range Not Satisfiable) status code indicates that none of
the ranges in the request's Range header field (Section 3.1) overlap
the current extent of the selected representation or that the set of
ranges requested has been rejected due to invalid ranges or an excessive
request of small or overlapping ranges.

Notes:

The overlap may depend on the representation, not only the resource, as is the case with byte ranges.
```

## Explanation

The erratum points out that using the term "resource" in Section 4.4 is inconsistent with the concept of representations.  The 416 status code's applicability depends on the representation's extent, not solely on the resource's extent.  This is particularly relevant for byte ranges, which are representation-specific.  The inconsistency affects how servers implement the 416 response, potentially causing incorrect responses in cases where multiple representations exist for the same resource.
