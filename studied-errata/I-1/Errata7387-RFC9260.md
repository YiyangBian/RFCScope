# Errata 7387 - RFC 9260

- **RFC Title:** Stream Control Transmission Protocol
- **RFC Publication Date:** June 2022
- Link to original errata report: [rfc-editor.org/errata/eid7387](https://www.rfc-editor.org/errata/eid7387)

```
Section 5.2.4.1 says:


   Endpoint A                                          Endpoint Z
   <-------------- Association is established---------------------->
   Tag=Tag_A                                             Tag=Tag_Z
   <--------------------------------------------------------------->
   {A crashes and restarts}
   {app sets up an association with Z}
   (build TCB)
   INIT [I-Tag=Tag_A'
         & other info]  --------\
   (Start T1-init timer)         \
   (Enter COOKIE-WAIT state)      \---> (find an existing TCB,
                                         populate TieTags if needed,
                                         compose Cookie_Z with Tie-Tags
                                         and other info)
                                   /--- INIT ACK [Veri Tag=Tag_A',
                                  /               I-Tag=Tag_Z',
   (Cancel T1-init timer) <------/                Cookie_Z]
                                        (leave original TCB in place)
   COOKIE ECHO [Veri=Tag_Z',
                Cookie_Z]-------\
   (Start T1-init timer)         \
   (Enter COOKIE-ECHOED state)    \---> (Find existing association,
                                         Tie-Tags in Cookie_Z match
                                         Tie-Tags in TCB,
                                         Tags do not match, i.e.,
                                         case X X M M above,
                                         Announce Restart to ULP
                                         and reset association).
                                  /---- COOKIE ACK
   (Cancel T1-init timer, <------/
    Enter ESTABLISHED state)
   {app sends 1st user data; strm 0}
   DATA [TSN=Initial TSN_A
       Strm=0,Seq=0 & user data]--\
   (Start T3-rtx timer)            \
                                    \->
                                 /--- SACK [TSN Ack=init TSN_A,Block=0]
   (Cancel T3-rtx timer) <------/


It should say:

   Endpoint A                                          Endpoint Z
   <-------------- Association is established---------------------->
   Tag=Tag_A                                             Tag=Tag_Z
   <--------------------------------------------------------------->
   {A crashes and restarts}
   {app sets up an association with Z}
   (build TCB)
   INIT [I-Tag=Tag_A'
         & other info]  --------\
   (Start T1-init timer)         \
   (Enter COOKIE-WAIT state)      \---> (find an existing TCB,
                                         populate TieTags if needed,
                                         compose Cookie_Z with Tie-Tags
                                         and other info)
                                   /--- INIT ACK [Veri Tag=Tag_A',
                                  /               I-Tag=Tag_Z',
   (Cancel T1-init timer) <------/                Cookie_Z]
                                        (leave original TCB in place)
   COOKIE ECHO [Veri=Tag_Z',
                Cookie_Z]-------\
   (Start T1-cookie timer)       \
   (Enter COOKIE-ECHOED state)    \---> (Find existing association,
                                         Tie-Tags in Cookie_Z match
                                         Tie-Tags in TCB,
                                         Tags do not match, i.e.,
                                         case X X M M above,
                                         Announce Restart to ULP
                                         and reset association).
                                  /---- COOKIE ACK
   (Cancel T1-cookie timer, <----/
    Enter ESTABLISHED state)
   {app sends 1st user data; strm 0}
   DATA [TSN=Initial TSN_A
       Strm=0,Seq=0 & user data]--\
   (Start T3-rtx timer)            \
                                    \->
                                 /--- SACK [TSN Ack=init TSN_A,Block=0]
   (Cancel T3-rtx timer) <------/


Notes:

A packet containing an COOKIE-ECHO chunk is protected against loss by the T1-cookie timer, not the T1-init timer.
```

## Explanation

The original diagram uses the T1-init timer for COOKIE-ECHO packets, while the T1-cookie timer is the correct timer. This inconsistency needs to be corrected to reflect the intended behavior.
