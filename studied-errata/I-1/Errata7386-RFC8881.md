# Errata 7386 - RFC 8881

- **RFC Title:** Network File System (NFS) Version 4 Minor Version 1 Protocol
- **RFC Publication Date:** August 2020
- Link to original errata report: [rfc-editor.org/errata/eid7386](https://www.rfc-editor.org/errata/eid7386)

```
Section 18.46.3. says:


                                                             Operations
   other than SEQUENCE, BIND_CONN_TO_SESSION, EXCHANGE_ID,
   CREATE_SESSION, and DESTROY_SESSION, MUST NOT appear as the first
   operation in a COMPOUND.

It should say:

                                                             Operations
   other than SEQUENCE, BIND_CONN_TO_SESSION, EXCHANGE_ID,
   CREATE_SESSION, DESTROY_SESSION, and DESTROY_CLIENTID, MUST NOT
   appear as the first operation in a COMPOUND.

Notes:

Section 18.50.3. DESCRIPTION of DESTROY_CLIENTID says

"DESTROY_CLIENTID MAY be preceded with a SEQUENCE"

and also says

"If DESTROY_CLIENTID is not prefixed by SEQUENCE, it MUST be the only operation in the COMPOUND request"

which implies that DESTROY_CLIENTID can appear as the first (and the only) operation in a COMPOUND.
```

## Explanation

The original text incorrectly restricts the first operation in a COMPOUND to exclude DESTROY_CLIENTID, while section 18.50.3 allows it as the first (and only) operation. This discrepancy creates an inconsistency between the general rule and the specific exception for DESTROY_CLIENTID.
