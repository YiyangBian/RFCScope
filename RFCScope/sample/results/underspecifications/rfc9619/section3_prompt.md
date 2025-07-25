Let us analyze section 3 of RFC 9619. All references made by section 3 have also been included below.

# RFC 9619: In the DNS, QDCOUNT Is (Usually) One

## 1. Introduction

   The DNS protocol [RFC1034] [RFC1035] includes a parameter QDCOUNT in
   the DNS message header whose value is specified to mean the number of
   questions in the Question section of a DNS message.

   In a general sense, it seems perfectly plausible for the QDCOUNT
   parameter, an unsigned 16-bit value, to take a considerable range of
   values.  However, in the specific case of messages that encode DNS
   queries and responses (messages with OPCODE = 0), there are other
   limitations inherent in the protocol that constrain values of QDCOUNT
   to be either 0 or 1.  In particular, several parameters specified for
   DNS response messages such as AA and RCODE have no defined meaning
   when the message contains multiple queries as there is no way to
   signal which question those parameters relate to.

   In this document, we briefly survey the existing written DNS
   specification; provide a description of the semantic and practical
   requirements for DNS queries that naturally constrain the allowable
   values of QDCOUNT; and update the DNS base specification to clarify
   the allowable values of the QDCODE parameter in the specific case of
   DNS messages with OPCODE = 0.

## 2. Terminology Used in This Document

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.

## 3. QDCOUNT Is (Usually) One

   A brief summary of the guidance provided in the existing DNS
   specification ([RFC1035] and many other documents) for the use of
   QDCOUNT can be found in Appendix A .  While the specification is clear
   in many cases, there is some ambiguity in the specific case of OPCODE
   = 0, which this document aims to eliminate.

## 4. Updates to RFC 1035

   A DNS message with OPCODE = 0 MUST NOT include a QDCOUNT parameter
   whose value is greater than 1.  It follows that the Question section
   of a DNS message with OPCODE = 0 MUST NOT contain more than one
   question.

   A DNS message with OPCODE = 0 and QDCOUNT > 1 MUST be treated as an
   incorrectly formatted message.  The value of the RCODE parameter in
   the response message MUST be set to 1 (FORMERR).

   Middleboxes (e.g., firewalls) that process DNS messages in order to
   eliminate unwanted traffic SHOULD treat messages with OPCODE = 0 and
   QDCOUNT > 1 as malformed traffic and return a FORMERR response as
   described above.  Such firewalls MUST NOT treat messages with OPCODE
   = 0 and QDCOUNT = 0 as malformed.  See Section 4 of [RFC8906] for
   further guidance.

## 5. Security Considerations

   This document clarifies the DNS specification [RFC1035] and aims to
   improve interoperability between different DNS implementations.  In
   general, the elimination of ambiguity seems well-aligned with
   security hygiene.

## 6. IANA Considerations

   This document has no IANA actions.

## 7. References





### 7.1. Normative References

   [RFC1034]  Mockapetris, P., "Domain names - concepts and facilities",
              STD 13, RFC 1034, DOI 10.17487/RFC1034, November 1987,
              <https://www.rfc-editor.org/info/rfc1034>.

   [RFC1035]  Mockapetris, P., "Domain names - implementation and
              specification", STD 13, RFC 1035, DOI 10.17487/RFC1035,
              November 1987, <https://www.rfc-editor.org/info/rfc1035>.

   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119,
              DOI 10.17487/RFC2119, March 1997,
              <https://www.rfc-editor.org/info/rfc2119>.

   [RFC3425]  Lawrence, D., "Obsoleting IQUERY", RFC 3425,
              DOI 10.17487/RFC3425, November 2002,
              <https://www.rfc-editor.org/info/rfc3425>.

   [RFC8174]  Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 
              2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174,
              May 2017, <https://www.rfc-editor.org/info/rfc8174>.

