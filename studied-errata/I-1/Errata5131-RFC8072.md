# Errata 5131 - RFC 8072

- **RFC Title:** YANG Patch Media Type
- **RFC Publication Date:** February 2017
- Link to original errata report: [rfc-editor.org/errata/eid5131](https://www.rfc-editor.org/errata/eid5131)

```
Section 2.2 says:


Regarding section 2.2 of RFC 8072, the third paragraph states:


                                       ... If the edit does not identify
    any existing resource instance and the operation for the edit is not
    "create", then the request MUST NOT be processed and a "404 Not
    Found" error response MUST be sent by the server.

It should say:

                                      ... If the edit does not identify
   any existing resource instance and the operation for the edit is
   "delete" or "move" then the request MUST NOT be processed and a
   "404 Not Found" error response MUST be sent by the server.

Notes:

As per the second paragraph of section 2.2 of RFC 8072, the operations are expected to mirror the semantics of the "operation" attribute described in Section 7.2 of [RFC6241].

The spec also doesn't specify what happens if it is a "create" operation and the resource already exists.  It should probably also state that "400 Bad Request" is returned.
```

## Explanation

The original specification states that a 404 error MUST be returned if an edit does not identify an existing resource instance and the operation is not "create". However, this is inconsistent with the semantics of RFC 6241, which specifies that a 404 error should only be returned for "delete" or "move" operations. The corrected specification aligns with RFC 6241, specifying that a 404 error MUST be returned only for "delete" or "move" operations and that a 400 error is returned for a create operation if the resource already exists.
