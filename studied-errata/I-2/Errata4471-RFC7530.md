# Errata 4471 - RFC 7530

- **RFC Title:** Network File System (NFS) Version 4 Protocol
- **RFC Publication Date:** March 2015
- Link to original errata report: [rfc-editor.org/errata/eid4471](https://www.rfc-editor.org/errata/eid4471)

```
Section 16.10.4. says:


   In the case that the lock is denied, the owner, offset, and length of
   a conflicting lock are returned.

It should say:

   In the case that the lock is denied, the owner, offset, length, and
   type of a conflicting lock are returned.

Notes:

The locktype in LOCK4denied is not specified for the LOCK operation.  See 16.11.4. for similar wording for LOCKT.
```

## Explanation

The original description omits the lock type in the LOCK4denied response when a lock is denied. This is inconsistent with the description of LOCKT in section 16.11.4, which includes the lock type. The omission leads to incomplete information in the response, making it inconsistent and affecting implementations that depend on having complete information about the conflicting lock.
