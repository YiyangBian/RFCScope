# Errata 4673 - RFC 7420

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Management Information Base (MIB) Module
- **RFC Publication Date:** December 2014
- Link to original errata report: [rfc-editor.org/errata/eid4673](https://www.rfc-editor.org/errata/eid4673)

```
Section 4.1 says:


pcePcepSessState OBJECT-TYPE
       SYNTAX      INTEGER {
                      tcpPending(1),
                      openWait(2),
                      keepWait(3),
                      sessionUp(4)
                   }
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The current state of the session.

            The set of possible states excludes the idle state since
            entries do not exist in this table in the idle state."
       ::= { pcePcepSessEntry 3 }

It should say:

pcePcepSessState OBJECT-TYPE
       SYNTAX      INTEGER {
		      idle(0),
                      tcpPending(1),
                      openWait(2),
                      keepWait(3),
                      sessionUp(4)
                   }
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The current state of the session."
       ::= { pcePcepSessEntry 3 }	

Notes:

As per security consideration, if PCE needs to allow incomming connections from only known PCCs. 
Source addresses of PCCs are configured on PCE. If PCEP session on PCE goes down with configured PCCs. 
PCE needs to raise notification pcePcepSessDown (i.e. details mentioned below).
Issue is whiling sending the notification pcePcepSessDown, as session state (pcePcepSessState) defined in RFC doesn't include idle state.
I suggest to include idle(0) state for pcePcepSessState. 


   pcePcepSessDown NOTIFICATION-TYPE
       OBJECTS     {
                      pcePcepSessState,
                      pcePcepSessStateLastChange
                   }
       STATUS      current
       DESCRIPTION
           "This notification is sent when the value of
            pcePcepSessState leaves the sessionUp state."
       ::= { pcePcepNotifications 2 }
```

## Explanation

The original specification omits the "idle" state, while the description mentions it and the notification pcePcepSessDown requires it.  This inconsistency leads to incorrect behavior when transitioning to an idle state, as the MIB doesn't have a way to represent the state before the session is established.  The correction adds the "idle" state, resolving the inconsistency.
