# Errata 7876 - RFC 9537

- **RFC Title:** Redacted Fields in the Registration Data Access Protocol (RDAP) Response
- **RFC Publication Date:** March 2024
- Link to original errata report: [rfc-editor.org/errata/eid7876](https://www.rfc-editor.org/errata/eid7876)

```
Section 4.2 says:


Figure 13:

  {
    "rdapConformance": [
      "rdap_level_0"
    ],
    "domainSearchResults":[
      {
        "objectClassName": "domain",
        "handle": "ABC121",
        "ldhName": "example1.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example1.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"related",
            "href":"https://example.com/rdap/domain/example1.com",
            "type":"application/rdap+json"
          }
        ]
      },
      {
        "objectClassName": "domain",
        "handle": "ABC122",
        "ldhName": "example2.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example2.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"related",
            "href":"https://example.com/rdap/domain/example2.com",
            "type":"application/rdap+json"
          }
        ]
      }
    ]
  }

Figure 14:

  {
    "rdapConformance": [
      "rdap_level_0",
      "redacted"
    ],
    "domainSearchResults":[
      {
        "objectClassName": "domain",
        "ldhName": "example1.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example1.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"related",
            "href":"https://example.com/rdap/domain/example1.com",
            "type":"application/rdap+json"
          }
        ],
        "redacted": [
          {
            "name": {
              "type": "Registry Domain ID"
            },
            "prePath": "$.domainSearchResults[0].handle",
            "pathLang": "jsonpath",
            "method": "removal",
            "reason": {
              "type": "Server policy"
            }
          }
        ]
      },
      {
        "objectClassName": "domain",
        "ldhName": "example2.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example2.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"related",
            "href":"https://example.com/rdap/domain/example2.com",
            "type":"application/rdap+json"
          }
        ],
        "redacted": [
          {
            "name": {
              "description": "Registry Domain ID"
            },
            "prePath": "$.domainSearchResults[1].handle",
            "pathLang": "jsonpath",
            "method": "removal",
            "reason": {
              "description": "Server policy"
            }
          }
        ]
      }
    ]
  }

It should say:

Figure 13:

  {
    "rdapConformance": [
      "rdap_level_0"
    ],
    "domainSearchResults":[
      {
        "objectClassName": "domain",
        "handle": "ABC121",
        "ldhName": "example1.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example1.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"related",
            "href":"https://example.net/rdap/v1/domain/example1.com",
            "type":"application/rdap+json"
          }
        ]
      },
      {
        "objectClassName": "domain",
        "handle": "ABC122",
        "ldhName": "example2.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example2.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"related",
            "href":"https://example.net/rdap/v1/domain/example2.com",
            "type":"application/rdap+json"
          }
        ]
      }
    ]
  }

Figure 14:

  {
    "rdapConformance": [
      "rdap_level_0",
      "redacted"
    ],
    "domainSearchResults":[
      {
        "objectClassName": "domain",
        "ldhName": "example1.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example1.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example1.com",
            "rel":"related",
            "href":"https://example.net/rdap/v1/domain/example1.com",
            "type":"application/rdap+json"
          }
        ],
        "redacted": [
          {
            "name": {
              "type": "Registry Domain ID"
            },
            "prePath": "$.domainSearchResults[0].handle",
            "pathLang": "jsonpath",
            "method": "removal",
            "reason": {
              "type": "Server policy"
            }
          }
        ]
      },
      {
        "objectClassName": "domain",
        "ldhName": "example2.com",
        "links":[
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"self",
            "href":"https://example.com/rdap/domain/example2.com",
            "type":"application/rdap+json"
          },
          {
            "value":"https://example.com/rdap/domain/example2.com",
            "rel":"related",
            "href":"https://example.net/rdap/v1/domain/example2.com",
            "type":"application/rdap+json"
          }
        ],
        "redacted": [
          {
            "name": {
              "description": "Registry Domain ID"
            },
            "prePath": "$.domainSearchResults[1].handle",
            "pathLang": "jsonpath",
            "method": "removal",
            "reason": {
              "description": "Server policy"
            }
          }
        ]
      }
    ]
  }

Notes:

Noticed that the "self" and "related" links in Figure 13 and Figure 14 examples have the same "href" value. From RFC 9083: A "related" link relation MUST NOT include an "href" URI that is the same as the "self" link relation "href" URI to reduce the risk of infinite client processing loops. (The new "href" values for the "related" links are per James Gould's earlier suggestion.)
```

## Explanation

The example in Figure 13 uses the same "href" value for both "self" and "related" links, which is inconsistent with the requirement in RFC 9083 that these URIs must be different to prevent infinite client processing loops.
