# Errata 6620 - RFC 8910

- **RFC Title:** Captive-Portal Identification in DHCP and Router Advertisements (RAs)
- **RFC Publication Date:** September 2020
- Link to original errata report: [rfc-editor.org/errata/eid6620](https://www.rfc-editor.org/errata/eid6620)

```
Section 2 says:


   A captive portal MAY do content negotiation (Section 3.4 of
   [RFC7231]) and attempt to redirect clients querying without an
   explicit indication of support for the captive portal API content
   type (i.e., without application/capport+json listed explicitly
   anywhere within an Accept header field as described in Section 5.3 of
   [RFC7231]).  In so doing, the captive portal SHOULD redirect the
   client to the value associated with the "user-portal-url" API key.
   When performing such content negotiation (Section 3.4 of [RFC7231]),
   implementors of captive portals need to keep in mind that such
   responses might be cached, and therefore SHOULD include an
   appropriate Vary header field (Section 7.1.4 of [RFC7231]) or set the
   Cache-Control header field in any responses to "private" or a more
   restrictive value such as "no-store" (Section 5.2.2.3 of [RFC7234]).

It should say:

   A captive portal MAY do content negotiation (Section 3.4 of
   [RFC7231]) and attempt to redirect clients querying without an
   explicit indication of support for the captive portal API content
   type (i.e., without application/captive+json listed explicitly
   anywhere within an Accept header field as described in Section 5.3 of
   [RFC7231]).  In so doing, the captive portal SHOULD redirect the
   client to the value associated with the "user-portal-url" API key.
   When performing such content negotiation (Section 3.4 of [RFC7231]),
   implementors of captive portals need to keep in mind that such
   responses might be cached, and therefore SHOULD include an
   appropriate Vary header field (Section 7.1.4 of [RFC7231]) or set the
   Cache-Control header field in any responses to "private" or a more
   restrictive value such as "no-store" (Section 5.2.2.3 of [RFC7234]).

Notes:

In RFC8908 the relevant Content-Type is defined as "application/captive+json" and not "application/capport+json".
```

## Explanation

The original text uses the incorrect content type "application/capport+json". The correction uses the correct content type, "application/captive+json", which is consistent with RFC 8908.
