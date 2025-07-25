# Errata 4016 - RFC 7210

- **RFC Title:** Database of Long-Lived Symmetric Cryptographic Keys
- **RFC Publication Date:** April 2014
- Link to original errata report: [rfc-editor.org/errata/eid4016](https://www.rfc-editor.org/errata/eid4016)

```
Section 2 says:


      SendLifetimeStart
         The SendLifetimeStart field specifies the earliest date and
         time in Coordinated Universal Time (UTC) at which this key
         should be considered for use when sending traffic.  The format
         is YYYYMMDDHHSSZ, where four digits specify the year, two
         digits specify the month, two digits specify the day, two
         digits specify the hour, two digits specify the minute, and two
         digits specify the second.  The "Z" is included as a clear
         indication that the time is in UTC.

      SendLifeTimeEnd
         The SendLifeTimeEnd field specifies the latest date and time at
         which this key should be considered for use when sending
         traffic.  The format is the same as the SendLifetimeStart
         field.

      AcceptLifeTimeStart
         The AcceptLifeTimeStart field specifies the earliest date and
         time in Coordinated Universal Time (UTC) at which this key
         should be considered for use when processing received traffic.
         The format is YYYYMMDDHHSSZ, where four digits specify the
         year, two digits specify the month, two digits specify the day,
         two digits specify the hour, two digits specify the minute, and
         two digits specify the second.  The "Z" is included as a clear
         indication that the time is in UTC.


It should say:

      SendLifetimeStart
         The SendLifetimeStart field specifies the earliest date and
         time in Coordinated Universal Time (UTC) at which this key
         should be considered for use when sending traffic.  The format
         is YYYYmmddHHMMSSZ, where four digits specify the year, two
         digits specify the month, two digits specify the day, two
         digits specify the hour, two digits specify the minute, and two
         digits specify the second.  The "Z" is included as a clear
         indication that the time is in UTC.

      SendLifeTimeEnd
         The SendLifeTimeEnd field specifies the latest date and time at
         which this key should be considered for use when sending
         traffic.  The format is the same as the SendLifetimeStart
         field.

      AcceptLifeTimeStart
         The AcceptLifeTimeStart field specifies the earliest date and
         time in Coordinated Universal Time (UTC) at which this key
         should be considered for use when processing received traffic.
         The format is YYYYmmddHHMMSSZ, where four digits specify the
         year, two digits specify the month, two digits specify the day,
         two digits specify the hour, two digits specify the minute, and
         two digits specify the second.  The "Z" is included as a clear
         indication that the time is in UTC.


Notes:

The date and time format in the original document omits minute even though the descriptive text indicates it should be included.
```

## Explanation

The errata corrects the specified format for the date and time fields. The original specification omits the minutes field, which is inconsistent with the description. This inconsistency could lead to incorrect implementation and interpretation of the timestamps, directly affecting the functionality of the key management system.
