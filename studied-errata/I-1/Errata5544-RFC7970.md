# Errata 5544 - RFC 7970

- **RFC Title:** The Incident Object Description Exchange Format Version 2
- **RFC Publication Date:** November 2016
- Link to original errata report: [rfc-editor.org/errata/eid5544](https://www.rfc-editor.org/errata/eid5544)

```
Section 8 says:


 <xs:element name="Node">
      <xs:complexType>
        <xs:sequence>
          <xs:choice maxOccurs="unbounded">
            <xs:element ref="iodef:DomainData"
                        minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref="iodef:Address"
                        minOccurs="0" maxOccurs="unbounded"/>
          </xs:choice>
          <xs:element ref="iodef:PostalAddress" minOccurs="0"/>
          <xs:element ref="iodef:Location"
                      minOccurs="0" maxOccurs="unbounded"/>
          <xs:element ref="iodef:Counter"
                      minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>

It should say:

 <xs:element name="Node">
      <xs:complexType>
        <xs:sequence>
          <xs:choice maxOccurs="unbounded">
            <xs:element ref="iodef:DomainData"
                        maxOccurs="unbounded"/>
            <xs:element ref="iodef:Address"
                        maxOccurs="unbounded"/>
          </xs:choice>
          <xs:element ref="iodef:PostalAddress" minOccurs="0"/>
          <xs:element ref="iodef:Location"
                      minOccurs="0" maxOccurs="unbounded"/>
          <xs:element ref="iodef:Counter"
                      minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>

Notes:

Section 3.18 says as follows:

"DomainData
      Zero or more.  The domain (DNS) information associated with this
      node.  If an Address is not provided, at least one DomainData MUST
      be specified.  See Section 3.19.

   Address
      Zero or more.  The hardware, network, or application address of
      the node.  If a DomainData is not provided, at least one Address
      MUST be specified.  See Section 3.18.1."

To comply with the above definition, "minOccurs" attribute for both DomainData and Address elements need to be removed. (Current schema allows to omit both of the elements, but the RFC says that at least one of them need to be presented.)
```

## Explanation

The original schema allows both DomainData and Address elements to be omitted, while the specification in section 3.18 requires at least one of them to be present.  The corrected schema removes the minOccurs="0" attribute from both elements to enforce this requirement, resolving the inconsistency.
