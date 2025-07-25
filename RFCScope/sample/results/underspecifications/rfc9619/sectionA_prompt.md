Let us analyze section A of RFC 9619. All references made by section A have also been included below.

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

### 4.1. Format

All communications inside of the domain protocol are carried in a single
format called a message.  The top level format of message is divided
into 5 sections (some of which are empty in certain cases) shown below:

    +---------------------+
    |        Header       |
    +---------------------+
    |       Question      | the question for the name server
    +---------------------+
    |        Answer       | RRs answering the question
    +---------------------+
    |      Authority      | RRs pointing toward an authority
    +---------------------+
    |      Additional     | RRs holding additional information
    +---------------------+

The header section is always present.  The header includes fields that
specify which of the remaining sections are present, and also specify
whether the message is a query or a response, a standard query or some
other opcode, etc.

The names of the sections after the header are derived from their use in
standard queries.  The question section contains fields that describe a
question to a name server.  These fields are a query type (QTYPE), a
query class (QCLASS), and a query domain name (QNAME).  The last three
sections have the same format: a possibly empty list of concatenated
resource records (RRs).  The answer section contains RRs that answer the
question; the authority section contains RRs that point toward an
authoritative name server; the additional records section contains RRs
which relate to the query, but are not strictly answers for the
question. 





#### 4.1.1. Header section format

The header contains the following fields:

                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

where:

ID              A 16 bit identifier assigned by the program that
                generates any kind of query.  This identifier is copied
                the corresponding reply and can be used by the requester
                to match up replies to outstanding queries.

QR              A one bit field that specifies whether this message is a
                query (0), or a response (1).

OPCODE          A four bit field that specifies kind of query in this
                message.  This value is set by the originator of a query
                and copied into the response.  The values are:

                0               a standard query (QUERY)

                1               an inverse query (IQUERY)

                2               a server status request (STATUS)

                3-15            reserved for future use

AA              Authoritative Answer - this bit is valid in responses,
                and specifies that the responding name server is an
                authority for the domain name in question section.

                Note that the contents of the answer section may have
                multiple owner names because of aliases.  The AA bit 
                corresponds to the name which matches the query name, or
                the first owner name in the answer section.

TC              TrunCation - specifies that this message was truncated
                due to length greater than that permitted on the
                transmission channel.

RD              Recursion Desired - this bit may be set in a query and
                is copied into the response.  If RD is set, it directs
                the name server to pursue the query recursively.
                Recursive query support is optional.

RA              Recursion Available - this be is set or cleared in a
                response, and denotes whether recursive query support is
                available in the name server.

Z               Reserved for future use.  Must be zero in all queries
                and responses.

RCODE           Response code - this 4 bit field is set as part of
                responses.  The values have the following
                interpretation:

                0               No error condition

                1               Format error - The name server was
                                unable to interpret the query.

                2               Server failure - The name server was
                                unable to process this query due to a
                                problem with the name server.

                3               Name Error - Meaningful only for
                                responses from an authoritative name
                                server, this code signifies that the
                                domain name referenced in the query does
                                not exist.

                4               Not Implemented - The name server does
                                not support the requested kind of query.

                5               Refused - The name server refuses to
                                perform the specified operation for
                                policy reasons.  For example, a name
                                server may not wish to provide the
                                information to the particular requester,
                                or a name server may not wish to perform
                                a particular operation (e.g., zone 
                                transfer) for particular data.

                6-15            Reserved for future use.

QDCOUNT         an unsigned 16 bit integer specifying the number of
                entries in the question section.

ANCOUNT         an unsigned 16 bit integer specifying the number of
                resource records in the answer section.

NSCOUNT         an unsigned 16 bit integer specifying the number of name
                server resource records in the authority records
                section.

ARCOUNT         an unsigned 16 bit integer specifying the number of
                resource records in the additional records section.

#### 4.1.2. Question section format

The question section is used to carry the "question" in most queries,
i.e., the parameters that define what is being asked.  The section
contains QDCOUNT (usually 1) entries, each of the following format:

                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                     QNAME                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     QTYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     QCLASS                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

where:

QNAME           a domain name represented as a sequence of labels, where
                each label consists of a length octet followed by that
                number of octets.  The domain name terminates with the
                zero length octet for the null label of the root.  Note
                that this field may be an odd number of octets; no
                padding is used.

