Below is an errata report that highlights a naming inconsistency discovered when analyzing Section 4 (together with its related text) of RFC 9619:

----------------------------------------------------------------
Errata Report for RFC 9619  
Title: In the DNS, QDCOUNT Is (Usually) One

Section(s):  
• Section 1 (Introduction) – where the document pledges “to clarify the allowable values of the QDCODE parameter in the specific case of DNS messages with OPCODE = 0.”  
• Section 4 uses the header field name QDCOUNT correctly.

Issue: Inconsistent Parameter Naming

Excerpt from Section 1 (Introduction):  
  “… update the DNS base specification to clarify the allowable values of the QDCODE parameter in the specific case of DNS messages with OPCODE = 0.”

Explanation:  
The DNS header field in question is defined in RFC 1035 as QDCOUNT. Later in the same document (for example, in Section 4) the text consistently refers to QDCOUNT. The use of “QDCODE” in Section 1 appears to be a typographical error or an inadvertent misnaming of the parameter. Such an inconsistency in the parameter’s naming could confuse implementers or readers who expect uniform terminology throughout the RFC. Since the DNS header field is clearly known as QDCOUNT, all references should use that term.

Notes:  
– The intended parameter is QDCOUNT.  
– This error likely results from a typographical oversight and should be corrected to maintain clarity and consistency with the DNS base specifications (RFC 1035).

----------------------------------------------------------------

No other internal inconsistencies were identified in Section 4’s normative guidance regarding QDCOUNT for messages with OPCODE = 0; the additional instructions (for example, about how middleboxes should handle messages with QDCOUNT > 1 versus QDCOUNT = 0) are consistent with the documented exceptions (such as for DNS Cookies and certain AXFR responses).

This concludes the errata report based on the analysis of Section 4 (and its referenced portions) of RFC 9619.