# Errata 7336 - RFC 9115

- **RFC Title:** An Automatic Certificate Management Environment (ACME) Profile for Generating Delegated Certificates
- **RFC Publication Date:** September 2021
- Link to original errata report: [rfc-editor.org/errata/eid7336](https://www.rfc-editor.org/errata/eid7336)

```
Section Appendix A says:


   oid = text .regexp "([0-2])((\.0)|(\.[1-9][0-9]*))*"


It should say:

   oid = text .regexp "([0-2])((\\.0)|(\\.[1-9][0-9]*))*"


Notes:

Backslashes need to be doubled in CDDL strings (as they are done in Appendix B).

An alternative fix would be to replace \\. by [.]

Note that the equivalent fix is not required for

   regtext = text .regexp "([^\*].*)|([\*][^\*].*)|([\*][\*].+)"

as the fact that the single backslashes have no effect is irrelevant here — the backslashes are not needed in the character classes [...].
As an editorial enhancement, the backslashes could be entirely removed from this line.
```

## Explanation

The original regular expression for the oid parameter incorrectly uses single backslashes instead of double backslashes to escape the period character in the CDDL string.  The correction uses double backslashes to properly escape the period, making the regular expression consistent with the CDDL syntax.
