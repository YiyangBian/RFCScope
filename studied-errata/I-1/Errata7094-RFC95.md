# Errata 7094 - RFC 95

- **RFC Title:** JSON Responses for the Registration Data Access Protocol (RDAP)
- **RFC Publication Date:** June 2021
- Link to original errata report: [rfc-editor.org/errata/eid7094](https://www.rfc-editor.org/errata/eid7094)

```
Section 2.1 says:


If The Registry of the Moon desires to express information not found
in this specification, it might select "lunarNIC" as its identifying
prefix and insert, as an example, the member named
"lunarNIC_beforeOneSmallStep" to signify registrations occurring
before the first moon landing and the member named
"lunarNIC_harshMistressNotes" that contains other descriptive text.

Consider the following JSON response with JSON names, some of which
should be ignored by clients without knowledge of their meaning.

{
  "handle" : "ABC123",
  "lunarNIC_beforeOneSmallStep" : "TRUE THAT!",
  "remarks" :
  [
    {
      "description" :
      [
        "She sells sea shells down by the sea shore.",
        "Originally written by Terry Sullivan."
      ]
    }
  ],
  "lunarNIC_harshMistressNotes" :
  [
    "In space,",
    "nobody can hear you scream."
  ]
}
Figure 2

It should say:

If The Registry of the Moon desires to express information not found
in this specification, it might select "lunarNIC_level_0" as its
identifying prefix and insert, as an example, the member named
"lunarNIC_level_0_beforeOneSmallStep" to signify registrations occurring
before the first moon landing and the member named
"lunarNIC_level_0_harshMistressNotes" that contains other descriptive
text.

Consider the following JSON response with JSON names, some of which
should be ignored by clients without knowledge of their meaning.

{
  "handle" : "ABC123",
  "lunarNIC_level_0_beforeOneSmallStep" : "TRUE THAT!",
  "remarks" :
  [
    {
      "description" :
      [
        "She sells sea shells down by the sea shore.",
        "Originally written by Terry Sullivan."
      ]
    }
  ],
  "lunarNIC_level_0_harshMistressNotes" :
  [
    "In space,",
    "nobody can hear you scream."
  ]
}
Figure 2

Notes:

The original text uses the string identifier "lunarNIC" as the prefix for an example extension. This is inconsistent with the example given in Section 4.1, where "lunarNIC_level_0" is used as an example of a registered identifier for an RDAP extension. This inconsistency can lead implementers to believe that the registered identifier and the extension prefix can be inconsistent, when the intent of the specification is that they should be consistent. This inconsistency can cause significant misunderstanding of the technical specification and might result in faulty implementations if not corrected. Changing the examples in Section 2.1 aligns the text with the example in Section 4.1, demonstrating that the extension prefix and the registered identifier should be one and the same.
```

## Explanation

The original example uses the string identifier "lunarNIC" as the prefix for an extension, which is inconsistent with the example in Section 4.1, where "lunarNIC_level_0" is used.  The correction uses the consistent prefix, ensuring that examples accurately reflect the intended use of extension prefixes.
