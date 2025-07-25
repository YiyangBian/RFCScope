# Errata 7312 - RFC 8519

- **RFC Title:** YANG Data Model for Network Access Control Lists (ACLs)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid7312](https://www.rfc-editor.org/errata/eid7312)

```
Section A.1 says:


   The "example-newco-acl" module is an example of a company's
   proprietary model that augments the "ietf-acl" module.  It shows how
   to use 'augment' with an XML Path Language (XPath) expression to add
   additional match criteria, actions, and default actions for when no
   ACE matches are found.  All these are company proprietary extensions
   or system feature extensions.  "example-newco-acl" is just an
   example, and it is expected that vendors will create their own
   proprietary models.

It should say:

   The "example-newco-acl" module is an example of a company's
   proprietary model that augments the "ietf-access-control-list" module.  It shows how
   to use 'augment' with an XML Path Language (XPath) expression to add
   additional match criteria, actions, and default actions for when no
   ACE matches are found.  All these are company proprietary extensions
   or system feature extensions.  "example-newco-acl" is just an
   example, and it is expected that vendors will create their own
   proprietary models.

Notes:

There is no "ietf-acl" module in the document.
```

## Explanation

The original text refers to a non-existent module ("ietf-acl"). The correct module name is "ietf-access-control-list". This inconsistency could lead to errors in implementations that attempt to use the example module.
