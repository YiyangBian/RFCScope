# Errata 3915 - RFC 7159

- **RFC Title:** The JavaScript Object Notation (JSON) Data Interchange Format
- **RFC Publication Date:** March 2014
- Link to original errata report: [rfc-editor.org/errata/eid3915](https://www.rfc-editor.org/errata/eid3915)

```
Section 12 says:


   Since JSON's syntax is borrowed from JavaScript, it is possible to
   use that language's "eval()" function to parse JSON texts.

It should say:

   Since JSON's syntax is borrowed from JavaScript, it is possible to
   use that language's "eval()" function to parse most (but not all)
   JSON texts.

Notes:

This wording may be construed as meaning that every compliant JSON text is parseable as JavaScript, which is not the case: <http://timelessrepo.com/json-isnt-a-javascript-subset>. (Actually I would prefer this to be stated clearly elsewhere in the document, e.g. where it says "JSON's design goals were for it to be [...] a subset of JavaScript".)

 --VERIFIER NOTES-- 
As per the above citation, there are characters (in particular line terminators like U+2028 and U+2029) which are permissible in JSON but not permissible in JavaScript. The corrected text makes this clearer.
```

## Explanation

The original statement implies that all valid JSON is directly parseable by JavaScript's eval(), which is incorrect. The correction acknowledges that some JSON texts may not be parseable with eval() due to differences in permitted characters between JSON and JavaScript. This inconsistency impacts implementations that rely on eval() for JSON parsing, potentially leading to errors or security vulnerabilities when processing non-compliant JSON.
