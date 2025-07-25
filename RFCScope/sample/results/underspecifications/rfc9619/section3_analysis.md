Below is an errata report for RFC 9619 (In the DNS, QDCOUNT Is (Usually) One) concentrating on Section 3.

────────────────────────────
Errata Report for RFC 9619  
Title: In the DNS, QDCOUNT Is (Usually) One  
Section: 3. QDCOUNT Is (Usually) One  
Excerpts from Section 3:  
  "A brief summary of the guidance provided in the existing DNS specification ([RFC1035] and many other documents) for the use of QDCOUNT can be found in Appendix A. While the specification is clear in many cases, there is some ambiguity in the specific case of OPCODE = 0, which this document aims to eliminate."

Issue 1. Ambiguous Use of “Usually”  
Explanation:  
Section 3’s title and text state that “QDCOUNT Is (Usually) One” without defining what “usually” means in this context. Although the introduction and later sections imply that in DNS messages with OPCODE = 0 the permitted QDCOUNT values are constrained to 0 or 1, the word “usually” can be interpreted in multiple ways. Implementers reading just this section might wonder whether a value of 0 is acceptable only under exceptional circumstances (for example, as in DNS Cookies or AXFR responses) or whether other cases might allow deviations. This underspecification of the term “usually” leaves the normative requirements for QDCOUNT in query messages—especially which conditions justify a value of 0 rather than 1—inadequately precise.

Issue 2. Lack of Explicit Description of the Ambiguity for OPCODE = 0  
Explanation:  
The section notes that "there is some ambiguity in the specific case of OPCODE = 0" yet does not state what aspects of previous guidance (for example, in RFC 1035 and related documents) are ambiguous or what kinds of DNS query scenarios (such as those involving DNS Cookies or multi-message AXFR responses) lead to it. Although Appendix A is referenced as containing a summary of the guidance, Section 3 itself—as a summary heading—does not provide any concise normative statement or clear pointers that let the reader quickly discern which interpretations are disallowed (for example, by clarifying that for DNS queries with OPCODE = 0 the Question section must contain either zero or one question). The lack of an explicit summary of the edge cases in Section 3 can lead to confusion for implementers who aim to understand the rationale without parsing the (longer) Appendix A or later sections.

Reasoning Behind the Analysis:  
• The term “usually” is employed in a technical context where precision is expected. Without a clear definition, there is room for multiple interpretations in the design and implementation of DNS systems.  
• Because Section 3 identifies that an ambiguity exists (specifically for messages with OPCODE = 0) without summarizing which situations require QDCOUNT = 0 versus 1, implementers may not immediately know—for instance, when dealing with special cases like DNS Cookies [RFC7873] or AXFR responses [RFC5936]—how to interpret the guidance if they consult Section 3 only.  
• While later sections (notably Section 4 and Appendix A) provide additional detail, a standalone summary section should still clearly state the nature of the ambiguity so that the document’s intent is immediately apparent and unambiguous.

────────────────────────────
Note:  
This errata report identifies underspecifications in Section 3 only. It is not a comment on other parts of the document, many of which do subsequently provide normative guidance. No proposed resolution is given here—the goal is solely to call attention to lack of explicit definitions and insufficient in‐section explanation regarding QDCOUNT values for OPCODE = 0.

