# Errata 3945 - RFC 7139

- **RFC Title:** GMPLS Signaling Extensions for Control of Evolving G.709 Optical Transport Networks
- **RFC Publication Date:** March 2014
- Link to original errata report: [rfc-editor.org/errata/eid3945](https://www.rfc-editor.org/errata/eid3945)

```
Section 7 says:


For the ingress node, a Path message with SE style SHOULD also be
sent for decreasing the ODUflex bandwidth.

It should say:

For the ingress node, a Path message with SE style MUST also be
sent for decreasing the ODUflex bandwidth.

Notes:

Section 7 requires that Shared Explicit (SE) MUST be used at the beginning when creating a resizable ODUflex connection. Thus, the SE style MUST also be used when signaling for bandwidth increase or decrease.  The increase procedure mandates the use of SE style; however, the decrease procedure uses SHOULD.  The decrease procedure should also make the SE signaling mandatory.

This change, that looks to be a change of substance, has been verified with the authors to be an editorial issue that was caused by not keeping the paragraphs in synch.
```

## Explanation

The erratum corrects a discrepancy in the use of SHOULD versus MUST for signaling bandwidth decrease.  The original text uses SHOULD, which is weaker and leaves room for non-compliant implementations. The correction to MUST ensures consistent and unambiguous behavior.  The inconsistency is between the requirements for increasing bandwidth (MUST use SE style) and decreasing bandwidth (SHOULD use SE style), which directly affects implementation correctness.
