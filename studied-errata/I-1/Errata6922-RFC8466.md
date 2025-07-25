# Errata 6922 - RFC 8466

- **RFC Title:** A YANG Data Model for Layer 2 Virtual Private Network (L2VPN) Service Delivery
- **RFC Publication Date:** October 2018
- Link to original errata report: [rfc-editor.org/errata/eid6922](https://www.rfc-editor.org/errata/eid6922)

```
Section 5.5.2.1 says:


...
             <network-access-id>LA1</network-access-id>
                <service>
                  <svc-bandwidth>
                     <bandwidth>
                       <direction>input-bw</direction>
                        <type>bw-per-cos</type>
                         <cir>450000000</cir>
                         <cbs>20000000</cbs>
                         <eir>1000000000</eir>
                         <ebs>200000000</ebs>
                     </bandwidth>
                    </svc-bandwidth>
...
            <network-access-id>LA2</network-access-id>
                <service>
                  <svc-bandwidth>
                     <bandwidth>
                       <direction>input-bw</direction>
                        <type>bw-per-cos</type>
                         <cir>450000000</cir>
                         <cbs>20000000</cbs>
                         <eir>1000000000</eir>
                         <ebs>200000000</ebs>

It should say:

...
             <network-access-id>LA1</network-access-id>
                <service>
                  <svc-bandwidth>
                     <bandwidth>
                       <direction>input-bw</direction>
                        <type>bw-per-cos</type>
                         <cos-id>10</cos-id>
                         <cir>450000000</cir>
                         <cbs>20000000</cbs>
                         <eir>1000000000</eir>
                         <ebs>200000000</ebs>
                     </bandwidth>
                    </svc-bandwidth>
...
            <network-access-id>LA2</network-access-id>
                <service>
                  <svc-bandwidth>
                     <bandwidth>
                       <direction>input-bw</direction>
                        <type>bw-per-cos</type>
                         <cos-id>10</cos-id>
                         <cir>450000000</cir>
                         <cbs>20000000</cbs>
                         <eir>1000000000</eir>
                         <ebs>200000000</ebs>


Notes:

The cos-id must be included when the bandwidth type is set to "bw-per-cos".
```

## Explanation

The original example omits the required "cos-id" parameter when the "type" attribute is set to "bw-per-cos".  The correction adds the missing "cos-id" parameter, resolving the inconsistency. This inconsistency would lead to implementations incorrectly processing svc-bandwidth configurations.
