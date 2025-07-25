# Errata 5878 - RFC 8288

- **RFC Title:** Web Linking
- **RFC Publication Date:** October 2017
- Link to original errata report: [rfc-editor.org/errata/eid5878](https://www.rfc-editor.org/errata/eid5878)

```
Section B.2 says:


       15.  Let star_param_names be the set of param_names in the
            (param_name, param_value) tuples of link_parameters where
            the last character of param_name is an asterisk ("*").
       16.  For each star_param_name in star_param_names:
            1.  Let base_param_name be star_param_name with the last
                character removed.
            2.  If the implementation does not choose to support an
                internationalised form of a parameter named
                base_param_name for any reason (including, but not
                limited to, it being prohibited by the parameter's
                specification), remove all tuples from link_parameters
                whose first member is star_param_name, and skip to the
                next star_param_name.
            3.  Remove all tuples from link_parameters whose first
                member is base_param_name.
            4.  Change the first member of all tuples in link_parameters
                whose first member is star_param_name to
                base_param_name.

It should say:

       15.  Let star_param_names be the set of param_names in the
            (param_name, param_value) tuples of target_attributes where
            the last character of param_name is an asterisk ("*").
       16.  For each star_param_name in star_param_names:
            1.  Let base_param_name be star_param_name with the last
                character removed.
            2.  If the implementation does not choose to support an
                internationalised form of a parameter named
                base_param_name for any reason (including, but not
                limited to, it being prohibited by the parameter's
                specification), remove all tuples from target_attributes
                whose first member is star_param_name, and skip to the
                next star_param_name.
            3.  Remove all tuples from target_attributes whose first
                member is base_param_name.
            4.  Change the first member of all tuples in target_attributes
                whose first member is star_param_name to
                base_param_name.

Notes:

The modified link_parameters value is not used, but target_attributes is. Additionally, the normative part of the document states that the RFC 8187 decoding scheme MAY be used for target attributes (especially extension attributes), not the ones that belong to the general link model.
```

## Explanation

The algorithm description uses the variable `link_parameters` which is not used in the algorithm but `target_attributes` which is the correct variable to use.  The algorithm is therefore inconsistent with its own definition.
