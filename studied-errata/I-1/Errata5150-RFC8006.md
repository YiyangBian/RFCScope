# Errata 5150 - RFC 8006

- **RFC Title:** Content Delivery Network Interconnection (CDNI) Metadata
- **RFC Publication Date:** December 2016
- Link to original errata report: [rfc-editor.org/errata/eid5150](https://www.rfc-editor.org/errata/eid5150)

```
Section 6.10 says:


         "generic-metadata-type": "MI.SourceMetadata",
         "generic-metadata-value": {
           "sources": [
             {
               "endpoint": ["acq1.ucdn.example"],
               "protocol": "http/1.1"
             },
             {
               "endpoint": ["acq2.ucdn.example"],
               "protocol": "http/1.1"
             }
           ]
         }


It should say:

         "generic-metadata-type": "MI.SourceMetadata",
         "generic-metadata-value": {
           "sources": [
             {
               "endpoints": ["acq1.ucdn.example"],
               "protocol": "http/1.1"
             },
             {
               "endpoints": ["acq2.ucdn.example"],
               "protocol": "http/1.1"
             }
           ]
         }


Notes:

The SourceMetadata object contains an array of "sources", which in turn contains an array of "endpoints".  The example in section 6.10 uses the singular "endpoint" instead of the plural "endpoints".  The examples in sections 4.2.1 and 4.2.1.1 correctly use the plural "endpoints" for the property name, as defined in section 4.2.1.1.
```

## Explanation

The erratum highlights an inconsistency in the example provided in Section 6.10 of RFC 8006.  The example uses the singular "endpoint" while other sections (4.2.1 and 4.2.1.1) correctly use the plural "endpoints". This inconsistency directly relates to implementation as it affects how the SourceMetadata object should be structured and parsed, causing ambiguity in the implementation.  Therefore, it is classified as INCONSISTENT.
