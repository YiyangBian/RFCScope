# Errata 5055 - RFC 7162

- **RFC Title:** IMAP Extensions: Quick Flag Changes Resynchronization (CONDSTORE) and Quick Mailbox Resynchronization (QRESYNC)
- **RFC Publication Date:** May 2014
- Link to original errata report: [rfc-editor.org/errata/eid5055](https://www.rfc-editor.org/errata/eid5055)

```
Section 3.1.2.1 says:


   C: A142 SELECT INBOX
   S: * 172 EXISTS
   S: * 1 RECENT
   S: * OK [UNSEEN 12] Message 12 is first unseen
   S: * OK [UIDVALIDITY 3857529045] UIDs valid
   S: * OK [UIDNEXT 4392] Predicted next UID
   S: * FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
   S: * OK [PERMANENTFLAGS (\Deleted \Seen \*)] Limited
   S: * OK [HIGHESTMODSEQ 715194045007]
   S: A142 OK [READ-WRITE] SELECT completed

It should say:

   C: A142 SELECT INBOX
   S: * 172 EXISTS
   S: * 1 RECENT
   S: * OK [UNSEEN 12] Message 12 is first unseen
   S: * OK [UIDVALIDITY 3857529045] UIDs valid
   S: * OK [UIDNEXT 4392] Predicted next UID
   S: * FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
   S: * OK [PERMANENTFLAGS (\Deleted \Seen \*)] Limited
   S: * OK [HIGHESTMODSEQ 715194045007] Ok
                                       ^^^
   S: A142 OK [READ-WRITE] SELECT completed

Notes:

RFC 7162 purports to extend RFC 3501 by adding the HIGHESTMODSEQ value as an option for the resp-text-code syntax. However, RFC 3501 only uses resp-text-code in the resp-text ABNF production, in which case it is always followed by a single space ("SP") and the "text" non-terminal, which expands to "1*TEXT-CHAR", as in non-empty text. As such, having a response code without any human-readable text suffix is illegal per the RFC 3501 spec, and the examples should be updated to be correct.
```

## Explanation

The erratum points out that the example in Section 3.1.2.1 violates RFC 3501 by omitting the human-readable text after HIGHESTMODSEQ response code.  This is inconsistent with the requirements of RFC 3501 and could result in implementations rejecting valid responses or producing invalid ones, thus directly affecting interoperability.
