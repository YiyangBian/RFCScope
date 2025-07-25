# Errata 7657 - RFC 8006

- **RFC Title:** Content Delivery Network Interconnection (CDNI) Metadata
- **RFC Publication Date:** December 2016
- Link to original errata report: [rfc-editor.org/errata/eid7657](https://www.rfc-editor.org/errata/eid7657)

```
Section 6.10 says:


   {
     "metadata": [
       {
         "generic-metadata-type": "MI.TimeWindowACL",
         "generic-metadata-value": {
           "times": [
             "windows": [
               {
                 "start": "1213948800",
                 "end": "1478047392"
               }
             ],
             "action": "allow"
           ]
         }
       }
     ]
   }

It should say:

   {
     "metadata": [
       {
         "generic-metadata-type": "MI.TimeWindowACL",
         "generic-metadata-value": {
           "times": [
              {
                "windows": [
                  {
                    "start": 1213948800,
                    "end": 1478047392
                  }
                ],
                "action": "allow"
              }
           ]
         }
       }
     ]
   }

Notes:

1. The "times" property of  the TimeWindowACL object has an array of TimeWindowRule type, so I changed it to "windows" and "action" are contained in braces.
2. The "start" and "end" property of the TimeWindow object have a Time type, which is an alias of Integer. So I changed their values ("1213948800", "1478047392") to Integer (1213948800, 1478047392).
```

## Explanation

The erratum corrects a structural error in the example JSON provided in Section 6.10 of RFC 8006.  The original example has an incorrect nesting of the "windows" and "action" properties within the "times" array. The correction shows the correct nesting, directly impacting how the JSON would be interpreted and parsed during implementation.  This inconsistency makes the original example unimplementable without additional clarification.
