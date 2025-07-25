# Errata 4948 - RFC 7252

- **RFC Title:** The Constrained Application Protocol (CoAP)
- **RFC Publication Date:** June 2014
- Link to original errata report: [rfc-editor.org/errata/eid4948](https://www.rfc-editor.org/errata/eid4948)

```
Section 5.6 says:


For a presented request, a CoAP endpoint MUST NOT use a stored
response, unless:

o  the presented request method and that used to obtain the stored
   response match,

o  all options match between those in the presented request and those
   of the request used to obtain the stored response (which includes
   the request URI), except that there is no need for a match of any
   request options marked as NoCacheKey (Section 5.4) or recognized
   by the Cache and fully interpreted with respect to its specified
   cache behavior (such as the ETag request option described in
   Section 5.10.6; see also Section 5.4.2), and

o  the stored response is either fresh or successfully validated as
   defined below.

The set of request options that is used for matching the cache entry
is also collectively referred to as the "Cache-Key".

It should say:

For a presented request, a CoAP endpoint MUST NOT use a stored
response, unless:

o  the presented request method and that used to obtain the stored
   response match,

o  all options match between those in the presented request and those
   of the request used to obtain the stored response (which includes
   the request URI), except that there is no need for a match of any
   request options marked as NoCacheKey (Section 5.4) or recognized
   by the Cache and fully interpreted with respect to its specified
   cache behavior (such as the ETag request option described in
   Section 5.10.6; see also Section 5.4.2), 

o  the payload of the presented request and the payload of the
   request used to obtain the stored response match, and

o  the stored response is either fresh or successfully validated as
   defined below.

The set of request options that is used for matching the cache entry
plus (if applicable) the request payload are also collectively referred
to as the "Cache-Key".

Notes:

CoAP servers may return error responses in reply to requests that are invalid at the CoAP level (e.g., 4.02 Bad Option if the client includes an unrecognized option) or at the application level above (e.g., 4.00 Bad Request if the client includes a malformed payload according to application semantics).

If the error response does not depend on the request payload, then it is desirable that repeated requests that differ only in the payload can be satisfied with the same cached response. E.g., repeated requests for a non-existing resource should result in a cached 4.04 Not Found response as often as possible, regardless of the payload, rather than hit the server every time.

If the error response depends on the request payload, then it is not desirable that cached responses are reused for repeated requests that differ only in the payload. E.g., a client should not receive an error response for a valid request payload because another client sent an identical request but with a malformed request payload. In this case, including the request payload in the Cache-Key would give the expected result.

The original text does not include the request in the Cache-Key, which may lead to unexpected results. The corrected text changes that.

Since CoAP does not provide any indication in responses to distinguish between the two cases, caches generally cannot determine whether the response depends on the request payload or not and thus must always include the request payload in the Cache-Key to give the expected result. (As an exception, a cache at an origin server may be able to determine whether a cached response depends on the request payload or not, and thus can reuse responses accordingly. This already applies to responses that do not depend on the request method.)
```

## Explanation

The original specification for cache key matching omits the request payload, leading to inconsistencies in handling cached responses.  The correction includes the request payload in the cache key, ensuring consistent behavior in scenarios where the response depends on the payload.  This inconsistency directly affects cache behavior and may lead to unexpected results in implementations that do not consider the payload when generating the cache key.
