# Errata 7958 - RFC 9562

- **RFC Title:** Universally Unique IDentifiers (UUIDs)
- **RFC Publication Date:** May 2024
- Link to original errata report: [rfc-editor.org/errata/eid7958](https://www.rfc-editor.org/errata/eid7958)

```
Section 4.1 says:


     | 0    | x    | x    | x    | 1-7     | Reserved.  Network      |
     |      |      |      |      |         | Computing System (NCS)  |
     |      |      |      |      |         | backward compatibility, |
     |      |      |      |      |         | and includes Nil UUID   |
     |      |      |      |      |         | as per Section 5.9.     |


It should say:

     | 0    | x    | x    | x    | 0-7     | Reserved.  Network      |
     |      |      |      |      |         | Computing System (NCS)  |
     |      |      |      |      |         | backward compatibility, |
     |      |      |      |      |         | and includes Nil UUID   |
     |      |      |      |      |         | as per Section 5.9.     |


Notes:

This row matches the case where MSB0, MSB1, MSB2, MSB3 are all 0, which would make the variant number 0.
```

## Explanation

The original text incorrectly restricts the version number to 1-7, while version 0 is also valid. The correction changes the range to 0-7, making it consistent with the description and the valid range for version numbers.
