# Errata 6268 - RFC 8489

- **RFC Title:** Session Traversal Utilities for NAT (STUN)
- **RFC Publication Date:** February 2020
- Link to original errata report: [rfc-editor.org/errata/eid6268](https://www.rfc-editor.org/errata/eid6268)

```
Section Appendix B.1 says:


        00 01 00 9c      Request type and message length
        21 12 a4 42      Magic cookie
        78 ad 34 33   }
        c6 ad 72 c0   }  Transaction ID
        29 da 41 2e   }
        00 1e 00 20      USERHASH attribute header
        4a 3c f3 8f   }
        ef 69 92 bd   }
        a9 52 c6 78   }
        04 17 da 0f   }  Userhash value (32 bytes)
        24 81 94 15   }
        56 9e 60 b2   }
        05 c4 6e 41   }
        40 7f 17 04   }
        00 15 00 29      NONCE attribute header
        6f 62 4d 61   }
        74 4a 6f 73   }
        32 41 41 41   }
        43 66 2f 2f   }
        34 39 39 6b   }  Nonce value and padding (3 bytes)
        39 35 34 64   }
        36 4f 4c 33   }
        34 6f 4c 39   }
        46 53 54 76   }
        79 36 34 73   }
        41 00 00 00   }
        00 14 00 0b      REALM attribute header
        65 78 61 6d   }
        70 6c 65 2e   }  Realm value (11 bytes) and padding (1 byte)
        6f 72 67 00   }
        00 1c 00 20      MESSAGE-INTEGRITY-SHA256 attribute header
        e4 68 6c 8f   }
        0e de b5 90   }
        13 e0 70 90   }
        01 0a 93 ef   }  HMAC-SHA256 value
        cc bc cc 54   }
        4c 0a 45 d9   }
        f8 30 aa 6d   }
        6f 73 5a 01   }
 

It should say:

   Password Algorithm: SHA-256 (0x0002), and parameters len (0)

      00 01 00 90     Request type and message length
      21 12 a4 42     Magic cookie
      78 ad 34 33  }
      c6 ad 72 c0  }  Transaction ID
      29 da 41 2e  }
      00 1e 00 20     USERHASH attribute header
      4a 3c f3 8f  }
      ef 69 92 bd  }
      a9 52 c6 78  }
      04 17 da 0f  }  Userhash value (32  bytes)
      24 81 94 15  }
      56 9e 60 b2  }
      05 c4 6e 41  }
      40 7f 17 04  }
      00 15 00 29     NONCE attribute header
      6f 62 4d 61  }
      74 4a 6f 73  }
      32 41 41 41  }
      43 66 2f 2f  }
      34 39 39 6b  }  Nonce value and padding (3 bytes)
      39 35 34 64  }
      36 4f 4c 33  }
      34 6f 4c 39  }
      46 53 54 76  }
      79 36 34 73  }
      41 00 00 00  }
      00 14 00 0b     REALM attribute header
      65 78 61 6d  }
      70 6c 65 2e  }  Realm value (11  bytes) and padding (1 byte)
      6f 72 67 00  }
      00 1d 00 04     PASSWORD-ALGORITHM attribute header
      00 02 00 00     PASSWORD-ALGORITHM value (4 bytes)
      00 1c 00 20     MESSAGE-INTEGRITY-SHA256 attribute header
      b5 c7 bf 00  }
      5b 6c 52 a2  }
      1c 51 c5 e8  }
      92 f8 19 24  }  HMAC-SHA256 value
      13 62 96 cb  }
      92 7c 43 14  }
      93 09 27 8c  }
      c6 51 8e 65  }

Notes:

The message length in the test vector (first line, value: 9c) is the absolute length of the whole test vector. However from section 5. STUN Message Structure

"The message length MUST contain the size of the message in bytes, not
   including the 20-byte STUN header."

So the message length in the header should be 20 bytes less than absolute length of the whole message. 

0x9C - 20 = 0x88.

Also the section was missing an indication of what password algorithm that was to be used to derive the password. As SHA-256 was used, and is not the default the PASSWORD-ALGORITHM attribute is required. Thus, this corrected message contains that STUN attribute. 

The corrected message has a recalculated Message-Integrity-SHA256 attribute.
```

## Explanation

The original example has an incorrect message length value in the STUN header, which does not account for the header's own size.  Additionally, the example omits the PASSWORD-ALGORITHM attribute and uses an incorrect Message-Integrity-SHA256 value. The correction adjusts the message length, adds the PASSWORD-ALGORITHM attribute, and provides the correct Message-Integrity-SHA256 value, resolving these inconsistencies.
