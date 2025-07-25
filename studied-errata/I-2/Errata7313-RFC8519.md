# Errata 7313 - RFC 8519

- **RFC Title:** YANG Data Model for Network Access Control Lists (ACLs)
- **RFC Publication Date:** March 2019
- Link to original errata report: [rfc-editor.org/errata/eid7313](https://www.rfc-editor.org/errata/eid7313)

```
Section A.1 says:


   The following figure is the tree diagram of example-newco-acl.  In
   this example, /ietf-acl:acls/ietf-acl:acl/ietf-acl:aces/ietf-acl:ace/
   ietf-acl:matches are augmented with two new choices: protocol-
   payload-choice and metadata.  The protocol-payload-choice uses a
   grouping with an enumeration of all supported protocol values.
   Metadata matches apply to fields associated with the packet, that are
   not in the packet header, such as overall packet length.  In another
   example, /ietf-acl:acls/ietf-acl:acl/ietf-acl:aces/ietf-acl:ace/
   ietf-acl:actions are augmented with a new choice of actions.

It should say:

   The following figure is the tree diagram of example-newco-acl.  In
   this example, /acl:acls/acl:acl/acl:aces/acl:ace/acl:matches
   are augmented with two new choices: protocol-payload-choice and
   metadata.  The protocol-payload-choice uses a
   grouping with an enumeration of all supported protocol values.
   Metadata matches apply to fields associated with the packet, that are
   not in the packet header, such as overall packet length.  In another
   example, /acl:acls/acl:acl/acl:aces/acl:ace/acl:actions 
   are augmented with a new choice of actions.

Notes:

The prefix is "acl" not "ietf-acl"

==
module ietf-access-control-list {
  yang-version 1.1;
  namespace "urn:ietf:params:xml:ns:yang:ietf-access-control-list";
  prefix acl;
  ...
==
```

## Explanation

The original text uses the prefix "ietf-acl", which is incorrect; the correct prefix is "acl".  This inconsistency affects the XPath expressions used for augmentation, making them invalid and impacting the implementation.
