# Errata 7833 - RFC 9483

- **RFC Title:** Lightweight Certificate Management Protocol (CMP) Profile
- **RFC Publication Date:** November 2023
- Link to original errata report: [rfc-editor.org/errata/eid7833](https://www.rfc-editor.org/errata/eid7833)

```
Section 4.1.6 says:


-- MUST be 0 for recipientInfo type PasswordRecipientInfo

It should say:

-- MUST be 3 for recipientInfo type PasswordRecipientInfo

Notes:

It turns out that we make a mistake interpreting CMS RFC 5652 section 6.1 (https://datatracker.ietf.org/doc/html/rfc5652#section-6.1).

AFAICS, this was due to a misleadingly formatted condition in that section:

IF ((originatorInfo is present) AND
___(any version 2 attribute certificates are present)) OR
___(any RecipientInfo structures include pwri) OR
___(any RecipientInfo structures include ori)
THEN version is 3

where for clarity the indentation of the 2nd line should be one more character to the right:

IF ((originatorInfo is present) AND
____(any version 2 attribute certificates are present)) OR
___(any RecipientInfo structures include pwri) OR
___(any RecipientInfo structures include ori)
THEN version is 3

(I replaced leading space chars by '_' to make sure the indentation comes across.)

So this can also be seen as an editorial erratum of RFC 5652.
```

## Explanation

The original text specifies an incorrect value (0) for the version number when using PasswordRecipientInfo. The correction uses the correct value (3), which is consistent with RFC 5652. This inconsistency would lead to implementations generating incorrectly formatted CMP messages.
