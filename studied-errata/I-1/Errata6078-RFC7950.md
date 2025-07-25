# Errata 6078 - RFC 7950

- **RFC Title:** The YANG 1.1 Data Modeling Language
- **RFC Publication Date:** August 2016
- Link to original errata report: [rfc-editor.org/errata/eid6078](https://www.rfc-editor.org/errata/eid6078)

```
Section 6.4. says:


   For example, consider the following definition:

     leaf lxiv {
       type decimal64 {
         fraction-digits 18;
       }
       must ". <= 10";
     }

   An instance of the "lxiv" leaf having the value of
   10.0000000000000001 will then successfully pass validation.

It should say:

   For example, consider the following definition:

     leaf lxiv {
       type decimal64 {
         fraction-digits 18;
       }
       must ". <= 9";
     }

   An instance of the "lxiv" leaf having the value of
   9.0000000000000001 will then successfully pass validation.

Notes:

Value 10.0000000000000001 is not a valid decimal64 value with 18 fraction digits as per Section 9.3.4.
```

## Explanation

The original example uses a decimal64 value (10.0000000000000001) that is not valid given the specified constraints (fraction-digits 18 and must ". <= 10").  The correction uses a valid value (9.0000000000000001), making the example consistent. This inconsistency would lead to implementations incorrectly validating the example.
