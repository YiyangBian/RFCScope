# Errata 7986 - RFC 95

- **RFC Title:** JSON Responses for the Registration Data Access Protocol (RDAP)
- **RFC Publication Date:** June 2021
- Link to original errata report: [rfc-editor.org/errata/eid7986](https://www.rfc-editor.org/errata/eid7986)

```
Section 9 says:


The following is an elided example of an entity truncated data.

{
  "objectClassName" : "entity",
  "handle" : "ANENTITY",
  "roles" : [ "registrant" ],
  ...
  "entities" :
  [
    {
      "objectClassName" : "entity",
      "handle": "ANEMBEDDEDENTITY",
      "roles" : [ "technical" ],
      ...
    },
    ...
  ],
  "networks" :
  [
    ...
  ],
  ...
  "remarks" :
  [
    {
      "title" : "Data Policy",
      "type" : "object truncated due to unexplainable reason",
      "description" :
      [
        "Some of the data in this object has been removed."
      ],
      "links" :
      [
        {
          "value" : "https://example.net/help",
          "rel" : "alternate",
          "type" : "text/html",
          "href" : "https://www.example.com/data_policy.html"
        }
      ]
    }
  ]
}


It should say:

The following is an elided example of an entity truncated data.

{
  "rdapConformance" :
  [
    "rdap_level_0"
  ],
  "objectClassName" : "entity",
  "handle" : "ANENTITY",
  "roles" : [ "registrant" ],
  ...
  "entities" :
  [
    {
      "objectClassName" : "entity",
      "handle": "ANEMBEDDEDENTITY",
      "roles" : [ "technical" ],
      ...
    },
    ...
  ],
  "networks" :
  [
    ...
  ],
  ...
  "remarks" :
  [
    {
      "title" : "Data Policy",
      "type" : "object truncated due to unexplainable reason",
      "description" :
      [
        "Some of the data in this object has been removed."
      ],
      "links" :
      [
        {
          "value" : "https://example.net/help",
          "rel" : "alternate",
          "type" : "text/html",
          "href" : "https://www.example.com/data_policy.html"
        }
      ]
    }
  ]
}


Notes:

RFC 9083 4.1 states that the rdapConformance data structure MUST appear in the topmost JSON object of RDAP responses. The example error response provided in Figure 33 should include the rdapConformance property but does not.
```

## Explanation

The example JSON response in Section 9 omits the required "rdapConformance" property as specified in Section 4.1, creating an inconsistency between the example and the specification.
