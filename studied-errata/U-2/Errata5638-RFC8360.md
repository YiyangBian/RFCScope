# Errata 5638 - RFC 8360

- **RFC Title:** Resource Public Key Infrastructure (RPKI) Validation Reconsidered
- **RFC Publication Date:** April 2018
- Link to original errata report: [rfc-editor.org/errata/eid5638](https://www.rfc-editor.org/errata/eid5638)

```
Section 4.2.4.4 says:


   7.  Compute the VRS-IP and VRS-AS set values as indicated below:

       *  If the IP Address Delegation extension is present in
          certificate x and x=1, set the VRS-IP to the resources found
          in this extension.

       *  If the IP Address Delegation extension (...)

       *  If the IP Address Delegation extension (...)

       *  If the IP Address Delegation extension is present in
          certificate x and x=1, set the VRS-IP to the resources found
          in this extension.

       *  If the AS Identifier Delegation extension (...)

       *  If the AS Identifier Delegation extension (...)

It should say:

   7.  Compute the VRS-IP and VRS-AS set values as indicated below:

       *  If the IP Address Delegation extension is present in
          certificate x and x=1, set the VRS-IP to the resources found
          in this extension.

       *  If the IP Address Delegation extension (...)

       *  If the IP Address Delegation extension (...)

       *  If the AS Identifier Delegation extension is present in
          certificate x and x=1, set the VRS-AS to the resources found
          in this extension.

       *  If the AS Identifier Delegation extension (...)

       *  If the AS Identifier Delegation extension (...)

Notes:

There seems to be a copy-paste error.

There are two bullet points explaining the initialization of VRS-IP, and none explaining the initialization of VRS-AS.

All the evidence suggests that the two extensions (IP Address Delegation and AS Identifier Delegation) are meant to be handled similarly, so I believe that the last three bullet points are supposed to perfectly mirror the first three.
```

## Explanation

The original text contains duplicate bullet points for handling the IP Address Delegation extension and omits the corresponding handling for the AS Identifier Delegation extension. The correction replaces one set of duplicate bullet points with the correct handling for the AS Identifier Delegation extension, resolving the inconsistency.
