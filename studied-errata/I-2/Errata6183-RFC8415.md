# Errata 6183 - RFC 8415

- **RFC Title:** Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
- **RFC Publication Date:** November 2018
- Link to original errata report: [rfc-editor.org/errata/eid6183](https://www.rfc-editor.org/errata/eid6183)

```
Section 18.3.8 says:


   After all the addresses have been processed, the server generates a
   Reply message by setting the "msg-type" field to REPLY and copying
   the transaction ID from the Decline message into the "transaction-id"
   field.  The client includes a Status Code option (see Section 21.13)
   with the value Success, a Server Identifier option (see Section 21.3)
   with the server's DUID, and a Client Identifier option (see
   Section 21.2) with the client's DUID

It should say:

   After all the addresses have been processed, the server generates a
   Reply message by setting the "msg-type" field to REPLY and copying
   the transaction ID from the Decline message into the "transaction-id"
   field.  The server includes a Status Code option (see Section 21.13)
   with the value Success, a Server Identifier option (see Section 21.3)
   with the server's DUID, and a Client Identifier option (see
   Section 21.2) with the client's DUID

Notes:

The corrected text replaces "client" with "server".

I would like to thank Timothy Winters <tim@qacafe.com> for confirming that this is a bug in the specification.
```

## Explanation

The original text incorrectly attributes the inclusion of options in the Reply message to the client. The correction assigns this responsibility to the server, which is consistent with the DHCPv6 protocol. This inconsistency would affect implementations that incorrectly handle option inclusion in the Reply message.
