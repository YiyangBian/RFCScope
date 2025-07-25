# Errata 6473 - RFC 8040

- **RFC Title:** RESTCONF Protocol
- **RFC Publication Date:** January 2017
- Link to original errata report: [rfc-editor.org/errata/eid6473](https://www.rfc-editor.org/errata/eid6473)

```
Section B.3.2 says:


   Example 3: depth=3

   To limit the depth level to the target resource plus two child
   resource layers, the value "3" is used.

      GET /restconf/data/example-jukebox:jukebox?depth=3 HTTP/1.1
      Host: example.com
      Accept: application/yang-data+json

   The server might respond as follows:

      HTTP/1.1 200 OK
      Date: Thu, 26 Jan 2017 20:56:30 GMT
      Server: example-server
      Cache-Control: no-cache
      Content-Type: application/yang-data+json

      {
        "example-jukebox:jukebox" : {
          "library" : {
            "artist" : {}
          },
          "playlist" : [
            {
              "name" : "Foo-One",
              "description" : "example playlist 1",
              "song" : {}
            }
          ],
          "player" : {
            "gap" : 0.5
          }
        }
      }

It should say:

   Example 3: depth=3

   To limit the depth level to the target resource plus two child
   resource layers, the value "3" is used.

      GET /restconf/data/example-jukebox:jukebox?depth=3 HTTP/1.1
      Host: example.com
      Accept: application/yang-data+json

   The server might respond as follows:

      HTTP/1.1 200 OK
      Date: Thu, 26 Jan 2017 20:56:30 GMT
      Server: example-server
      Cache-Control: no-cache
      Content-Type: application/yang-data+json

      {
        "example-jukebox:jukebox" : {
          "library" : {
            "artist" : []
          },
          "playlist" : [
            {
              "name" : "Foo-One",
              "description" : "example playlist 1",
              "song" : []
            }
          ],
          "player" : {
            "gap" : 0.5
          }
        }
      }

Notes:

"artist" and "song" are defined as list.  Therefore, according to RFC 7951, they should be encoded as array instead of object.
```

## Explanation

The response example in Section B.3.2 incorrectly represents "artist" and "song" as empty objects when they should be empty arrays according to RFC 7951, given that they are defined as lists in the YANG model.  This inconsistency misrepresents how list types should be encoded in JSON responses, potentially causing incorrect implementation of RESTCONF data serialization and deserialization.
