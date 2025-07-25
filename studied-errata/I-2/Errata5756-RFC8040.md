# Errata 5756 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid5756](https://www.rfc-editor.org/errata/eid5756)

```
Section 8 says:


  module ietf-system {
    leaf system-reset {
      type empty;
    }
  }


It should say:

  module ietf-system {
    leaf system-restart {
      type empty;
    }
  }


Notes:

The section on page 84 discusses the "system-restart" RPC from RFC 7317, but the conceptual example has "system-reset".  Fix: s/system-reset/system-restart/.
```

## Explanation

The example YANG module in Section 8 uses the name "system-reset" for an RPC operation, which is inconsistent with the name "system-restart" discussed and referenced earlier in the RFC from RFC 7317.  This inconsistency could lead to confusion and incorrect implementation of the system restart functionality.
