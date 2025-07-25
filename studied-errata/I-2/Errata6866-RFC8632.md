# Errata 6866 - RFC 8632

- **RFC Title:** A YANG Data Model for Alarm Management
- **RFC Publication Date:** September 2019
- Link to original errata report: [rfc-editor.org/errata/eid6866](https://www.rfc-editor.org/errata/eid6866)

```
Section 6 says:


      container older-than {
        presence "Age specification";
        description
          "Matches the 'last-status-change' leaf in the alarm.";
        choice age-spec {


It should say:

      container older-than {
        presence "Age specification";
        description
          "Matches the 'last-changed' leaf in the alarm.";
        choice age-spec {


Notes:

There is no last-status-change leaf in alarm (and it seems there never was).

See also https://mailarchive.ietf.org/arch/msg/ccamp/wmCgk0DQq0lG6S_e59W-MKW8EOQ/
```

## Explanation

The original text refers to a non-existent leaf ("last-status-change"). The correction uses the correct leaf name ("last-changed"), resolving the inconsistency.  This inconsistency would affect implementations that try to use this container to filter alarms.
