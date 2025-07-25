# Errata 5543 - RFC 7970

- **RFC Title:** The Incident Object Description Exchange Format Version 2
- **RFC Publication Date:** November 2016
- Link to original errata report: [rfc-editor.org/errata/eid5543](https://www.rfc-editor.org/errata/eid5543)

```
Section 8 says:


    <xs:element name="Confidence">
      <xs:complexType>
        <xs:attribute name="rating"
                      type="confidence-rating-type" use="required"/>
        <xs:attribute name="ext-rating"
                      type="xs:string" use="optional"/>
      </xs:complexType>
    </xs:element>

It should say:

    <xs:element name="Confidence">
      <xs:complexType>
        <xs:simpleContent>
          <xs:extension base="xs:float">
            <xs:attribute name="rating"
                          type="confidence-rating-type" use="required"/>
            <xs:attribute name="ext-rating"
                          type="xs:string" use="optional"/>
          </xs:extension>
        </xs:simpleContent>
      </xs:complexType>
    </xs:element>

Notes:

Section 3.12.5 says as follows:
  "The content of the class is of type REAL and specifies a numerical
   assessment in the confidence of the data when the value of the rating
   attribute is "numeric".  Otherwise, this element MUST be empty."

The current schema does not allow the confidence class to have the content (REAL type), thus the correction (note the addition of "<xs:extension base="xs:float">") is proposed.
```

## Explanation

The original schema definition for the Confidence element does not allow for a numerical value, while Section 3.12.5 specifies that a numerical assessment of confidence is possible.  The correction includes an xs:extension of xs:float, thus allowing for a numerical value, resolving the inconsistency. This inconsistency would prevent implementations from correctly handling numerical confidence values.
