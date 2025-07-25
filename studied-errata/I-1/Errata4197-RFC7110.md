# Errata 4197 - RFC 7110

- **RFC Title:** Return Path Specified Label Switched Path (LSP) Ping
- **RFC Publication Date:** January 2014
- Link to original errata report: [rfc-editor.org/errata/eid4197](https://www.rfc-editor.org/errata/eid4197)

```
Section 4 says:


The Reply Path TLV contains one or more nested sub-TLVs that can be
used


It should say:

The Reply Path TLV contains zero or more nested sub-TLVs that can be
used

Notes:

As section 4.2 correctly states, the Reply Path TLV can contain zero
sub-TLVs; this brings section 4 inline.
```

## Explanation

The erratum points out an inconsistency between Section 4 and Section 4.2 regarding the number of nested sub-TLVs in the Reply Path TLV.  Section 4 incorrectly states "one or more", while Section 4.2 correctly states "zero or more."  This impacts implementation because an implementation relying on Section 4's description would incorrectly reject valid messages with zero sub-TLVs.
