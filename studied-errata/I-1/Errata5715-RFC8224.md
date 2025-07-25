# Errata 5715 - RFC 8224

- **RFC Title:** Authenticated Identity Management in the Session Initiation Protocol (SIP)
- **RFC Publication Date:** February 2018
- Link to original errata report: [rfc-editor.org/errata/eid5715](https://www.rfc-editor.org/errata/eid5715)

```
Section 4.1 says:


o  Second, the JSON "dest" array MUST be populated.  If the
   destination identity is a telephone number, then the array MUST be
   populated with a JSON object containing a "tn" element with a
   value set to the value of the quoted destination identity, a
   canonicalized telephone number (see Section 8.3).  Otherwise, the
   array MUST be populated with a JSON object containing a "uri"
   element, set to the value of the addr-spec component of the
   To header field, which is the AoR to which the request is being
   sent, per the procedures in Section 8.5.  Multiple JSON objects
   are permitted in "dest" for future compatibility reasons.

...

The "orig" and "dest" arrays may contain identifiers of heterogeneous
type; for example, the "orig" array might contain a "tn" claim, while
the "dest" contains a "uri" claim.  Also note that in some cases, the
"dest" array may be populated with more than one value.  This could,
for example, occur when multiple "dest" identities are specified in a
meshed conference.  Defining how a SIP implementation would align
multiple destination identities in PASSporT with such systems is left
as a subject for future specifications.

It should say:

o  Second, the JSON "dest" object MUST be populated.  If the
   destination identity is a telephone number, then the object MUST
   contain a "tn" element with a value set to an array containing the
   value of the quoted destination identity, a
   canonicalized telephone number (see Section 8.3).  Otherwise, the
   object MUST contain a "uri" element, set to an array containing
   the value of the addr-spec component of the
   To header field, which is the AoR to which the request is being
   sent, per the procedures in Section 8.5.  Additional elements
   are permitted in "dest" for future compatibility reasons.

...

The "orig" and "dest" objects may contain identifiers of heterogeneous
type; for example, the "orig" object might contain a "tn" claim, while
the "dest" contains a "uri" claim.  Also note that in some cases, the
"dest" object may be populated with more than one claim, and its claim
value arrays may contain more than one value.  This could,
for example, occur when multiple "dest" identities are specified in a
meshed conference.  Defining how a SIP implementation would align
multiple destination identities in PASSporT with such systems is left
as a subject for future specifications.

Notes:

The description of the "dest" element does not match RFC8225 or the example that is provided in this section.

The terminology is a bit less clear than in RFC8225 section 5.2.1, in that no differentiation is made between the top level "claims" and embedded "identity claims". The proposed correction does not address this lack of clarity, however.

From RFC8225 section 5.2.1:

The "dest" claim is a JSON object with the claim name of "dest" and
MUST have at least one identity claim object.  The "dest" claim value
is an array containing one or more identity claim JSON objects
representing the destination identities of any type (currently "tn"
or "uri").  If the "dest" claim value array contains both "tn" and
"uri" claim names, the JSON object should list the "tn" array first
and the "uri" array second.  Within the "tn" and "uri" arrays, the
identity strings should be put in lexicographical order, including
the scheme-specific portion of the URI characters.

(The above text might need correction as well, because it refers to the '"dest" claim value array'.)
```

## Explanation

The original description of the "dest" element is inconsistent with RFC 8225 and the provided example. The original description uses an array for the "dest" element, while RFC 8225 and the example use an object containing arrays for telephone numbers and URIs.  The corrected description uses an object containing arrays, aligning with RFC 8225 and the example.
