# Errata 4874 - RFC 7181

- **RFC Title:** The Optimized Link State Routing Protocol Version 2
- **RFC Publication Date:** April 2014
- Link to original errata report: [rfc-editor.org/errata/eid4874](https://www.rfc-editor.org/errata/eid4874)

```
Section 17.1 says:


   If the router changes its originator address, then:

   1.  If there is no Originator Tuple with:

       *  O_orig_addr = old originator address

       then create an Originator Tuple with:

       *  O_orig_addr := old originator address

       The Originator Tuple (existing or new) with:

       *  O_orig_addr = new originator address

       is then modified as follows:

       *  O_time := current time + O_HOLD_TIME


It should say:

   If the router changes its originator address, then:

   1.  If there is an Originator Tuple with:

       *  O_orig_addr = old originator address

       then modify it as follows:

       *  O_orig_addr := new originator address
       *  O_time := current time + O_HOLD_TIME

       otherwise create an Originator Tuple with:

       *  O_orig_addr := new originator address
       *  O_time := current time + O_HOLD_TIME


Notes:

At the time of the modification Originator Tuple with O_orig_addr = new originator address does not yet exist.

===
The Corrected text reflects consultation with the WG.
```

## Explanation

The original description contradicts itself regarding the handling of Originator Tuples when the originator address changes. It states that a new tuple should be created if one with the old address does not exist, but then proceeds to modify a tuple with the new address (which wouldn't yet exist). The correction provides a consistent and unambiguous algorithm by correctly ordering the creation and modification of the Originator Tuple.  This inconsistency would lead to incorrect management of Originator Tuples, affecting the routing protocol's operation.
