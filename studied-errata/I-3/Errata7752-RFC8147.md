# Errata 7752 - RFC 8147

- **RFC Title:** Next-Generation Pan-European eCall
- **RFC Publication Date:** May 2017
- Link to original errata report: [rfc-editor.org/errata/eid7752](https://www.rfc-editor.org/errata/eid7752)

```
Section 13 says:


<?xml version="1.0"?>
<xs:schema
    targetNamespace="urn:ietf:params:xml:ns:EmergencyCallData:control"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:pi="urn:ietf:params:xml:ns:EmergencyCallData:control"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    elementFormDefault="qualified"
    attributeFormDefault="unqualified">
    
    <xs:import namespace="http://www.w3.org/XML/1998/namespace"/>
    
    <xs:element name="EmergencyCallData.Control"
        type="pi:controlType"/>
    
    <xs:complexType name="controlType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:choice>
                    <xs:element name="capabilities"
                        type="pi:capabilitiesType"/>
                    <xs:element name="request" type="pi:requestType"/>
                    <xs:element name="ack" type="pi:ackType"/>
                    <xs:any namespace="##any" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:choice>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
    
    <xs:complexType name="ackType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:sequence minOccurs="1" maxOccurs="unbounded">
                    <xs:element name="actionResult" minOccurs="0"
                        maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:attribute name="action"
                                type="xs:token"
                                use="required"/>
                            <xs:attribute name="success"
                                type="xs:boolean"
                                use="required"/>
                            <xs:attribute name="reason"
                                type="xs:token">
                                <xs:annotation>
                                    <xs:documentation>
                                        conditionally mandatory
                                        when @success="false"
                                        to indicate reason code
                                        for a failure
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:attribute>
                            <xs:attribute name="details"
                                type="xs:string"/>
                            <xs:anyAttribute
                                processContents="skip"/>
                        </xs:complexType>
                    </xs:element>
                    <xs:any namespace="##any" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="ref"
                    type="xs:anyURI"
                    use="required"/>
                
                <xs:attribute name="received"
                    type="xs:boolean"/>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
    
    <xs:complexType name="capabilitiesType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:sequence minOccurs="1" maxOccurs="unbounded">
                    <xs:element name="request"
                        type="pi:requestType"
                        minOccurs="1"
                        maxOccurs="unbounded"/>
                    <xs:any namespace="##any" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
    
    <xs:complexType name="requestType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:choice minOccurs="1" maxOccurs="unbounded">
                    <xs:element name="text" minOccurs="0"
                        maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:simpleContent>
                                <xs:extension base="xs:string">
                                    <xs:anyAttribute
                                        namespace="##any"
                                        processContents="skip"/>
                                </xs:extension>
                            </xs:simpleContent>
                        </xs:complexType>
                    </xs:element>
                    <xs:any namespace="##any" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:choice>
                <xs:attribute name="action" type="xs:token"
                    use="required"/>
                
                <xs:attribute name="int-id" type="xs:unsignedInt"/>
                <xs:attribute name="persistence"
                    type="xs:duration"/>
                <xs:attribute name="datatype" type="xs:token"/>
                <xs:attribute name="supported-values"
                    type="xs:string"/>
                <xs:attribute name="element-id" type="xs:token"/>
                <xs:attribute name="requested-state"
                    type="xs:token"/>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
</xs:schema>

It should say:

<?xml version="1.0"?>
<xs:schema
    targetNamespace="urn:ietf:params:xml:ns:EmergencyCallData:control"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:pi="urn:ietf:params:xml:ns:EmergencyCallData:control"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    elementFormDefault="qualified"
    attributeFormDefault="unqualified">
    
    <xs:import namespace="http://www.w3.org/XML/1998/namespace"/>
    
    <xs:element name="EmergencyCallData.Control"
        type="pi:controlType"/>
    
    <xs:complexType name="controlType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:choice>
                    <xs:element name="capabilities"
                        type="pi:capabilitiesType"/>
                    <xs:element name="request" type="pi:requestType"/>
                    <xs:element name="ack" type="pi:ackType"/>
                    <xs:any namespace="##other" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:choice>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
    
    <xs:complexType name="ackType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:sequence minOccurs="1" maxOccurs="unbounded">
                    <xs:element name="actionResult" minOccurs="0"
                        maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:attribute name="action"
                                type="xs:token"
                                use="required"/>
                            <xs:attribute name="success"
                                type="xs:boolean"
                                use="required"/>
                            <xs:attribute name="reason"
                                type="xs:token">
                                <xs:annotation>
                                    <xs:documentation>
                                        conditionally mandatory
                                        when @success="false"
                                        to indicate reason code
                                        for a failure
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:attribute>
                            <xs:attribute name="details"
                                type="xs:string"/>
                            <xs:anyAttribute
                                processContents="skip"/>
                        </xs:complexType>
                    </xs:element>
                    <xs:any namespace="##other" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="ref"
                    type="xs:anyURI"
                    use="required"/>
                
                <xs:attribute name="received"
                    type="xs:boolean"/>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
    
    <xs:complexType name="capabilitiesType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:sequence minOccurs="1" maxOccurs="unbounded">
                    <xs:element name="request"
                        type="pi:requestType"
                        minOccurs="1"
                        maxOccurs="unbounded"/>
                    <xs:any namespace="##other" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
    
    <xs:complexType name="requestType">
        <xs:complexContent>
            <xs:restriction base="xs:anyType">
                <xs:choice minOccurs="1" maxOccurs="unbounded">
                    <xs:element name="text" minOccurs="0"
                        maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:simpleContent>
                                <xs:extension base="xs:string">
                                    <xs:anyAttribute
                                        namespace="##any"
                                        processContents="skip"/>
                                </xs:extension>
                            </xs:simpleContent>
                        </xs:complexType>
                    </xs:element>
                    <xs:any namespace="##other" processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"/>
                </xs:choice>
                <xs:attribute name="action" type="xs:token"
                    use="required"/>
                
                <xs:attribute name="int-id" type="xs:unsignedInt"/>
                <xs:attribute name="persistence"
                    type="xs:duration"/>
                <xs:attribute name="datatype" type="xs:token"/>
                <xs:attribute name="supported-values"
                    type="xs:string"/>
                <xs:attribute name="element-id" type="xs:token"/>
                <xs:attribute name="requested-state"
                    type="xs:token"/>
                <xs:anyAttribute/>
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>
</xs:schema>

Notes:

The complex types "controlType", "ackType", "capabilitiesType" and "requestType" define extension points by using xs:any with namespace ##any. This violates the "Unique Particle Attribution" rule for XSD 1.0 (see: https://www.w3.org/wiki/UniqueParticleAttribution) and shows up as an error in some tools.

I suggest changing the namespace to ##other like it's done in other schemas (for example, RFC7865 defines extension points in this way: https://datatracker.ietf.org/doc/html/rfc7865#section-9 ).

[Verifier note:]

Replace all four occurrences of:

<xs:any namespace="##any" processContents="lax">

with:

<xs:any namespace="##other" processContents="lax">
```

## Explanation

The original schema uses `xs:any namespace="##any"`, which violates the "Unique Particle Attribution" rule for XSD 1.0.  The corrected schema uses `xs:any namespace="##other"`, which resolves this inconsistency and produces a schema that is valid and correctly parses.
