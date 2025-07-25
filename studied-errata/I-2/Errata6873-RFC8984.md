# Errata 6873 - RFC 8984

- **RFC Title:** JSCalendar: A JSON Representation of Calendar Data
- **RFC Publication Date:** July 2021
- Link to original errata report: [rfc-editor.org/errata/eid6873](https://www.rfc-editor.org/errata/eid6873)

```
Section 4.3.2. says:


Identifies the time zone of the main JSCalendar object, of which this
JSCalendar object is a recurrence instance.  This property MUST be
set if the "recurrenceId" property is set.  It MUST NOT be set if the
"recurrenceId" property is not set.

It should say:

Identifies the time zone of the main JSCalendar object, of which this
JSCalendar object is a recurrence instance.  It MUST NOT be set if the
"recurrenceId" property is not set.

Notes:

A recurrence instance may be in floating time, in which case the value of the "recurrenceIdTimeZone" property is null. As null is the default value of the "recurrenceIdTimeZone" property, it is NOT required to be set if "recurrenceId" is set.
```

## Explanation

The original description creates ambiguity by requiring the "recurrenceIdTimeZone" property to be set when "recurrenceId" is set, while it could be null, which is the default value.  The correction removes the requirement, making the specification clearer.
