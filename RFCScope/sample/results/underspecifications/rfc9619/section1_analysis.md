Below is an errata report for an ambiguity found in Section 1 of RFC 9619.

────────────────────────────────────────
Errata Report: Typographical Ambiguity in the Parameter Name  
RFC: 9619 – In the DNS, QDCOUNT Is (Usually) One  
Section: 1. Introduction

Excerpt from Section 1:
  …update the DNS base specification to clarify the allowable values of the QDCODE parameter in the specific case of DNS messages with OPCODE = 0.

Explanation:
In the introduction the document consistently discusses the DNS header field that counts the number of questions, which is defined as QDCOUNT in RFC 1035. However, in the final sentence of Section 1 the text refers to a “QDCODE parameter.” This term is undefined and does not appear anywhere else in RFC 9619, leading to ambiguity. It appears to be a typographical error that mistakenly substitutes “QDCODE” for the intended “QDCOUNT.” Since this misnaming might confuse implementers regarding which parameter is being updated and clarified, it constitutes an underspecification.

Notes:
– The error could lead readers to wonder if a new parameter (QDCODE) is meant to be introduced or if it is simply an inadvertent misnaming of QDCOUNT.
– The intended meaning — to update the DNS base specification for DNS messages with OPCODE = 0 — becomes less clear due to this typographical ambiguity.

────────────────────────────────────────

No other underspecifications were identified in Section 1.