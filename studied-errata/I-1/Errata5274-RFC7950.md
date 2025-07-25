# Errata 5274 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid5274](https://www.rfc-editor.org/errata/eid5274)

```
Section 7.16.3 says:


   A corresponding XML instance example of the complete notification:

     <notification
       xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
       <eventTime>2008-07-08T00:01:00Z</eventTime>
       <event xmlns="urn:example:event">
         <event-class>fault</event-class>
         <reporting-entity>
           /ex:interface[ex:name='Ethernet0']
         </reporting-entity>
         <severity>major</severity>
       </event>
     </notification>

It should say:

   A corresponding XML instance example of the complete notification
   follows.  This example reports an event for an interface from the
   "example-foo" module defined in Section 13.1.1.

     <notification
       xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
       <eventTime>2008-07-08T00:01:00Z</eventTime>
       <event xmlns="urn:example:event">
         <event-class>fault</event-class>
         <reporting-entity xmlns:ex="urn:example:foo">
           /ex:interface[ex:name='Ethernet0']
         </reporting-entity>
         <severity>major</severity>
       </event>
     </notification>


Notes:

The "ex" prefix is not declared.  The "example-foo" module in 13.1.1 is the only module in the draft that matches the given instance-identifier.  An alternative fix would be to use a different module and a matching instance-identifier.
```

## Explanation

The original XML example lacks a namespace declaration for the "ex" prefix, leading to an invalid XML instance. The correction adds the necessary namespace declaration, making the example consistent and valid. This inconsistency would cause issues for implementations that validate the XML instance against the YANG module.
