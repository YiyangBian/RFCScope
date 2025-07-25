# Errata 4916 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid4916](https://www.rfc-editor.org/errata/eid4916)

```
Section 7.17. says:


If the target node is a container, list, case, input, output, or
notification node, the "container", "leaf", "list", "leaf-list",
"uses", and "choice" statements can be used within the "augment"
statement.

It should say:

If the target node is a container, list, case, input, output, or
notification node, the "anydata", "anyxml", "container", "leaf",
"list", "leaf-list", "uses", and "choice" statements can be used
within the "augment" statement.

Notes:

It was forgotten to mention "anydata" and "anyxml" as valid substatements in this case.
```

## Explanation

The original text omits "anydata" and "anyxml" statements from the list of allowed substatements within an "augment" statement when the target node is a container, list, case, input, output, or notification node.  This omission creates an inconsistency because "anydata" and "anyxml" are valid substatements in this context.  The correction adds these statements to the list, resolving the inconsistency.
