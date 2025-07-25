# Errata 5054 - RFC 8007

- **RFC Title:** Content Delivery Network Interconnection (CDNI) Control Interface / Triggers
- **RFC Publication Date:** December 2016
- Link to original errata report: [rfc-editor.org/errata/eid5054](https://www.rfc-editor.org/errata/eid5054)

```
Section 5.2.7 says:


| ecanceled    |

It should say:

| ecancelled   |



Notes:

In the final editing phase, I believe it was agreed that text would use the American spelling with 1 "l", but that the status strings would use 2 "l"s.  This should apply to the error codes as well.  The first column of the table in section 5.2.7 is providing the Error Code values, which like the status code strings in sections 2.3, 4.3, 4.5, 5.2.3, and Appendix A, should have 2 "l"s.  Note: The IANA registry has the error code as "ecancelled" with 2 "l"s.  http://www.iana.org/assignments/cdni-parameters/cdni-parameters.xhtml#error-codes

Note: This errata also applies to Appendix A.
```

## Explanation

The table in section 5.2.7 uses inconsistent spelling for the error code compared to other sections of the document and the IANA registry. The corrected table uses the double-l spelling that matches the rest of the document and the IANA registry, resolving the inconsistency.
