# Errata 7703 - RFC 7854

- **RFC Title:** BGP Monitoring Protocol (BMP)
- **RFC Publication Date:** June 2016
- Link to original errata report: [rfc-editor.org/errata/eid7703](https://www.rfc-editor.org/errata/eid7703)

```
Section 4.2 says:


      *  The L flag, if set to 1, indicates that the message reflects
         the post-policy Adj-RIB-In (i.e., its path attributes reflect
         the application of inbound policy).  It is set to 0 if the
         message reflects the pre-policy Adj-RIB-In.  Locally sourced
         routes also carry an L flag of 1.  See Section 5 for further
         detail.  This flag has no significance when used with route
         mirroring messages (Section 4.7).

It should say:

      *  The L flag, if set to 1, indicates that the message reflects
         the post-policy Adj-RIB-In (i.e., its path attributes reflect
         the application of inbound policy).  It is set to 0 if the
         message reflects the pre-policy Adj-RIB-In.  Locally sourced
         routes also carry an L flag of 1.  See Section 5 for further
         detail.  This flag has significance only when used with Route
         Monitoring messages.

Notes:

The L flag is used to indicate whether the route monitoring update reflects Adj-RIB-In pre-policy or post-policy (RFC 7854), or Adj-RIB-Out pre-policy or post-policy (RFC 8671). It does not apply to any message other than the Route Monitoring message.
```

## Explanation

The original description of the L flag incorrectly states that it has no significance for route mirroring messages. The corrected description clarifies that the L flag is only significant for Route Monitoring messages.  This inconsistency between the original description and the actual usage of the L flag could lead to misinterpretations and incorrect implementations.
