# Errata 6158 - RFC 7483

- **RFC Title:** JSON Responses for the Registration Data Access Protocol (RDAP)
- **RFC Publication Date:** March 2015
- Link to original errata report: [rfc-editor.org/errata/eid6158](https://www.rfc-editor.org/errata/eid6158)

```
Section 10.2.3 says:


Description: The object instance was transferred from one registrant to another.

It should say:

Description: The object instance was transferred from one registrar to another.

Notes:

I believe the corrected text is what was intended for this particular registry value, and is what is being implemented by operators today. Registrant-to-registrant transfers are also possible, but they're not performed using EPP and are not logged as an event action. The text in the RFC should be changed and the description of the action in the IANA registry should also be changed.
```

## Explanation

The original description uses the term "registrant", which is incorrect in the context of EPP object transfers. The correction uses the term "registrar", which aligns with the intended meaning of object transfers performed using EPP and is consistent with current implementations. The inconsistency would lead to misinterpretations of the event action.