### 7.2. Informative References

   [RFC1996]  Vixie, P., "A Mechanism for Prompt Notification of Zone
              Changes (DNS NOTIFY)", RFC 1996, DOI 10.17487/RFC1996,
              August 1996, <https://www.rfc-editor.org/info/rfc1996>.

   [RFC2136]  Vixie, P., Ed., Thomson, S., Rekhter, Y., and J. Bound,
              "Dynamic Updates in the Domain Name System (DNS UPDATE)",RFC 2136, DOI 10.17487/RFC2136, April 1997,
              <https://www.rfc-editor.org/info/rfc2136>.

   [RFC5936]  Lewis, E. and A. Hoenes, Ed., "DNS Zone Transfer Protocol
              (AXFR)", RFC 5936, DOI 10.17487/RFC5936, June 2010,
              <https://www.rfc-editor.org/info/rfc5936>.

   [RFC7873]  Eastlake 3rd, D. and M. Andrews, "Domain Name System (DNS)
              Cookies", RFC 7873, DOI 10.17487/RFC7873, May 2016,
              <https://www.rfc-editor.org/info/rfc7873>.

   [RFC8490]  Bellis, R., Cheshire, S., Dickinson, J., Dickinson, S.,
              Lemon, T., and T. Pusateri, "DNS Stateful Operations",RFC 8490, DOI 10.17487/RFC8490, March 2019,
              <https://www.rfc-editor.org/info/rfc8490>.

   [RFC8906]  Andrews, M. and R. Bellis, "A Common Operational Problem
              in DNS Servers: Failure to Communicate", BCP 231,RFC 8906, DOI 10.17487/RFC8906, September 2020,
              <https://www.rfc-editor.org/info/rfc8906>.

## A. Guidance for the Use of QDCOUNT in the DNS Specification

   The DNS specification [RFC1035] provides some guidance about the
   values of QDCOUNT that are appropriate in various situations.  A
   brief summary of this guidance is collated below.

### A.1. OPCODE = 0 (QUERY) and 1 (IQUERY)

   [RFC1035] significantly predates the use of the normative requirement
   key words specified in BCP 14 [RFC2119] [RFC8174], and parts of it
   are consequently somewhat open to interpretation. Section 4.1.2 ("Question section format") of [RFC1035] states the
   following about QDCOUNT:

      "The section contains QDCOUNT (usually 1) entries"

   The only documented exceptions within [RFC1035] relate to the IQuery
   OpCode, where the request has "an empty question section" (QDCOUNT =
   0), and the response has "zero, one, or multiple domain names for the
   specified resource as QNAMEs in the question section".  The IQuery
   OpCode was obsoleted by [RFC3425].

   In the absence of clearly expressed normative requirements, we rely
   on other text in [RFC1035] that makes use of the definite article or
   that implies a singular question and, by implication, QDCOUNT = 1.

   For example, Section 4.1 of [RFC1035] states the following:

      "the question for the name server"

   and

      "The question section contains fields that describe a question to
      a name server."

   And per Section 4.1.1 ("Header section format") of [RFC1035]:

      "AA: Authoritative Answer - this bit is valid in responses, and
      specifies that the responding name server is an authority for the
      domain name in question section."

   DNS Cookies (Section 5.4 of [RFC7873]) allow a client to receive a
   valid Server Cookie without sending a specific question by sending a
   request (QR = 0) with OPCODE = 0 and QDCOUNT = 0, with the resulting
   response also containing no question.

   The DNS Zone Transfer Protocol (Section 2.2 of [RFC5936]) allows an
   authoritative server to optionally send a response message (QR = 1)
   to a standard Authoritative Transfer (AXFR) query (OPCODE = 0,
   QTYPE=252) with QDCOUNT = 0 in the second or subsequent message of a
   multi-message response.

### A.2. OPCODE = 4 (NOTIFY)

   DNS Notify [RFC1996] also lacks a clearly defined range of values for
   QDCOUNT.  Section 3.7 states that:

      "A NOTIFY request has QDCOUNT>0"

   However, all other text in the RFC discusses the <QNAME, QCLASS,
   QTYPE> tuple in the singular form.

### A.3. OPCODE = 5 (UPDATE)

   DNS Update [RFC2136] renames the QDCOUNT field to ZOCOUNT, but the
   value is constrained to be one by Section 2.3 ("Zone Section"):

      "All records to be updated must be in the same zone, and therefore
      the Zone Section is allowed to contain exactly one record."

### A.4. OPCODE = 6 (DNS Stateful Operations, DSO)

   DNS Stateful Operations (DSO) (OpCode 6) [RFC8490] preserves
   compatibility with the standard DNS 12-octet header by requiring all
   four of the section count values to be set to zero.

### A.5. Conclusion

   There is no text in [RFC1035] that describes how other parameters in
   the DNS message, such as AA and RCODE, should be interpreted in the
   case where a message includes more than one question.  An originator
   of a query with QDCOUNT > 1 can have no expectations of how it will
   be processed, and the receiver of a response with QDCOUNT > 1 has no
   guidance for how it should be interpreted.

   The allowable values of QDCOUNT seem to be clearly specified for
   OPCODE = 4 (NOTIFY), OPCODE = 5 (UPDATE), and OPCODE = 6 (DNS
   Stateful Operations, DSO).  OPCODE = 1 (IQUERY) is obsolete and
   OPCODE = 2 (STATUS) is not specified.  OPCODE = 3 is reserved.

   However, the allowable values of QDCOUNT for OPCODE = 0 (QUERY) are
   specified in [RFC1035] without the clarity of normative language, and
   this looseness of language results in some ambiguity.



