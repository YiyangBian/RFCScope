# Errata 7381 - RFC 9073

- **RFC Title:** Event Publishing Extensions to iCalendar
- **RFC Publication Date:** August 2021
- Link to original errata report: [rfc-editor.org/errata/eid7381](https://www.rfc-editor.org/errata/eid7381)

```
Section 7.2 says:


   Format Definition:  This component is defined by the following
      notation:

      locationc    = "BEGIN" ":" "VLOCATION" CRLF
                     locprop
                     "END" ":" "VLOCATION" CRLF

      locprop      = *(
                     ;
                     ; The following are REQUIRED
                     ; but MUST NOT occur more than once.
                     ;
                     uid /
                     ;
                     ; The following are OPTIONAL
                     ; but MUST NOT occur more than once.
                     ;
                     description / geo / loctype / name
                     ;
                     ; The following are OPTIONAL
                     ; and MAY occur more than once.
                     ;
                     sdataprop / iana-prop
                  )

It should say:

   Format Definition:  This component is defined by the following
      notation:

      locationc    = "BEGIN" ":" "VLOCATION" CRLF
                     locprop
                     "END" ":" "VLOCATION" CRLF

      locprop      = *(
                     ;
                     ; The following are REQUIRED
                     ; but MUST NOT occur more than once.
                     ;
                     uid /
                     ;
                     ; The following are OPTIONAL
                     ; but MUST NOT occur more than once.
                     ;
                     description / geo / loctype / name / url /
                     ;
                     ; The following are OPTIONAL
                     ; and MAY occur more than once.
                     ;
                     sdataprop / iana-prop
                  )

Notes:

The url property is missing or the specification clahes with RFC 9074, where in section 8.2 in the example it reads:

   BEGIN:VLOCATION
   UID:123456-abcdef-98765432
   NAME:Office
   URL:geo:40.443,-79.945;u=10
   END:VLOCATION

Either "geo" was intended as a geo uri as defined in RFC 5870 (instead of the geographic position from RFC 2445/5545) or "url" should be added as a valid property (or RFC 9074 is wrong).

--

Verifier's notes: A "/" was missing after "name" and was added after "url" in this same errata.
```

## Explanation

The original specification omits the "url" property from the list of allowed properties in the "locprop" definition, which is inconsistent with the example provided in RFC 9074 and the general allowance for URL properties in iCalendar.
