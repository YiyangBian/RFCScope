# Errata 5807 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid5807](https://www.rfc-editor.org/errata/eid5807)

```
Section 7.21.5. says:


   o  If the "when" statement is a child of a "uses", "choice", or
      "case" statement, then the context node is the closest ancestor
      node to the node with the "when" statement that is also a data
      node.  If no such node exists, the context node is the root node.
      The accessible tree is tentatively altered during the processing
      of the XPath expression by removing all instances (if any) of the
      nodes added by the "uses", "choice", or "case" statement.

It should say:

   o  If the "when" statement is a child of a "uses", "choice", or
      "case" statement, then the context node is the closest ancestor
      node to the node with the "when" statement that is also a data
      node, rpc, action or notification.  If no such node exists, the
      context node is the root node. The accessible tree is tentatively
      altered during the processing of the XPath expression by removing
      all instances (if any) of the nodes added by the "uses",
      "choice", or "case" statement.

Notes:

Similar to verified errata 4794 (https://www.rfc-editor.org/errata/eid4794) but covers the "uses", "choice" and "case" corner case (instead of "augment"). If the node for which the "when" statement is defined is within an rpc, action or notification, the context node also needs to be inside that rpc, action or notification. There are published IETF modules, which rely on this to be true, such as "ietf-netconf-nmda@2019-01-07" in RFC8526 (https://tools.ietf.org/html/rfc8526) at schema node id "/ncds:get-data/ncds:input/ncds:origin-filters". Original text assigns the context node to the root node, if no data node ancestor is found. "rpc", "action" and "notification" are not data nodes and are represented by nodes that are descendants of the root node, as described in Section 6.4.1.
```

## Explanation

The original description of context node selection for "when" statements within "uses", "choice", or "case" statements incorrectly limits the context node to only data nodes. The correction extends the selection to also include rpc, action, and notification nodes, ensuring that "when" statements within "uses", "choice", or "case" statements function correctly when the target node is within an rpc, action, or notification.
