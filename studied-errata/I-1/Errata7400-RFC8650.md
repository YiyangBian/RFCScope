# Errata 7400 - RFC 8650

- **RFC Title:** Dynamic Subscription to YANG Events and Datastores over RESTCONF
- **RFC Publication Date:** November 2019
- Link to original errata report: [rfc-editor.org/errata/eid7400](https://www.rfc-editor.org/errata/eid7400)

```
Section Appendix A.3 says:


   POST /restconf/operations
        /ietf-subscribed-notifications:establish-subscription
   {
      "ietf-subscribed-notifications:input": {
         "stream": "NETCONF",
         "stream-xpath-filter":
           "/ietf-vrrp:vrrp-protocol-error-event[
             protocol-error-reason='checksum-error']/",
      }
   }

       Figure 16: Establishing a Subscription Error Reason via XPath

...

   POST /restconf/operations
        /ietf-subscribed-notifications:modify-subscription
   {
      "ietf-subscribed-notifications:input": {
         "stream": "NETCONF",
         "stream-subtree-filter": {
           "/ietf-vrrp:vrrp-protocol-error-event" : {}
         }
      }
   }
                Figure 17: Example "modify-subscription" RPC

It should say:

   POST /restconf/operations
        /ietf-subscribed-notifications:establish-subscription

   {
      "ietf-subscribed-notifications:input": {
         "stream": "NETCONF",
         "stream-xpath-filter":
           "/ietf-vrrp:vrrp-protocol-error-event[
             protocol-error-reason='checksum-error']/"
      }
   }

       Figure 16: Establishing a Subscription Error Reason via XPath

...

   POST /restconf/operations
        /ietf-subscribed-notifications:modify-subscription

   {
      "ietf-subscribed-notifications:input": {
         "stream": "NETCONF",
         "stream-subtree-filter": {
           "/ietf-vrrp:vrrp-protocol-error-event" : {}
         }
      }
   }
                Figure 17: Example "modify-subscription" RPC


Notes:

* There is a missing CRLF in both figures as per RFC9112:

--
  HTTP-message   = start-line CRLF
                   *( field-line CRLF )
                   CRLF
                   [ message-body ]
--

* The last item in the JSON of figure 16 includes a trailing "," while it shouldn't.
```

## Explanation

The errata report points out missing CRLF in the HTTP messages and a trailing comma in the JSON of Figure 16, both of which are stylistic issues rather than errors that affect the implementation. The corrected figures include the CRLF and remove the trailing comma.
