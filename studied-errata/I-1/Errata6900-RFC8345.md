# Errata 6900 - RFC 8345

- **RFC Title:** A YANG Data Model for Network Topologies
- **RFC Publication Date:** March 2018
- Link to original errata report: [rfc-editor.org/errata/eid6900](https://www.rfc-editor.org/errata/eid6900)

```
Section Appendix C says:


"network-id": "otn-hc",

It should say:

"network-id": "foo:otn-hc",

Notes:

This is to match the network-id type:

     typedef network-id {
       type inet:uri;
       description
         "Identifier for a network.  The precise structure of the
          network-id will be up to the implementation.  The identifier
          SHOULD be chosen such that the same network will always be
          identified through the same identifier, even if the data model
          is instantiated in separate datastores.  An implementation MAY
          choose to capture semantics in the identifier -- for example,
          to indicate the type of network.";
     }
```

## Explanation

The original example uses a simple string for network-id, which is inconsistent with the definition of the network-id type as an IETF URI.  The correction adds a prefix to make it a valid IETF URI, resolving the inconsistency.
