Below are a set of errata reports based on an analysis of Section A (“Guidance for the Use of QDCOUNT in the DNS Specification”) in RFC 9619, “In the DNS, QDCOUNT Is (Usually) One.” In our analysis we examined each sub‐section (A.1 through A.5) and identified areas where the text leaves its guidance open to multiple interpretations. In the following reports we include excerpts from the text, an explanation of the issue, and our reasoning as to why we believe these issues constitute underspecifications.

────────────────────────────
Errata Report 1: Ambiguity in the QDCOUNT Value for DNS NOTIFY Requests  
────────────────────────────
RFC: RFC 9619 “In the DNS, QDCOUNT Is (Usually) One”  
Section: A.2. OPCODE = 4 (NOTIFY)  

Excerpt from Section A.2:  
  "DNS Notify [RFC1996] also lacks a clearly defined range of values for QDCOUNT. Section 3.7 states that:  
    'A NOTIFY request has QDCOUNT>0'  
  However, all other text in the RFC discusses the <QNAME, QCLASS, QTYPE> tuple in the singular form."

Explanation:  
The text requires that a NOTIFY request must have a QDCOUNT greater than zero, which formally allows any value greater than 0. In contrast, the remainder of the discussion implies that there is a single question (i.e. one <QNAME, QCLASS, QTYPE> tuple). This contrasting guidance leaves it ambiguous whether implementations should accept—and, if so, how to interpret—messages that contain more than one question in a NOTIFY request. Without explicit normative language (such as “MUST equal 1”), different implementations might treat non‐singular question sections differently. This underspecification could lead to interoperability issues.

────────────────────────────
Errata Report 2: Unclear Normative Boundaries for Allowing QDCOUNT = 0 in OPCODE = 0 Queries  
────────────────────────────
RFC: RFC 9619 “In the DNS, QDCOUNT Is (Usually) One”  
Section: A.1. OPCODE = 0 (QUERY) and 1 (IQUERY)  

Excerpt from Section A.1:  
  "Section 4.1.2 ('Question section format') of [RFC1035] states the following:  
    'The section contains QDCOUNT (usually 1) entries'
  ...
  DNS Cookies (Section 5.4 of [RFC7873]) allow a client to receive a valid Server Cookie without sending a specific question by sending a request (QR = 0) with OPCODE = 0 and QDCOUNT = 0, with the resulting response also containing no question.
  The DNS Zone Transfer Protocol (Section 2.2 of [RFC5936]) allows an authoritative server to optionally send a response message ... with QDCOUNT = 0 in the second or subsequent message of a multi‐message response."

Explanation:  
RFC 9619’s normative update (in Section 4 of the document) clarifies that for messages with OPCODE = 0 (QUERY) the QDCOUNT value MUST not be greater than 1. Yet, Section A identifies two “exceptions” (DNS Cookies and AXFR responses) where a QDCOUNT of 0 is used. What is not made explicit is exactly under which circumstances a message with OPCODE = 0 and QDCOUNT = 0 is valid (that is, whether only the DNS Cookies and AXFR cases are acceptable) and how receivers are to distinguish these cases from erroneously formed messages. The discussion uses descriptive language (“allow” or “optionally send … with QDCOUNT = 0”) without setting clear normative boundaries. In the absence of a precise conditional statement, implementations might diverge in their treatment of queries with an empty question section, resulting in potential interoperability problems.

────────────────────────────
Errata Report 3: Lack of Guidance for QDCOUNT in OPCODE = 2 (STATUS) Messages  
────────────────────────────
RFC: RFC 9619 “In the DNS, QDCOUNT Is (Usually) One”  
Section: A.5. Conclusion  

Excerpt from Section A.5:  
  "OPCODE = 1 (IQUERY) is obsolete and OPCODE = 2 (STATUS) is not specified. OPCODE = 3 is reserved."

Explanation:  
The text explicitly notes that the allowed values of QDCOUNT for OPCODE = 2 (STATUS) messages are not specified. No additional guidance or reference is provided to resolve how a DNS entity should construct or process the QDCOUNT field in STATUS messages. This open-ended statement leaves implementers without a clear set of rules or expected behaviors for STATUS operations—including whether a STATUS message might ever include more than one question. The absence of normative language or referenced clarification results in a degree of underspecification that may lead to inconsistent implementations and interoperability issues.

────────────────────────────
These reports identify places where the RFC’s descriptive guidance is open to multiple interpretations. We recommend that the working group consider clarifying the normative requirements (or explicitly stating the intended restrictions) in these cases to avoid ambiguity in implementations.