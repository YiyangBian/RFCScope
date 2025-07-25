# Errata 6716 - RFC 8995

- **RFC Title:** Bootstrapping Remote Secure Key Infrastructure (BRSKI)
- **RFC Publication Date:** May 2021
- Link to original errata report: [rfc-editor.org/errata/eid6716](https://www.rfc-editor.org/errata/eid6716)

```
Section 5.8.3 says:


A registrar MAY be configured to ignore (i.e., override
the above policy) the history of the device, but it is RECOMMENDED
that this only be configured if hardware-assisted (i.e., Transport
Performance Metrics (TPM) anchored) Network Endpoint Assessment (NEA)
[RFC5209] is supported.

It should say:

A registrar MAY be configured to ignore (i.e., override
the above policy) the history of the device, but it is RECOMMENDED
that this only be configured if hardware-assisted (i.e., Trusted 
Platform Module (TPM) anchored) Network Endpoint Assessment (NEA)
 [RFC5209] is supported.

Notes:

The logical expansion of 'TPM' in this parenthetical example is the Trusted Platform Module.
```

## Explanation

The logical expansion of 'TPM' in this parenthetical example is the Trusted Platform Module.
