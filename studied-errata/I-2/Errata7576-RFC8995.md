# Errata 7576 - RFC 8995

- **RFC Title:** Bootstrapping Remote Secure Key Infrastructure (BRSKI)
- **RFC Publication Date:** May 2021
- Link to original errata report: [rfc-editor.org/errata/eid7576](https://www.rfc-editor.org/errata/eid7576)

```
Section 4.3 says:


   objective-value = text       ; name of the (list of) supported
                                ; protocols: "EST-TLS" for RFC 7030.


It should say:

   objective-value = text       ; name of the supported protocol,
                                ; e.g., "EST-TLS" for RFC 7030.


Notes:

This objective does not support a list of supported protocols. 
The comment in the example might lead people to conclude they can do that.
```

## Explanation

The original description allows for multiple protocols, while the intended functionality supports only a single protocol. The ambiguity stems from the use of "(list of)" in the description, leading to multiple interpretations of the objective-value.
