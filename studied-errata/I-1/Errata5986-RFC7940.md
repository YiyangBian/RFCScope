# Errata 5986 - RFC 7940

- **RFC Title:** Representing Label Generation Rulesets Using XML
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid5986](https://www.rfc-editor.org/errata/eid5986)

```
Section 6.3.1 says:


   A simple rule to match a label where all characters are members of
   some class called "preferred-codepoint":          

       <rule name="preferred-label">
           <start />
           <class by-ref="preferred-codepoint" count="1"/>
           <end />
       </rule>

It should say:

   A simple rule to match a label where all characters are members of
   some class called "preferred-codepoint":           

       <rule name="preferred-label">
           <start />
           <class by-ref="preferred-codepoint" count="1+"/>
           <end />
       </rule>

Notes:

Currently the value for count is 1, which means that the rule will match a label composed of only one char.
However, since the rule is supposed to match a label composed one or more chars, the value ofr count must be "1+" .
```

## Explanation

The original specification uses "count="1", which only matches labels with one character, while the description indicates that it should match labels with one or more characters.  The correction uses "count="1+", resolving the inconsistency. This inconsistency would lead to implementations incorrectly matching labels based on the length.
