You are an expert in networking and have over 20 years of experience in writing RFC (Request for Comments) documents related to Internet protocol standards. Today you will be analysing excerpts from RFC documents and discovering any underspecifications in them. You will report these underspecifications in the form of errata reports, which we will submit to the IETF portal to help improve the quality of the RFC documents. You MUST follow all the steps given below to complete this task.

1. Scan the provided text carefully and identify several concepts. Concepts can be entities, processes, relationships, constraints, etc. present in the text. Think deeply about each concept as you try to discover underspecifications concept-by-concept. Do not miss anything in the text, not even diagrams, tables, or examples.

2. For each concept, identify whether there are any underspecifications in the text.
    2.1. Consider if there are terms that have not been defined in the text. You should also look for terms which are ambiguous, like adjectives used in technical contexts without clear definitions. Similarly, look for terms that can be interpreted in multiple ways.
    2.2. Check if there is incomplete information in the text that can be resolved only by inputs from the authors. This may include missing constraints, missing situations or conditions in a process, or even just missing explanations.
    2.3. It is possible that there are references to non-existent sections, or that the references do not really support the text. This is also an underspecification and should be reported.
    2.4. It is common to see that when two parts of the text are related, one part provides incomplete information with respect to the other. This is a common underspecification and should be reported.
    2.5. As before, double-check your findings to ensure that they are indeed underspecifications and not clarifications, stylistic issues, or technical improvements in the protocols themselves. These MUST NOT be reported as underspecifications.
    2.6. Make sure that you are NOT excessively eager to find underspecifications. It is possible that the information that is not provided in the text is not relevant to the context of the document. Similarly, it is possible that the information is specified later in the document, or in some reference. DO NOT report these as underspecifications. Make sure that you keep this in mind before reporting an underspecification.

3. Write an errata report for all the underspecifications you find. The report should be clear, concise, and should contain the following information:
    3.1. The RFC number and title where the issue was found.
    3.2. Proper reference to the section where the issue was found, preferably with excerpts from the text.
    3.3. A detailed explanation of the issue, including why it belongs to underspecifications. You MUST include the reasoning behind your analysis and why you think it is an error. This is very important for us to understand the issue better and to check that your analysis is correct.
    3.4. You NEED NOT provide a solution to the issue. Your job is to identify and report the issue only.

Go through these steps sequentially for each concept you identify in the text, and carefully write the errata reports. Here are some examples of errata reports for your reference:

# Direct under-specification due to undefined terms

## Use of ambiguous terms with multiple interpretations

Errata 7894 from RFC 8888 (RTP Control Protocol (RTCP) Feedback for Congestion Control)

Section 3.1 says:

   RTCP Congestion Control Feedback Packets SHOULD include a report
   block for every active SSRC.
It should say:

   RTCP Congestion Control Feedback Packets SHOULD include a report
   block for every SSRC where packets have been received since the
   previous report was generated.

Notes:

The term "active" is ambiguous. Discussion on the avtcore mailing list indicates that this is the intended meaning.
The original text uses the term "active SSRC", which is ambiguous. The correction clarifies that a report block should be included for each SSRC where packets have been received since the last report, providing a more precise definition.

## Use of undefined terms

Errata 4439 from RFC 7240 (Prefer Header for HTTP)

Section 2 says:

     preference = token [ BWS "=" BWS word ]
                  *( OWS ";" [ OWS parameter ] )
     parameter  = token [ BWS "=" BWS word ]

It should say:

     preference = preference-parameter *( OWS ";" [ OWS
                  preference-parameter ] )
     preference-parameter = parameter / token

Notes:

Section 1.1 incorrectly states that "word" is defined in RFC 7230.  It is not.  Therefore, the syntax is completely under-specified.

The "parameter" rule, as defined in RFC 7231, is used in lots of other header field definitions successfully.  The only drawback is that "parameter" doesn't permit the use of "OWS" either side of the "=" character.

This change would also require changes to Section 1.1.
The erratum points out that the original specification uses an undefined term "word" in the definition of `preference` and `parameter`, rendering the syntax incomplete and making it impossible to unambiguously implement support for the Prefer header. The lack of a clear definition for "word" and the suggested replacement using the more precisely defined `parameter` rule from RFC 7231 directly addresses this underspecification, impacting the correct implementation of parsing and handling of the Prefer header.

# Direct under-specification due to incomplete constraints

## Missing constraints

Errata 4938 from RFC 7714 (AES-GCM Authenticated Encryption in the Secure Real-time Transport Protocol (SRTP))

Section 11 says:

A Key Derivation Function (KDF) is used to derive all of the required
encryption and authentication keys from a secret value shared by the
endpoints.  The AEAD_AES_128_GCM algorithm MUST use the (128-bit)
AES_CM PRF KDF described in [RFC3711].  AEAD_AES_256_GCM MUST use the
AES_256_CM_PRF KDF described in [RFC6188].

It should say:

