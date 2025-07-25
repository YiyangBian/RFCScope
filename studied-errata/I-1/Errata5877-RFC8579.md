# Errata 5877 - RFC 8579

- **RFC Title:** Sieve Email Filtering: Delivering to Special-Use Mailboxes
- **RFC Publication Date:** May 2019
- Link to original errata report: [rfc-editor.org/errata/eid5877](https://www.rfc-editor.org/errata/eid5877)

```
Section 6 says:


require "imapsieve";
require "special-use";
require "environment";
require "variables";

if environment :contains "imap.mailbox" "*" {
    set "mailbox" "${1}";
}

if allof(
    environment "imap.cause" "COPY",
    specialuse_exists "${mailbox}" "\\Junk") {
    redirect "spam-report@example.org";
}


It should say:

require "imapsieve";
require "special-use";
require "environment";
require "variables";

if environment :matches "imap.mailbox" "*" {
    set "mailbox" "${1}";
}

if allof(
    environment "imap.cause" "COPY",
    specialuse_exists "${mailbox}" "\\Junk") {
    redirect "spam-report@example.org";
}


Notes:

The final example is using the ":contains" match type to extract a match variable, which will not work. It should use ":matches" instead.
```

## Explanation

The original example uses the ":contains" match type, which is incorrect for extracting a match variable. The correction uses the ":matches" type, which is the correct match type for this operation.  This inconsistency would affect the operation of the Sieve script.
