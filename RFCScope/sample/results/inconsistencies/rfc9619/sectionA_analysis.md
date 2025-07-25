Below are two errata reports based on our detailed analysis of Section A (“Guidance for the Use of QDCOUNT in the DNS Specification”) in RFC 9619.

─────────────────────────────────────────────  
Errata Report 1: Incorrect Field Name ("QDCODE" vs. "QDCOUNT")  
─────────────────────────────────────────────  
RFC Number & Title:  
 RFC 9619 – In the DNS, QDCOUNT Is (Usually) One

Section:  
 Section 1 (Introduction)

Excerpt from the text:  
 “…update the DNS base specification to clarify the allowable values of the QDCODE parameter in the specific case of DNS messages with OPCODE = 0.”

Detailed Explanation:  
The introduction refers to a field called “QDCODE” even though every other reference and the DNS header specification (e.g., in Section 4.1.1 of RFC 1035) use the term “QDCOUNT.” Since the DNS header field in question is officially named QDCOUNT, the use of “QDCODE” is an apparent typographical error. This inconsistency in terminology might confuse implementers regarding which header field is being discussed and updated. The document should consistently refer to the field as QDCOUNT.

─────────────────────────────────────────────  
Errata Report 2: Ambiguity in the NOTIFY Request’s QDCOUNT Range  
─────────────────────────────────────────────  
RFC Number & Title:  
 RFC 9619 – In the DNS, QDCOUNT Is (Usually) One

Section:  
 Section A.2 (“OPCODE = 4 (NOTIFY)”)

Excerpt from the text:  
 “DNS Notify [RFC1996] also lacks a clearly defined range of values for QDCOUNT. Section 3.7 states that:  
  "A NOTIFY request has QDCOUNT>0"  
However, all other text in the RFC discusses the <QNAME, QCLASS, QTYPE> tuple in the singular form.”

Detailed Explanation:  
In RFC 9619 Section A.2, the authors note that the DNS Notify specification (RFC 1996) stipulates that a NOTIFY request “has QDCOUNT>0.” Taken literally, this requirement permits any value greater than zero—even though all other descriptive language in RFC 1996 treats the question section as if it consists of a single <QNAME, QCLASS, QTYPE> tuple. This mismatch creates ambiguity:
 • On one hand, the normative statement “QDCOUNT>0” does not explicitly restrict the count to 1.  
 • On the other hand, the singular phrasing (“the question …”) strongly implies that only one question is intended.
As a result, implementers might be unsure whether a NOTIFY request with multiple questions (i.e., QDCOUNT > 1) should be accepted or must be treated as malformed. This inconsistency in the treatment and expectation of the question section for NOTIFY requests could lead to interoperability problems.

─────────────────────────────────────────────  

These two issues highlight internal inconsistencies between the terminology and the intended structural constraints on QDCOUNT as described in RFC 9619 (and in the referenced RFCs).