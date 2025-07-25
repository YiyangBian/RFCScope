Below is an errata report for an underspecification that we identified while analyzing Section 4 (“Updates to RFC 1035”) of RFC 9619 (“In the DNS, QDCOUNT Is (Usually) One”).

---------------------------------------------------------------------
Errata Report for RFC 9619, “In the DNS, QDCOUNT Is (Usually) One”

Section: 4 (“Updates to RFC 1035”)

Excerpt from Section 4:
  “A DNS message with OPCODE = 0 MUST NOT include a QDCOUNT parameter whose value is greater than 1. It follows that the Question section of a DNS message with OPCODE = 0 MUST NOT contain more than one question.

  A DNS message with OPCODE = 0 and QDCOUNT > 1 MUST be treated as an incorrectly formatted message. The value of the RCODE parameter in the response message MUST be set to 1 (FORMERR).

  Middleboxes (e.g., firewalls) that process DNS messages in order to eliminate unwanted traffic SHOULD treat messages with OPCODE = 0 and QDCOUNT > 1 as malformed traffic and return a FORMERR response as described above. Such firewalls MUST NOT treat messages with OPCODE = 0 and QDCOUNT = 0 as malformed. See Section 4 of [RFC8906] for further guidance.”

Issue:
There is an underspecification regarding the normative processing of DNS messages with OPCODE = 0 and QDCOUNT = 0. While the section clearly disallows QDCOUNT values greater than 1 and mandates that messages with QDCOUNT > 1 be replied to with RCODE = FORMERR, it does not explicitly state how DNS servers or resolvers (as opposed to middleboxes) SHOULD handle DNS messages that have OPCODE = 0 and QDCOUNT = 0 in cases other than the specific deployments (e.g., DNS Cookies or multi-message AXFR responses) already mentioned in Appendix A. In other words, outside the guidance given to middleboxes, the document leaves open whether a QDCOUNT = 0 in a DNS query with OPCODE = 0 is acceptable or should be flagged and processed specially by name servers.

Explanation:
• The Introduction of RFC 9619 notes that, for DNS queries and responses (OPCODE = 0), the natural values of QDCOUNT are constrained to either 0 or 1. However, Section 4 “Updates to RFC 1035” only contains an explicit prohibition on QDCOUNT values greater than 1 and provides middlebox guidance for QDCOUNT = 0.
• There is no normative directive aimed at authoritative servers or recursive resolvers that addresses what action (if any) they should take when processing a DNS message with OPCODE = 0 and QDCOUNT = 0. RFC 7873 (DNS Cookies) and the DNS Zone Transfer Protocol (RFC 5936) do mention valid uses of QDCOUNT = 0, but Section 4 does not reconcile those uses with general query processing.
• This gap could lead to divergent interpretations. For example, one implementation might treat a QDCOUNT = 0 message as valid only in the context of DNS Cookies or zone transfers, while another might mistakenly drop or generate an error for any DNS query lacking a question—unless it also incorporates guidance from RFC 8906. The reference “See Section 4 of [RFC8906] for further guidance” helps middleboxes decide that such messages are not malformed, yet it does not tie down normative behavior for standard resolver/server implementations.

Reasoning:
The issue qualifies as an underspecification because a key processing behavior (i.e., how to handle OPCODE = 0 messages with QDCOUNT = 0) is left open to interpretation for non–middlebox implementations. Although the document implies that there are legitimate cases for QDCOUNT = 0 (as noted in the introduction and Appendix A), Section 4 does not provide a clear, normative directive ensuring uniform server behavior. This gap might result in interoperability issues if different implementations handle such messages inconsistently.

---------------------------------------------------------------------

This errata report identifies the gap in normative guidance for processing DNS messages with OPCODE = 0 and QDCOUNT = 0 (outside of the explicitly mentioned contexts) and explains why this omission represents an underspecification in RFC 9619.