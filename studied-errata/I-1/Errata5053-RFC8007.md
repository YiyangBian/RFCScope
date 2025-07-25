# Errata 5053 - RFC 8007

- **RFC Title:** Content Delivery Network Interconnection (CDNI) Control Interface / Triggers
- **RFC Publication Date:** December 2016
- Link to original errata report: [rfc-editor.org/errata/eid5053](https://www.rfc-editor.org/errata/eid5053)

```
Section 5.2.3 says:


| canceling |
| canceled  |

It should say:

| cancelling |
| cancelled  |


Notes:

In the final editing phase, I believe it was agreed that text would use the American spelling with 1 "l", but that the actual status strings would use 2 "l"s.  In sections 2.3, 4.3, 4.5, and Appendix A, the quoted status strings all use 2 "l"s.  The first column of the table in section 5.2.3 is providing the JSON string values, which should match the quoted status strings in sections 2.3, 4.3, 4.5, and Appendix A and have 2 "l"s.
```

## Explanation

The table in section 5.2.3 uses inconsistent spellings ("canceling", "canceled") compared to other sections (2.3, 4.3, 4.5, Appendix A) which use ("cancelling", "cancelled"). The inconsistent spelling affects the interpretation and implementation of the JSON status strings.
