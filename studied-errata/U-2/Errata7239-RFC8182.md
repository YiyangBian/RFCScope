# Errata 7239 - RFC 8182

- **RFC Title:** The RPKI Repository Delta Protocol (RRDP)
- **RFC Publication Date:** July 2017
- Link to original errata report: [rfc-editor.org/errata/eid7239](https://www.rfc-editor.org/errata/eid7239)

```
Section 3.2 says:


Certificate Authorities that use RRDP MUST include an instance of an
SIA AccessDescription extension in resource certificates they
produce, in addition to the ones defined in [RFC6487]:

It should say:

Certificate Authorities that use RRDP MUST include an instance of an
SIA AccessDescription extension in CA resource certificates they
produce, in addition to the ones defined in [RFC6487]:

Notes:

Between draft-ietf-sidr-delta-protocol-04 and draft-ietf-sidr-delta-protocol-05 a bit of text was removed (perhaps because it was considered redundant). But, unfortunately that snippet helped establish important context as to what types of certificates are expected to contain the id-ad-rpkiNotify accessMethod inside the Subject Information Access extension. The text that was removed:

"""
Relying Parties that do not support this delta protocol MUST MUST NOT
reject a CA certificate merely because it has an SIA extension
containing this new kind of AccessDescription.
"""

From the removed text is is clear that id-ad-rpkiNotify was only expected to show up on CA certificates. However, without the above text, Section 3.2 of RFC 8182 is somewhat ambiguous whether 'resource certificates' is inclusive of EE certificates or not.

RFC 6487 Section 4.8.8.2 sets expectations that only id-ad-signedObject is expected to show up in the SIA of EE certificates "Other AccessMethods MUST NOT be used for an EE certificates's SIA."

The ambiguity in RFC8182 led to one RIR including id-ad-rpkiNotify in the SIA of the EE certificate of all signed objects they produce (such as ROAs). The RIR indicated they'll work to remove id-ad-rpkiNotify from all EE certificates their CA implementation produces.

It should be noted that the presence of id-ad-rpkiNotify in EE certificates is superfluous; Relying Parties can't use the rpkiNotify accessMethod in EE certificates for any purpose in the validation decision tree.

(Verifying this Errata does not block a future transition from rsync to https; as RFC6487 Section 4.8.8.2 leaves room for additional instances of id-ad-signedObject with non-rsync URIs)
```

## Explanation

The original text is ambiguous about whether the SIA extension containing the id-ad-rpkiNotify accessMethod should be included in all resource certificates or only in CA certificates.  This ambiguity led to different interpretations and implementations.  The corrected text clarifies that it only applies to CA certificates, removing the ambiguity and promoting consistency.
