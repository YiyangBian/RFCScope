# Errata 4794 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid4794](https://www.rfc-editor.org/errata/eid4794)

```
Section 7.21.5 says:


   o  If the "when" statement is a child of an "augment" statement, then
      the context node is the augment's target node in the data tree, if
      the target node is a data node.  Otherwise, the context node is
      the closest ancestor node to the target node that is also a data
      node.  If no such node exists, the context node is the root node.
      The accessible tree is tentatively altered during the processing
      of the XPath expression by removing all instances (if any) of the
      nodes added by the "augment" statement.


It should say:

   o  If the "when" statement is a child of an "augment" statement, then
      the context node is the augment's target node in the data tree, if
      the target node is a data node, rpc, action or notification.
      Otherwise, the context node is the closest ancestor node to the
      target node that is also a data node, rpc, action or notification.
      If no such node exists, the context node is the root node. The
      accessible tree is tentatively altered during the processing of
      the XPath expression by removing all instances (if any) of the
      nodes added by the "augment" statement.


Notes:

If the target node of an "augment" is inside an rpc, action or notification, the context node also needs to be inside that rpc, action or notification. For example, if the target node is the "input" node of an action, the context node should be the action node, not the data node for which the action is defined as the original text implies. This is also in accordance with the definition of the accessible tree in Sec. 6.4.1.
```

## Explanation

The original description of context node selection for "when" statements within "augment" statements incorrectly limits the context node to only data nodes. The correction extends the selection to also include rpc, action, and notification nodes, making it consistent with the definition of the accessible tree and ensuring that "when" statements within "augment" statements function correctly when the target node is within an rpc, action, or notification.