QTYPE           a two octet code which specifies the type of the query.
                The values for this field include all codes valid for a
                TYPE field, together with some more general codes which
                can match more than one type of RR. 
QCLASS          a two octet code that specifies the class of the query.
                For example, the QCLASS field is IN for the Internet.

#### 4.1.3. Resource record format

The answer, authority, and additional sections all share the same
format: a variable number of resource records, where the number of
records is specified in the corresponding count field in the header.
Each resource record has the following format:
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                                               /
    /                      NAME                     /
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     CLASS                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TTL                      |
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                   RDLENGTH                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--|
    /                     RDATA                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

where:

NAME            a domain name to which this resource record pertains.

TYPE            two octets containing one of the RR type codes.  This
                field specifies the meaning of the data in the RDATA
                field.

CLASS           two octets which specify the class of the data in the
                RDATA field.

TTL             a 32 bit unsigned integer that specifies the time
                interval (in seconds) that the resource record may be
                cached before it should be discarded.  Zero values are
                interpreted to mean that the RR can only be used for the
                transaction in progress, and should not be cached. 
RDLENGTH        an unsigned 16 bit integer that specifies the length in
                octets of the RDATA field.

RDATA           a variable length string of octets that describes the
                resource.  The format of this information varies
                according to the TYPE and CLASS of the resource record.
                For example, the if the TYPE is A and the CLASS is IN,
                the RDATA field is a 4 octet ARPA Internet address.

#### 4.1.4. Message compression

In order to reduce the size of messages, the domain system utilizes a
compression scheme which eliminates the repetition of domain names in a
message.  In this scheme, an entire domain name or a list of labels at
the end of a domain name is replaced with a pointer to a prior occurance
of the same name.

The pointer takes the form of a two octet sequence:

    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    | 1  1|                OFFSET                   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

The first two bits are ones.  This allows a pointer to be distinguished
from a label, since the label must begin with two zero bits because
labels are restricted to 63 octets or less.  (The 10 and 01 combinations
are reserved for future use.)  The OFFSET field specifies an offset from
the start of the message (i.e., the first octet of the ID field in the
domain header).  A zero offset specifies the first byte of the ID field,
etc.

The compression scheme allows a domain name in a message to be
represented as either:

   - a sequence of labels ending in a zero octet

   - a pointer

   - a sequence of labels ending with a pointer

Pointers can only be used for occurances of a domain name where the
format is not class specific.  If this were not the case, a name server
or resolver would be required to know the format of all RRs it handled.
As yet, there are no such cases, but they may occur in future RDATA
formats.

If a domain name is contained in a part of the message subject to a
length field (such as the RDATA section of an RR), and compression is 
used, the length of the compressed name is used in the length
calculation, rather than the length of the expanded name.

Programs are free to avoid using pointers in messages they generate,
although this will reduce datagram capacity, and may cause truncation.
However all programs are required to understand arriving messages that
contain pointers.

For example, a datagram might need to use the domain names F.ISI.ARPA,
FOO.F.ISI.ARPA, ARPA, and the root.  Ignoring the other fields of the
message, these domain names might be represented as:

       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    20 |           1           |           F           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    22 |           3           |           I           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    24 |           S           |           I           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    26 |           4           |           A           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    28 |           R           |           P           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    30 |           A           |           0           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    40 |           3           |           F           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    42 |           O           |           O           |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    44 | 1  1|                20                       |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    64 | 1  1|                26                       |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    92 |           0           |                       |
       +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

The domain name for F.ISI.ARPA is shown at offset 20.  The domain name
FOO.F.ISI.ARPA is shown at offset 40; this definition uses a pointer to
concatenate a label for FOO to the previously defined F.ISI.ARPA.  The
domain name ARPA is defined at offset 64 using a pointer to the ARPA
component of the name F.ISI.ARPA at 20; note that this pointer relies on
ARPA being the last label in the string at 20.  The root domain name is 
defined by a single octet of zeros at 92; the root domain name has no
labels.

# Referenced Sections from RFC 7873: Domain Name System (DNS) Cookies

The following sections were referenced. Remaining sections are not included.