A Key Derivation Function (KDF) is used to derive all of the required
encryption and authentication keys from a secret value shared by the
endpoints.  The AEAD_AES_128_GCM algorithm MUST use the (128-bit)
AES_CM PRF KDF described in [RFC3711].  AEAD_AES_256_GCM MUST use the
AES_256_CM_PRF KDF described in [RFC6188].  Since the KDF functions in
those RFCs assume as input a 112-bit master salt, the 96-bit master
salt specified in this document must be multiplied by 2^16 to form the
112-bit salt used as the master salt in those key derivation functions.

Notes:

The salt specified in RFC 7714 is 96 bits in length, but intended for use in KDF functions defined in RFC 3711.  This led to different interpretations when implementing this RFC.  A more complete description was presented on the avtcore mailing list (https://mailarchive.ietf.org/arch/msg/avt/IRfLuNKglD3qhqwSz3v3t0CG6fA) and, after some dialog, there seemed to be agreement to adopt the approach most widely implemented (https://mailarchive.ietf.org/arch/msg/avt/-C1cIWQXpyzS2KfBjGR6B2kK92w).  This suggested text is intended to reflect that agreement.  In effect, 16 zero bits are padded to the right of the salt value  defined in RFC 7714 (creating a 112 bit salt value) before it is used as described in the KDF functions defined in RFC 3711 that require a 112 bit salt value.
The original text does not specify how to handle the 96-bit master salt defined in RFC 7714 with the 112-bit master salt assumed by the KDF functions in RFC 3711. The correction clarifies that the 96-bit salt must be multiplied by 2^16 to create a 112-bit salt, resolving the inconsistency.

## Missing cases or situations

Errata 5540 from RFC 7728 (RTP Stream Pause and Resume)

Section 8.2.  PAUSED says:

   PAUSED SHALL contain a fixed-length 32-bit parameter at the start of
   the Type Specific field with the extended RTP sequence number of the
   last RTP packet sent before the RTP stream was paused, in the same
   format as the extended highest sequence number received
   (Section 6.4.1 of [RFC3550]).

It should say:

   PAUSED SHALL contain a fixed-length 32-bit parameter at the start of
   the Type Specific field with the extended RTP sequence number of the
   last RTP packet sent before the RTP stream was paused, in the same
   format as the extended highest sequence number received
   (Section 6.4.1 of [RFC3550]), or, if no packet has been sent, the
   value one less than the sequence number that will be chosen for the
   next packet sent (modulo 2^32).

Notes:

The paragraph leaves the value of the parameter undefined when the stream is paused before any data has been sent.
The original specification does not define the value of the 32-bit parameter in the PAUSED message when no RTP packets have been sent before pausing.  This under-specification leads to ambiguity in implementations and potential interoperability issues. The correction clarifies the value to be used in this scenario.

## Missing descriptions or explanations

Errata 5554 from RFC 7432 (BGP MPLS-Based Ethernet VPN)

Section 7 says:

Clarifications to following sub-sections:

Section 7.1

Section 7.2

Section 7.5

It should say:

Section 7.1:

Add below text to the section 7.1 regarding the encoding
of MPLS label field:

"The value of the 20-bit MPLS label is encoded in the high-order
20 bits of the 3 octets MPLS Label field."

Section 7.2:

Add below text to the section 7.2 regarding the encoding
of both the MPLS label fields:

"The value of the 20-bit MPLS label is encoded in the high-order
20 bits of the 3 octets MPLS Label1 and MPLS Label2 fields."

Section 7.5:

Add below text to the section 7.5 regarding the encoding of
ESI Label field:

"The value of the 20-bit MPLS label is encoded in the high-order
20 bits of the 3 octets ESI Label field."

Notes:

MPLS label is a 20-bit value and is stored in a 3 bytes field in a packet.
The 20-bit MPLS label value is generally stored in higher order 20 bits
of the 3 octet label field. The exact encoding to be followed for storing
MPLS label values are not explicitly mentioned in the RFC 7432 under
section 7.1, 7.2 and 7.5 for different types of EVPN routes. This lead to
ambiguity in different  implementations. Hence a clarification is required.
The original specification lacks explicit details on the encoding of MPLS label values within 3-octet fields. The lack of this information leads to ambiguity in implementations, resulting in different interpretations of the encoding.  The erratum's suggested additions address this incompleteness, making the specification more precise and improving interoperability.

# Indirect under-specification

## Missing constraints

Errata 6123 from RFC 8446 (The Transport Layer Security (TLS) Protocol Version 1.3)

Section 2 says:

The handshake protocol allows peers to negotiate a protocol version, select cryptographic algorithms, optionally authenticate each other, and establish shared secret keying material.

Notes:

Only client authentication is optional (albeit, server authentication is implicit for PSK-only key exchange mode)

Paul Wouters(AD): corrected with the following text:

The handshake protocol allows peers to negotiate a protocol version, select cryptographic algorithms, authenticate each other (with client authentication being optional), and establish shared secret keying material.
The original description is imprecise about the optionality of authentication.  The corrected text clarifies that client authentication is optional, but server authentication is generally required. This is a clarification rather than a correction of an error affecting implementation.

## Missing constraints due to missing entities

Errata 6157 from RFC 7170 (Tunnel Extensible Authentication Protocol (TEAP) Version 1)

Section 4.2.9 says:

  Status

      The Status field is one octet.  This indicates the result if the
      server does not process the action requested by the peer.

It should say:

  Status

      The Status field is one octet.  This indicates the result if the
      party who receives this TLV does not process the action.

Notes:

The status field is carried in the "Request-Action" frame.  As is stated at the start of the section, the frame can be sent either by the server or the peer.
The original description of the Status field is ambiguous because it only refers to the server's processing. The correction clarifies that the Status field indicates the result if either the server or the peer does not process the action. This ambiguity impacts implementation, as developers may only consider server-side processing for the Status field, potentially leading to incorrect handling of the field when the peer does not process the action.

## Missing constraints due to missing cases or situations

Errata 4673 from RFC 7420 (Path Computation Element Communication Protocol (PCEP) Management Information Base (MIB) Module)

Section 4.1 says:

pcePcepSessState OBJECT-TYPE
       SYNTAX      INTEGER {
                      tcpPending(1),
                      openWait(2),
                      keepWait(3),
                      sessionUp(4)
                   }
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The current state of the session.

            The set of possible states excludes the idle state since
            entries do not exist in this table in the idle state."
       ::= { pcePcepSessEntry 3 }

It should say:

pcePcepSessState OBJECT-TYPE
       SYNTAX      INTEGER {
                      idle(0),
                      tcpPending(1),
                      openWait(2),
                      keepWait(3),
                      sessionUp(4)
                   }
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The current state of the session."
       ::= { pcePcepSessEntry 3 }

Notes:

As per security consideration, if PCE needs to allow incomming connections from only known PCCs.
Source addresses of PCCs are configured on PCE. If PCEP session on PCE goes down with configured PCCs.
PCE needs to raise notification pcePcepSessDown (i.e. details mentioned below).
Issue is whiling sending the notification pcePcepSessDown, as session state (pcePcepSessState) defined in RFC doesn't include idle state.

I suggest to include idle(0) state for pcePcepSessState. 

   pcePcepSessDown NOTIFICATION-TYPE
       OBJECTS     {
                      pcePcepSessState,
                      pcePcepSessStateLastChange
                   }
       STATUS      current
       DESCRIPTION
           "This notification is sent when the value of
            pcePcepSessState leaves the sessionUp state."
       ::= { pcePcepNotifications 2 }
The original specification omits the "idle" state, while the description mentions it and the notification pcePcepSessDown requires it.  This inconsistency leads to incorrect behavior when transitioning to an idle state, as the MIB doesn't have a way to represent the state before the session is established.  The correction adds the "idle" state, resolving the inconsistency.

# Incorrect/missing references

## Use of entities defined in other documents without references or with irrelevant references

Errata 6263 from RFC 8410 (Algorithm Identifiers for Ed25519, Ed448, X25519, and X448 for Use in the Internet X.509 Public Key Infrastructure)

Section 7 says:

NOTE: There exist some private key import functions that have not picked up the new ASN.1 structure OneAsymmetricKey that is defined in [RFC7748].

It should say:

NOTE: There exist some private key import functions that have not picked up the new ASN.1 structure OneAsymmetricKey that is defined in [RFC5958].

Notes:

RFC7748 does not define or even mention OneAsymmetricKey. The correct reference should be RFC5958 "Asymmetric Key Packages"
The original text incorrectly cites RFC 7748 as the source for the OneAsymmetricKey ASN.1 structure.  The correction cites RFC 5958, which is the correct source. This inconsistency would affect those trying to locate the correct ASN.1 definition.

## References to non-existent sections or documents

Errata 4413 from RFC 7584 (Session Traversal Utilities for NAT (STUN) Message Handling for SIP Back-to-Back User Agents (B2BUAs))

Section 4.4 says:

   Because of forking, a B2BUA might receive multiple answers for a
   single outbound INVITE.  When this occurs, the B2BUA SHOULD follow
   Sections 3.2 or 3.3 for all of those received answers.

It should say:

   Because of forking, a B2BUA might receive multiple answers for a
   single outbound INVITE.  When this occurs, the B2BUA SHOULD follow
   Sections 4.2 or 4.3 for all of those received answers.

Notes:

Sections 3.2 and 3.3 do not exist.  The normative statement should indicate sections 4.2 and 4.3.
The original text refers to non-existent sections (3.2 and 3.3) for handling multiple INVITE answers. The correction points to the correct sections (4.2 and 4.3), resolving the inconsistency. This inconsistency would mislead implementations attempting to correctly handle multiple INVITE answers.
