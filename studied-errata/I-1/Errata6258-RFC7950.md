# Errata 6258 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid6258](https://www.rfc-editor.org/errata/eid6258)

```
Section 5.6.5 says:


For example, with these modules:

     module a {
       yang-version 1.1;
       namespace "urn:example:a";
       prefix "a";

       import b {
         revision-date 2015-01-01;
       }
       import c;

       revision 2015-01-01;


It should say:

For example, with these modules:

     module a {
       yang-version 1.1;
       namespace "urn:example:a";
       prefix "a";

       import b {
         revision-date 2015-01-01;
         prefix b;
       }
       import c {
         prefix c;
       }

       revision 2015-01-01;


Notes:

As is considered in 7.1.5, The mandatory "prefix" substatement assigns a prefix for the imported module that is scoped to the importing module or submodule. 

So, there should be a prefix substatement in the "import b" and "import c" statement respectively.
```

## Explanation

The original example omits the mandatory "prefix" substatement within the "import" statements, violating the rules defined in Section 7.1.5. The correction adds the missing "prefix" substatements, making the example consistent with the specification. This inconsistency would affect implementations that rely on the correct usage of the "prefix" substatement within import statements.