### 5.4. Querying for a Server Cookie

   In many cases, a client will learn the Server Cookie for a server as
   the "side effect" of another transaction; however, there may be times
   when this is not desirable.  Therefore, a means is provided for
   obtaining a Server Cookie through an extension to the QUERY opcode
   for which opcode most existing implementations require that QDCOUNT
   be one (1) (see Section 4.1.2 of [RFC1035]). 
   For servers with DNS Cookies enabled, the QUERY opcode behavior is
   extended to support queries with an empty Question Section (a QDCOUNT
   of zero (0)), provided that an OPT record is present with a COOKIE
   option.  Such servers will send a reply that has an empty
   Answer Section and has a COOKIE option containing the Client Cookie
   and a valid Server Cookie.

   If such a query provided just a Client Cookie and no Server Cookie,
   the response SHALL have the RCODE NOERROR.

   This mechanism can also be used to confirm/re-establish an existing
   Server Cookie by sending a cached Server Cookie with the
   Client Cookie.  In this case, the response SHALL have the RCODE
   BADCOOKIE if the Server Cookie sent with the query was invalid and
   the RCODE NOERROR if it was valid.

   Servers that don't support the COOKIE option will normally send
   FORMERR in response to such a query, though REFUSED, NOTIMP, and
   NOERROR without a COOKIE option are also possible in such responses.

# Referenced Sections from RFC 5936: DNS Zone Transfer Protocol (AXFR)

The following sections were referenced. Remaining sections are not included.

### 2.2. AXFR Response

   The AXFR response will consist of one or more messages.  The special
   case of a server closing the TCP connection without sending an AXFR
   response is covered in Section 2.3.

   An AXFR response that is transferring the zone's contents will
   consist of a series (which could be a series of length 1) of DNS
   messages.  In such a series, the first message MUST begin with the
   SOA resource record of the zone, and the last message MUST conclude
   with the same SOA resource record.  Intermediate messages MUST NOT
   contain the SOA resource record.  The AXFR server MUST copy the
   Question section from the corresponding AXFR query message into the
   first response message's Question section.  For subsequent messages,
   it MAY do the same or leave the Question section empty.

   The AXFR protocol treats the zone contents as an unordered collection
   (or to use the mathematical term, a "set") of RRs.  Except for the
   requirement that the transfer must begin and end with the SOA RR,
   there is no requirement to send the RRs in any particular order or
   grouped into response messages in any particular way.  Although
   servers typically do attempt to send related RRs (such as the RRs
   forming an RRset, and the RRsets of a name) as a contiguous group or,
   when message space allows, in the same response message, they are not
   required to do so, and clients MUST accept any ordering and grouping
   of the non-SOA RRs.  Each RR SHOULD be transmitted only once, and
   AXFR clients MUST ignore any duplicate RRs received.

   Each AXFR response message SHOULD contain a sufficient number of RRs
   to reasonably amortize the per-message overhead, up to the largest
   number that will fit within a DNS message (taking the required
   content of the other sections into account, as described below). 
   Some old AXFR clients expect each response message to contain only a
   single RR.  To interoperate with such clients, the server MAY
   restrict response messages to a single RR.  As there is no standard
   way to automatically detect such clients, this typically requires
   manual configuration at the server.

   To indicate an error in an AXFR response, the AXFR server sends a
   single DNS message when the error condition is detected, with the
   response code set to the appropriate value for the condition
   encountered.  Such a message terminates the AXFR session; it MUST
   contain a copy of the Question section from the AXFR query in its
   Question section, but the inclusion of the terminating SOA resource
   record is not necessary.

   An AXFR server may send a number of AXFR response messages free of an
   error condition before it sends the message indicating an error.

