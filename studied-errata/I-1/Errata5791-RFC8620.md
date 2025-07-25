# Errata 5791 - RFC 8620

- **RFC Title:** The JSON Meta Application Protocol (JMAP)
- **RFC Publication Date:** July 2019
- Link to original errata report: [rfc-editor.org/errata/eid5791](https://www.rfc-editor.org/errata/eid5791)

```
Section 2.1 says:


"capabilities": {
  "urn:ietf:params:jmap:core": {
    "maxSizeUpload": 50000000,
    "maxConcurrentUpload": 8,
    "maxSizeRequest": 10000000,
    "maxConcurrentRequest": 8,
    "maxCallsInRequest": 32,
    "maxObjectsInGet": 256,
    "maxObjectsInSet": 128,
    "collationAlgorithms": [
      "i;ascii-numeric",
      "i;ascii-casemap",
      "i;unicode-casemap"
    ]
  },
  "urn:ietf:params:jmap:mail": {}
  "urn:ietf:params:jmap:contacts": {},
  "https://example.com/apis/foobar": {
    "maxFoosFinangled": 42
  }
}

It should say:

"capabilities": {
  "urn:ietf:params:jmap:core": {
    "maxSizeUpload": 50000000,
    "maxConcurrentUpload": 8,
    "maxSizeRequest": 10000000,
    "maxConcurrentRequests": 8,
    "maxCallsInRequest": 32,
    "maxObjectsInGet": 256,
    "maxObjectsInSet": 128,
    "collationAlgorithms": [
      "i;ascii-numeric",
      "i;ascii-casemap",
      "i;unicode-casemap"
    ]
  },
  "urn:ietf:params:jmap:mail": {},
  "urn:ietf:params:jmap:contacts": {},
  "https://example.com/apis/foobar": {
    "maxFoosFinangled": 42
  }
}

Notes:

In the capabilities section of the example Session Resource response, "maxConcurrentRequest" should be "maxConcurrentRequests". 

In addition, the following line is missing a trailing comma:
  "urn:ietf:params:jmap:mail": {}
```

## Explanation

The example JSON uses the incorrect parameter name "maxConcurrentRequest" instead of the correct parameter name "maxConcurrentRequests". This inconsistency would cause issues when parsing and generating JMAP capability responses.
