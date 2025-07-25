# Errata 7250 - RFC 8446

- **RFC Title:** The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid7250](https://www.rfc-editor.org/errata/eid7250)

```
Section 4.6.1 says:


   The client MAY use this PSK for future handshakes by including the
   ticket value in the "pre_shared_key" extension in its ClientHello
   (Section 4.2.11).

It should say:

(to add)

  Where the client does not support session tickets, this extension MUST be ignored.

Notes:

I've seen a TLS implementation which doesn't implement session tickets.  That's fine, but the implementation doesn't *ignore* session tickets it receives.  Instead, it treats reception of the ticket as un recoverable error, and drops the TLS connection.

It's also worth adding a note to section 4.2 at the bottom of page 38.  To note that in general, f an extension isn't supported AND doesn't materially affect the TLS exchange, THEN it should be ignored.

i.e. there's nothing in the spec which mentions Postel's law "be conservative in what you send, be liberal in what you accept".  So implementors reading this document are free to do all kinds of odd things.

In addition, the text in Section 4.2 at the bottom of page 38 says:

"
      Designers
      and implementors should be aware of the fact that until the
      handshake has been authenticated, active attackers can modify
      messages and insert, remove, or replace extensions.
"

The implicit conclusion here is that an implementation receiving extensions must sanity check them.  e.g. an attacker adding an undefined / unknown extension should not cause the entire session to be torn down.

Paul Wouters(AD): Resolved but with the Corrected Text:

The client MAY use this PSK for future handshakes by including the ticket value in the "pre_shared_key" extension in its ClientHello (Section 4.2.11). Clients which receive a NewSessionTicket message but do not support resumption MUST silently ignore this message.
```

## Explanation

The original specification is unclear about how clients that do not support session tickets should handle the presence of the "pre_shared_key" extension. The corrected text adds a statement clarifying that clients without session ticket support MUST silently ignore the extension. This omission in the original specification leads to ambiguity in implementation.
