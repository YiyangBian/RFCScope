# Errata 7303 - RFC 8446

- **RFC Title:** The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC Publication Date:** August 2018
- Link to original errata report: [rfc-editor.org/errata/eid7303](https://www.rfc-editor.org/errata/eid7303)

```
Section 6.1 says:


This alert notifies the recipient that the sender will not send any more messages on this connection. 

It should say:

This alert notifies the recipient that the sender will not send any more messages on this connection. close_notify alerts should be sent with a severity level of WARNING.

Notes:

Apparently, TLS/1.0 specified these should be set to WARNING, not FATAL, but this text got lost somewhere along the way. https://github.com/pion/dtls/issues/195

OpenSSL/NSS both send as WARNING, and servers that have tried sending as FATAL have encountered compatibility problems with clients which treat FATAL alerts differently than WARNING alerts: e.g. https://source.chromium.org/chromium/chromium/src/+/main:third_party/boringssl/src/ssl/tls_record.cc;l=591;drc=c0872c02015009bf3dbab0a83c0452d141e8e9cf?q=tls_open_record&ss=chromium%2Fchromium%2Fsrc

Paul Wouters(AD): Resolved but with the following Corrected Text:

close_notify:  This alert notifies the recipient that the sender will not send any more messages on this connection.  Any data received after a closure alert has been received MUST be ignored. This alert MUST be sent with AlertLevel=warning.
```

## Explanation

The original text does not specify the severity level for close_notify alerts, while the corrected text specifies that close_notify alerts MUST be sent with a severity level of WARNING. This inconsistency may lead to interoperability issues between implementations that treat alerts with different severity levels differently.
