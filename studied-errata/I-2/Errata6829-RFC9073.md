# Errata 6829 - RFC 9073

- **RFC Title:** Event Publishing Extensions to iCalendar
- **RFC Publication Date:** August 2021
- Link to original errata report: [rfc-editor.org/errata/eid6829](https://www.rfc-editor.org/errata/eid6829)

```
Section 7.1 says:


      partprop     = *(
                     ;
                     ; The following are REQUIRED
                     ; but MUST NOT occur more than once.
                     ;
                     participanttype / uid /
                     ;
                     ; The following are OPTIONAL
                     ; but MUST NOT occur more than once.
                     ;
                     calendaraddress / created / description / dtstamp /
                     geo / last-mod / priority / seq /
                     status / summary / url /
                     ;
                     ; The following are OPTIONAL
                     ; and MAY occur more than once.
                     ;
                     attach / categories / comment
                     contact / location / rstatus / related /
                     resources / strucloc / strucres /
                     styleddescription / sdataprop / iana-prop
                     ;
                     )


It should say:

      partprop     = *(
                     ;
                     ; The following are REQUIRED
                     ; but MUST NOT occur more than once.
                     ;
                     participanttype / uid /
                     ;
                     ; The following are OPTIONAL
                     ; but MUST NOT occur more than once.
                     ;
                     calendaraddress / created / description / dtstamp /
                     geo / last-mod / priority / seq /
                     status / summary / url /
                     ;
                     ; The following are OPTIONAL
                     ; and MAY occur more than once.
                     ;
                     attach / categories / comment
                     contact / location / rstatus / related /
                     resources /
                     styleddescription / sdataprop / iana-prop
                     ;
                     )


Notes:

'structloc' and 'structres' are not defined in this document.  These are leftover artifacts from a draft version of this specification and were replaced by 'locationc' and 'resourcec'
```

## Explanation

The original specification includes properties ("strucloc" and "structres") that are not defined in the document.  The removal of these undefined properties resolves the inconsistency.