#### 2.2.1. Header Values

   These are the DNS message header values for AXFR responses.

      ID          MUST be copied from request -- see Note a)

      QR          MUST be 1 (Response)

      OPCODE      MUST be 0 (Standard Query)

      Flags:
         AA       normally 1 -- see Note b)
         TC       MUST be 0 (Not truncated)
         RD       RECOMMENDED: copy request's value; MAY be set to 0
         RA       SHOULD be 0 -- see Note c)
         Z        "mbz" -- see Note d)
         AD       "mbz" -- see Note d)
         CD       "mbz" -- see Note d)

      RCODE       See Note e)

      QDCOUNT     MUST be 1 in the first message;
                  MUST be 0 or 1 in all following messages;
                  MUST be 1 if RCODE indicates an error

      ANCOUNT     See Note f)

      NSCOUNT     MUST be 0

      ARCOUNT     See Note g)
   Notes:

   a) Because some old implementations behave differently than is now
      desired, the requirement on this field is stated in detail.  New
      DNS servers MUST set this field to the value of the AXFR query ID
      in each AXFR response message for the session.  AXFR clients MUST
      be able to manage sessions resulting from the issuance of multiple
      outstanding queries, whether AXFR queries or other DNS queries.  A
      client SHOULD discard responses that do not correspond (via the
      message ID) to any outstanding queries.

      Unless the client is sure that the server will consistently set
      the ID field to the query's ID, the client is NOT RECOMMENDED to
      issue any other queries until the end of the zone transfer.  A
      client MAY become aware of a server's abilities via a
      configuration setting.

   b) If the RCODE is 0 (no error), then the AA bit MUST be 1.  For any
      other value of RCODE, the AA bit MUST be set according to the
      rules for that error code.  If in doubt, it is RECOMMENDED that it
      be set to 1.  It is RECOMMENDED that the value be ignored by the
      AXFR client.

   c) It is RECOMMENDED that the server set the value to 0; the client
      MUST ignore this value.

      The server MAY set this value according to the local policy
      regarding recursive service, but doing so might confuse the
      interpretation of the response, as AXFR cannot be retrieved
      recursively.  A client MAY note the server's policy regarding
      recursive service from this value, but SHOULD NOT conclude that
      the AXFR response was obtained recursively, even if the RD bit was
      1 in the query.

   d) "mbz" -- The server MUST set this bit to 0; the client MUST ignore
      it.

   e) In the absence of an error, the server MUST set the value of this
      field to NoError(0).  If a server is not authoritative for the
      queried zone, the server SHOULD set the value to NotAuth(9).
      (Reminder: Consult the appropriate IANA registry [DNSVALS ].)  If a
      client receives any other value in response, it MUST act according
      to the error.  For example, a malformed AXFR query or the presence
      of an OPT resource record sent to an old server will result in a
      FormErr(1) value.  This value is not set as part of the AXFR-
      specific response processing.  The same is true for other values
      indicating an error. 
   f) The count of answer records MUST equal the number of resource
      records in the AXFR Answer section.  When a server is aware that a
      client will only accept response messages with a single resource
      record, then the value MUST be 1.  A server MAY be made aware of a
      client's limitations via configuration data.

   g) The server MUST set this field to the number of resource records
      it places into the Additional section.  In the absence of explicit
      specification of new RRs to be carried in the Additional section
      of AXFR response messages, the value MAY be 0, 1, or 2.  See Section 2.1.5 above for details on the currently applicable RRs
      and Section 2.2.5 for additional considerations specific to AXFR
      servers.

#### 2.2.2. Question Section

   In the first response message, this section MUST be copied from the
   query.  In subsequent messages, this section MAY be copied from the
   query, or it MAY be empty.  However, in an error response message
   (see Section 2.2), this section MUST be copied as well.  The content
   of this section MAY be used to determine the context of the message,
   that is, the name of the zone being transferred.

#### 2.2.3. Answer Section

   The Answer section MUST be populated with the zone contents.  See Section 3 below on encoding zone contents.

#### 2.2.4. Authority Section

   The Authority section MUST be empty.

#### 2.2.5. Additional Section

   The contents of this section MUST follow the guidelines for the OPT,
   TSIG, and SIG(0) RRs, or whatever other future record is possible
   here.  The contents of Section 2.1.5 apply analogously as well.

   The following considerations specifically apply to AXFR responses:

   If the client has supplied an EDNS OPT RR in the AXFR query and if
   the server supports EDNS as well, it SHOULD include one OPT RR in the
   first response message and MAY do so in subsequent response messages
   (see Section 2.2); the specifications of EDNS options to be carried
   in the OPT RR may impose stronger requirements. 
   If the client has supplied a transaction security resource record
   (currently a choice of TSIG and SIG(0)) and the server supports the
   method chosen by the client, it MUST place the corresponding resource
   record into the AXFR response message(s), according to the rules
   specified for that method.

