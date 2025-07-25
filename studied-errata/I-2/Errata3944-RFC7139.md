# Errata 3944 - RFC 7139

- **RFC Title:** GMPLS Signaling Extensions for Control of Evolving G.709 Optical Transport Networks
- **RFC Publication Date:** March 2014
- Link to original errata report: [rfc-editor.org/errata/eid3944](https://www.rfc-editor.org/errata/eid3944)

```
Section 5.1 says:


      ODUk.ts       Minimum          Nominal          Maximum
      -----------------------------------------------------------
      ODU2.ts    1,249,384.632    1,249,409.620     1,249,434.608
      ODU3.ts    1,254,678.635    1,254,703.729     1,254,728.823
      ODU4.ts    1,301,683.217    1,301,709.251     1,301,735.285

              Table 1: Actual TS Bit Rate of ODUk (in Kbps)


It should say:

      ODTUk.ts       Minimum          Nominal           Maximum
      ------------------------------------------------------------
      ODTU2.ts    1,249,384.632    1,249,409.620     1,249,434.608
      ODTU3.ts    1,254,678.635    1,254,703.729     1,254,728.823
      ODTU4.ts    1,301,683.217    1,301,709.251     1,301,735.285

              Table 1: Actual TS Bit Rate of ODUk (in Kbps)
```

## Explanation

The erratum corrects a typographical error in Table 1, changing "ODUk.ts" to "ODTUk.ts".  While seemingly minor, this inconsistency could lead to implementation issues if an implementation is strictly following the incorrect label in the original text.  The inconsistency is in the naming of the transport units which would directly impact how an implementation would interpret the values in the table.
