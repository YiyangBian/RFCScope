Below is the errata report detailing the inconsistency found in Section 1 of RFC 9619.

─────────────────────────────  
Errata for RFC 9619: In the DNS, QDCOUNT Is (Usually) One  
─────────────────────────────  

1. Inconsistent Naming of the Query Count Field

Section Affected:  
 • Section 1 (Introduction)

Excerpt:  
 "In this document, we briefly survey the existing written DNS specification; provide a description of the semantic and practical requirements for DNS queries that naturally constrain the allowable values of QDCOUNT; and update the DNS base specification to clarify the allowable values of the QDCODE parameter in the specific case of DNS messages with OPCODE = 0."

Issue Details:  
The Introduction correctly introduces the parameter as QDCOUNT (the unsigned 16‐bit field in the DNS header that indicates the number of questions). However, in the same paragraph the document later refers to “the QDCODE parameter” when discussing updates to the DNS base specification. This appears to be a typographical error or misnaming, as no parameter named QDCODE is defined anywhere in this document or the base DNS specifications. Given the context and the remainder of the document, the intended reference should be to QDCOUNT.

Reasoning:  
– The document’s title (“In the DNS, QDCOUNT Is (Usually) One”) and earlier text consistently use QDCOUNT.  
– The use of “QDCODE” is inconsistent with both the well-known DNS header field name and the contextual description provided.  
– Such a misnaming could lead to confusion during implementation or further clarification documents, as implementers might be unsure whether QDCODE is an intended new parameter or simply a typographical error.

This inconsistency needs to be reported so that the document can be corrected to refer consistently to QDCOUNT throughout.

─────────────────────────────  
End of Errata Report  
─────────────────────────────