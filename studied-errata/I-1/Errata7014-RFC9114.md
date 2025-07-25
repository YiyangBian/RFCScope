# Errata 7014 - RFC 9114

- **RFC Title:** HTTP/3
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7014](https://www.rfc-editor.org/errata/eid7014)

```
Section 4.3.1 says:


   ":path":  Contains the path and query parts of the target URI (the
      "path-absolute" production and optionally a ? character (ASCII
      0x3f) followed by the "query" production; see Sections 3.3 and 3.4
      of [URI].

It should say:

   ":path":  Contains the path and query parts of the target URI (the
      "absolute-path" production and optionally a ? character (ASCII
      0x3f) followed by the "query" production; see Section 4.1 of
      [HTTP] and Section 3.4 of [URI].

Notes:

There is a conflict between RFC 9114 and RFCs 9110,9112,9113. RFC 9114 disallows paths that start with "//" whereas the others allow them. Research seems to indicate that this was not intentional. More details on the mailing list discussion: https://lists.w3.org/Archives/Public/ietf-http-wg/2022JulSep/0014.html
```

## Explanation

The description of the ":path" header field in Section 4.3.1 uses the term "path-absolute", which conflicts with the usage in other RFCs (RFCs 9110, 9112, 9113) and the intended behavior.  The correct term should be "absolute-path", aligning with the definitions in those RFCs. This inconsistency affects interoperability, as implementations might interpret the path differently based on which RFC they adhere to more strictly.