---
# Referenced Sections from RFC 1035: Domain names - implementation and specification

The following sections were referenced. Remaining sections are not included.

## 1. STATUS OF THIS MEMO

This RFC describes the details of the domain system and protocol, and
assumes that the reader is familiar with the concepts discussed in a
companion RFC, "Domain Names - Concepts and Facilities" [RFC-1034].

The domain system is a mixture of functions and data types which are an
official protocol and functions and data types which are still
experimental.  Since the domain system is intentionally extensible, new
data types and experimental behavior should always be expected in parts
of the system beyond the official protocol.  The official protocol parts
include standard queries, responses and the Internet class RR data
formats (e.g., host addresses).  Since the previous RFC set, several
definitions have changed, so some previous definitions are obsolete.

Experimental or obsolete features are clearly marked in these RFCs, and
such information should be used with caution.

The reader is especially cautioned not to depend on the values which
appear in examples to be current or complete, since their purpose is
primarily pedagogical.  Distribution of this memo is unlimited.

                           Table of Contents

  1. STATUS OF THIS MEMO                                              1
  2. INTRODUCTION                                                     3
      2.1. Overview                                                   3
      2.2. Common configurations                                      4
      2.3. Conventions                                                7
          2.3.1. Preferred name syntax                                7
          2.3.2. Data Transmission Order                              8
          2.3.3. Character Case                                       9
          2.3.4. Size limits                                         10
  3. DOMAIN NAME SPACE AND RR DEFINITIONS                            10
      3.1. Name space definitions                                    10
      3.2. RR definitions                                            11
          3.2.1. Format                                              11
          3.2.2. TYPE values                                         12
          3.2.3. QTYPE values                                        12
          3.2.4. CLASS values                                        13
          3.2.5. QCLASS values                                       13
      3.3. Standard RRs                                              13
          3.3.1. CNAME RDATA format                                  14
          3.3.2. HINFO RDATA format                                  14
          3.3.3. MB RDATA format (EXPERIMENTAL)                      14
          3.3.4. MD RDATA format (Obsolete)                          15
          3.3.5. MF RDATA format (Obsolete)                          15
          3.3.6. MG RDATA format (EXPERIMENTAL)                      16
          3.3.7. MINFO RDATA format (EXPERIMENTAL)                   16
          3.3.8. MR RDATA format (EXPERIMENTAL)                      17
          3.3.9. MX RDATA format                                     17
          3.3.10. NULL RDATA format (EXPERIMENTAL)                   17
          3.3.11. NS RDATA format                                    18
          3.3.12. PTR RDATA format                                   18
          3.3.13. SOA RDATA format                                   19
          3.3.14. TXT RDATA format                                   20
      3.4. ARPA Internet specific RRs                                20
          3.4.1. A RDATA format                                      20
          3.4.2. WKS RDATA format                                    21
      3.5. IN-ADDR.ARPA domain                                       22
      3.6. Defining new types, classes, and special namespaces       24
  4. MESSAGES                                                        25
      4.1. Format                                                    25
          4.1.1. Header section format                               26
          4.1.2. Question section format                             28
          4.1.3. Resource record format                              29
          4.1.4. Message compression                                 30
      4.2. Transport                                                 32
          4.2.1. UDP usage                                           32
          4.2.2. TCP usage                                           32
  5. MASTER FILES                                                    33
      5.1. Format                                                    33
      5.2. Use of master files to define zones                       35
      5.3. Master file example                                       36
  6. NAME SERVER IMPLEMENTATION                                      37
      6.1. Architecture                                              37
          6.1.1. Control                                             37
          6.1.2. Database                                            37
          6.1.3. Time                                                39
      6.2. Standard query processing                                 39
      6.3. Zone refresh and reload processing                        39
      6.4. Inverse queries (Optional)                                40
          6.4.1. The contents of inverse queries and responses       40
          6.4.2. Inverse query and response example                  41
          6.4.3. Inverse query processing                            42
      6.5. Completion queries and responses                          42
  7. RESOLVER IMPLEMENTATION                                         43
      7.1. Transforming a user request into a query                  43
      7.2. Sending the queries                                       44
      7.3. Processing responses                                      46
      7.4. Using the cache                                           47
  8. MAIL SUPPORT                                                    47
      8.1. Mail exchange binding                                     48
      8.2. Mailbox binding (Experimental)                            48
  9. REFERENCES and BIBLIOGRAPHY                                     50
  Index                                                              54

