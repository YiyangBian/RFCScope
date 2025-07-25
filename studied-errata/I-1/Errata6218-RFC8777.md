# Errata 6218 - RFC 8777

- **RFC Title:** DNS Reverse IP Automatic Multicast Tunneling (AMT) Discovery
- **RFC Publication Date:** April 2020
- Link to original errata report: [rfc-editor.org/errata/eid6218](https://www.rfc-editor.org/errata/eid6218)

```
Section 4.3.2 says:


10   IN TYPE260  \# (
       18 ; length
       0a ; precedence=10
       02 ; D=0, relay type=2, an IPv6 address
       20010db800000000000000000000000f ) ; 2001:db8::15
10   IN TYPE260  \# (
       24 ; length
       80 ; precedence=128
       83 ; D=1, relay type=3, a wire-encoded domain name
       09616d7472656c617973076578616d706c6503636f6d ) ; domain name

It should say:

10   IN TYPE260  \# (
       18 ; length
       0a ; precedence=10
       02 ; D=0, relay type=2, an IPv6 address
       20010db8000000000000000000000015 ) ; 2001:db8::15
10   IN TYPE260  \# (
       25 ; length
       80 ; precedence=128
       83 ; D=1, relay type=3, a wire-encoded domain name
       09616d7472656c617973076578616d706c6503636f6d00 ) ; domain name

Notes:

In the first example, the IPv6 address is incorrectly encoded.

In the second example, the trailing root label of the domain name was not included, and should be.  This also increases the length by 1 byte.
```

## Explanation

The erratum points out two errors in the examples in Section 4.3.2 of RFC 8777. The first error is an incorrect encoding of an IPv6 address, and the second error is the omission of a trailing null byte in a domain name encoding.  Both errors are directly related to the correct implementation of the AMT discovery mechanism and will lead to incorrect interpretation of the data, therefore, the classification is INCONSISTENT.
