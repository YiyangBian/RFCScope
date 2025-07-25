# Errata 8133 - RFC 9656

- **RFC Title:** A YANG Data Model for Microwave Topology
- **RFC Publication Date:** September 2024
- Link to original errata report: [rfc-editor.org/errata/eid8133](https://www.rfc-editor.org/errata/eid8133)

```
Section B.1 says:


   {
    "ietf-interfaces:interfaces": {
     "interface": [
      {
       "name": "L2Interface1",
       "description": "'Ethernet Interface 1'",
       "type": "iana-if-type:ethernetCsmacd"
      },
      {
       "name": "L2Interface2",
       "description": "'Ethernet Interface 2'",
       "type": "iana-if-type:ethernetCsmacd"
      },
      {
       "name": "RLT-1",
       "description": "'Radio Link Terminal 1'",
       "type": "iana-if-type:microwaveRadioLinkTerminal",
       "ietf-microwave-radio-link:mode":
         "ietf-microwave-types:two-plus-zero",
       "ietf-microwave-radio-link:carrier-terminations": [
        "CT-1",
        "CT-3"
       ]
      },
      {
       "name": "RLT-2",
       "description": "'Radio Link Terminal 2'",
       "type": "iana-if-type:microwaveRadioLinkTerminal",
       "ietf-microwave-radio-link:mode":
          "ietf-microwave-types:two-plus-zero",
       "ietf-microwave-radio-link:carrier-terminations": [
        "CT-2",
        "CT-4"
       ]
      },
      {
       "name": "CT-1",
       "description": "'Carrier Termination 1'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10728000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      },
      {
       "name": "CT-3",
       "description": "'Carrier Termination 3'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10528000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      },
      {
       "name": "CT-2",
       "description": "'Carrier Termination 2'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10615000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      },
      {
       "name": "CT-4",
       "description": "'Carrier Termination 4'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10415000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      }
     ]
    },
    "ietf-network:networks": {
     "network": [
      {
       "network-id": "L2-network",
       "network-types": {
        "ietf-te-topology:te-topology": {
         "ietf-eth-te-topology:eth-tran-topology": {}
        }
       },
       "supporting-network": [
        {
         "network-ref": "mw-network"
        }
       ],
       "node": [
        {
         "node-id": "L2-N1",
         "supporting-node": [
          {
           "network-ref": "mw-network",
           "node-ref": "mw-N1"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "L2-N1-TP1",
           "supporting-termination-point": [
            {
             "network-ref": "mw-network",
             "node-ref": "mw-N1",
             "tp-ref": "mw-N1-RLTP1"
            }
           ]
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.1",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-eth-te-topology:eth-node": {}
          }
         }
        },
        {
         "node-id": "L2-N2",
         "supporting-node": [
          {
           "network-ref": "mw-network",
           "node-ref": "mw-N2"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "L2-N2-TP2",
           "supporting-termination-point": [
            {
             "network-ref": "mw-network",
             "node-ref": "mw-N2",
             "tp-ref": "mw-N2-RLTP2"
            }
           ]
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.2",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-eth-te-topology:eth-node": {}
          }
         }
        }
       ],
       "ietf-network-topology:link": [
        {
         "link-id": "L2-N1-N2",
         "source": {
          "source-node": "L2-N1",
          "source-tp": "L2-N1-TP1"
         },
         "destination": {
          "dest-node": "L2-N2",
          "dest-tp": "L2-N2-TP2"
         },
         "supporting-link": [
          {
           "network-ref": "mw-network",
           "link-ref": "mwrl-N1-N2"
          }
         ],
         "ietf-te-topology:te": {
          "te-link-attributes": {
           "interface-switching-capability": [
            {
             "switching-capability": "ietf-te-types:switching-l2sc",
             "encoding": "ietf-te-types:lsp-encoding-ethernet"
            }
           ]
          }
         }
        }
       ]
      },
      {
       "network-id": "mw-network",
       "network-types": {
        "ietf-te-topology:te-topology": {
         "ietf-microwave-topology:mw-topology": {}
        }
       },
       "supporting-network": [
        {
         "network-ref": "mw-network"
        }
       ],
       "node": [
        {
         "node-id": "mw-N1",
         "supporting-node": [
          {
           "network-ref": "mw-network",
           "node-ref": "mw-N1"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "mw-N1-RLTP1",
           "supporting-termination-point": [
            {
             "network-ref": "mw-network",
             "node-ref": "mw-N1",
             "tp-ref": "mw-N1-CTP1"
            },
            {
             "network-ref": "mw-network",
             "node-ref": "mw-N1",
             "tp-ref": "mw-N1-CTP3"
            }
           ],
           "ietf-te-topology:te-tp-id": "192.0.2.3",
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-rltp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
            "RLT-1"
           }
          },
          {
           "tp-id": "mw-N1-CTP1",
           "ietf-te-topology:te-tp-id": 1,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
            "CT-1"
           }
          },
          {
           "tp-id": "mw-N1-CTP3",
           "ietf-te-topology:te-tp-id": 2,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
            "CT-3"
           }
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.1",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-microwave-topology:mw-node": {}
          }
         }
        },
        {
         "node-id": "mw-N2",
         "supporting-node": [
          {
           "network-ref": "mw-network",
           "node-ref": "mw-N2"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "mw-N2-RLTP2",
           "supporting-termination-point": [
            {
             "network-ref": "mw-network",
             "node-ref": "mw-N2",
             "tp-ref": "mw-N2-CTP2"
            },
            {
             "network-ref": "mw-network",
             "node-ref": "mw-N2",
             "tp-ref": "mw-N2-CTP4"
            }
           ],
           "ietf-te-topology:te-tp-id": "192.0.2.4",
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-rltp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
            "RLT-2"
           }
          },
          {
           "tp-id": "mw-N2-CTP2",
           "ietf-te-topology:te-tp-id": 1,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
            "CT-2"
           }
          },
          {
           "tp-id": "mw-N2-CTP4",
           "ietf-te-topology:te-tp-id": 2,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
            "CT-4"
           }
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.1",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-microwave-topology:mw-node": {}
          }
         }
        }
       ],
       "ietf-network-topology:link": [
        {
         "link-id": "mwrl-N1-N2",
         "source": {
          "source-node": "mw-N1",
          "source-tp": "mw-N1-RLTP1"
         },
         "destination": {
          "dest-node": "mw-N2",
          "dest-tp": "mw-N2-RLTP2"
         },
         "ietf-te-topology:te": {
          "bundled-links": {
           "bundled-link": [
            {
             "sequence": 1,
             "src-tp-ref": "mw-N1-CTP1",
             "des-tp-ref": "mw-N2-CTP2"
            },
            {
             "sequence": 2,
             "src-tp-ref": "mw-N1-CTP3",
             "des-tp-ref": "mw-N2-CTP4"
            }
           ]
          },
          "te-link-attributes": {
           "ietf-microwave-topology:mw-link": {
            "microwave-radio-link": {
             "rlt-mode": {
              "num-bonded-carriers": 2,
              "num-protecting-carriers": 0
             }
            }
           }
          }
         }
        },
        {
         "link-id": "mwc-N1-N2-A",
         "source": {
          "source-node": "mw-N1",
          "source-tp": "mw-N1-CTP1"
         },
         "destination": {
          "dest-node": "mw-N2",
          "dest-tp": "mw-N2-CTP2"
         },
         "ietf-te-topology:te": {
          "te-link-attributes": {
           "ietf-bandwidth-availability-topology:link-availability": [
            {
             "availability": "0.99",
             "link-bandwidth": "998423"
            },
            {
             "availability": "0.95",
             "link-bandwidth": "1048576"
            }
           ],
           "ietf-microwave-topology:mw-link": {
            "microwave-carrier": {
             "tx-frequency": 10728000,
             "channel-separation": 28000
            }
           }
          }
         }
        },
        {
         "link-id": "mwc-N1-N2-B",
         "source": {
          "source-node": "mw-N1",
          "source-tp": "mw-N1-CTP3"
         },
         "destination": {
          "dest-node": "mw-N2",
          "dest-tp": "mw-N2-CTP4"
         },
         "ietf-te-topology:te": {
          "te-link-attributes": {
           "ietf-microwave-topology:mw-link": {
            "microwave-carrier": {
             "tx-frequency": 10528000,
             "channel-separation": 28000
            }
           }
          }
         }
        }
       ]
      }
     ]
    }
   }

It should say:

   {
    "ietf-interfaces:interfaces": {
     "interface": [
      {
       "name": "L2Interface1",
       "description": "'Ethernet Interface 1'",
       "type": "iana-if-type:ethernetCsmacd"
      },
      {
       "name": "L2Interface2",
       "description": "'Ethernet Interface 2'",
       "type": "iana-if-type:ethernetCsmacd"
      },
      {
       "name": "RLT-1",
       "description": "'Radio Link Terminal 1'",
       "type": "iana-if-type:microwaveRadioLinkTerminal",
       "ietf-microwave-radio-link:mode":
         "ietf-microwave-types:two-plus-zero",
       "ietf-microwave-radio-link:carrier-terminations": [
        "CT-1",
        "CT-3"
       ]
      },
      {
       "name": "RLT-2",
       "description": "'Radio Link Terminal 2'",
       "type": "iana-if-type:microwaveRadioLinkTerminal",
       "ietf-microwave-radio-link:mode":
          "ietf-microwave-types:two-plus-zero",
       "ietf-microwave-radio-link:carrier-terminations": [
        "CT-2",
        "CT-4"
       ]
      },
      {
       "name": "CT-1",
       "description": "'Carrier Termination 1'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10728000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      },
      {
       "name": "CT-3",
       "description": "'Carrier Termination 3'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10528000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      },
      {
       "name": "CT-2",
       "description": "'Carrier Termination 2'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10615000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      },
      {
       "name": "CT-4",
       "description": "'Carrier Termination 4'",
       "type": "iana-if-type:microwaveCarrierTermination",
       "ietf-microwave-radio-link:tx-frequency": 10415000,
       "ietf-microwave-radio-link:duplex-distance": 113000,
       "ietf-microwave-radio-link:channel-separation": 28000,
       "ietf-microwave-radio-link:rtpc": {
        "maximum-nominal-power": "20.0"
       },
       "ietf-microwave-radio-link:single": {
        "selected-cm": "ietf-microwave-types:qam-512"
       }
      }
     ]
    },
    "ietf-network:networks": {
     "network": [
      {
       "network-id": "example:L2-network",
       "network-types": {
        "ietf-te-topology:te-topology": {
         "ietf-eth-te-topology:eth-tran-topology": {}
        }
       },
       "supporting-network": [
        {
         "network-ref": "example:mw-network"
        }
       ],
       "node": [
        {
         "node-id": "example:L2-N1",
         "supporting-node": [
          {
           "network-ref": "example:mw-network",
           "node-ref": "example:mw-N1"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "example:L2-N1-TP1",
           "supporting-termination-point": [
            {
             "network-ref": "example:mw-network",
             "node-ref": "example:mw-N1",
             "tp-ref": "example:mw-N1-RLTP1"
            }
           ]
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.1",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-eth-te-topology:eth-node": {}
          }
         }
        },
        {
         "node-id": "example:L2-N2",
         "supporting-node": [
          {
           "network-ref": "example:mw-network",
           "node-ref": "example:mw-N2"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "example:L2-N2-TP2",
           "supporting-termination-point": [
            {
             "network-ref": "example:mw-network",
             "node-ref": "example:mw-N2",
             "tp-ref": "example:mw-N2-RLTP2"
            }
           ]
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.2",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-eth-te-topology:eth-node": {}
          }
         }
        }
       ],
       "ietf-network-topology:link": [
        {
         "link-id": "example:L2-N1-N2",
         "source": {
          "source-node": "example:L2-N1",
          "source-tp": "example:L2-N1-TP1"
         },
         "destination": {
          "dest-node": "example:L2-N2",
          "dest-tp": "example:L2-N2-TP2"
         },
         "supporting-link": [
          {
           "network-ref": "example:mw-network",
           "link-ref": "example:mwrl-N1-N2"
          }
         ],
         "ietf-te-topology:te": {
          "te-link-attributes": {
           "interface-switching-capability": [
            {
             "switching-capability": "ietf-te-types:switching-l2sc",
             "encoding": "ietf-te-types:lsp-encoding-ethernet"
            }
           ]
          }
         }
        }
       ]
      },
      {
       "network-id": "example:mw-network",
       "network-types": {
        "ietf-te-topology:te-topology": {
         "ietf-microwave-topology:mw-topology": {}
        }
       },
       "supporting-network": [
        {
         "network-ref": "example:mw-network"
        }
       ],
       "node": [
        {
         "node-id": "example:mw-N1",
         "supporting-node": [
          {
           "network-ref": "example:mw-network",
           "node-ref": "example:mw-N1"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "example:mw-N1-RLTP1",
           "supporting-termination-point": [
            {
             "network-ref": "example:mw-network",
             "node-ref": "example:mw-N1",
             "tp-ref": "example:mw-N1-CTP1"
            },
            {
             "network-ref": "example:mw-network",
             "node-ref": "example:mw-N1",
             "tp-ref": "example:mw-N1-CTP3"
            }
           ],
           "ietf-te-topology:te-tp-id": "192.0.2.3",
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-rltp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
   	 "RLT-1"
           }
          },
          {
           "tp-id": "example:mw-N1-CTP1",
           "ietf-te-topology:te-tp-id": 1,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
   	 "CT-1"
           }
          },
          {
           "tp-id": "example:mw-N1-CTP3",
           "ietf-te-topology:te-tp-id": 2,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
   	 "CT-3"
           }
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.1",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-microwave-topology:mw-node": {}
          }
         }
        },
        {
         "node-id": "example:mw-N2",
         "supporting-node": [
          {
           "network-ref": "example:mw-network",
           "node-ref": "example:mw-N2"
          }
         ],
         "ietf-network-topology:termination-point": [
          {
           "tp-id": "example:mw-N2-RLTP2",
           "supporting-termination-point": [
            {
             "network-ref": "example:mw-network",
             "node-ref": "example:mw-N2",
             "tp-ref": "example:mw-N2-CTP2"
            },
            {
             "network-ref": "example:mw-network",
             "node-ref": "example:mw-N2",
             "tp-ref": "example:mw-N2-CTP4"
            }
           ],
           "ietf-te-topology:te-tp-id": "192.0.2.4",
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-rltp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
   	 "RLT-2"
           }
          },
          {
           "tp-id": "example:mw-N2-CTP2",
           "ietf-te-topology:te-tp-id": 1,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
   	 "CT-2"
           }
          },
          {
           "tp-id": "example:mw-N2-CTP4",
           "ietf-te-topology:te-tp-id": 2,
           "ietf-te-topology:te": {
            "ietf-microwave-topology:mw-tp": {
             "microwave-ctp": {}
            },
            "ietf-tp-interface-reference-topology:tp-to-interface-path":
   	 "CT-4"
           }
          }
         ],
         "ietf-te-topology:te-node-id": "192.0.2.1",
         "ietf-te-topology:te": {
          "te-node-attributes": {
           "ietf-microwave-topology:mw-node": {}
          }
         }
        }
       ],
       "ietf-network-topology:link": [
        {
         "link-id": "example:mwrl-N1-N2",
         "source": {
          "source-node": "example:mw-N1",
          "source-tp": "example:mw-N1-RLTP1"
         },
         "destination": {
          "dest-node": "example:mw-N2",
          "dest-tp": "example:mw-N2-RLTP2"
         },
         "ietf-te-topology:te": {
          "bundled-links": {
           "bundled-link": [
            {
             "sequence": 1,
             "src-tp-ref": "example:mw-N1-CTP1",
             "des-tp-ref": "example:mw-N2-CTP2"
            },
            {
             "sequence": 2,
             "src-tp-ref": "example:mw-N1-CTP3",
             "des-tp-ref": "example:mw-N2-CTP4"
            }
           ]
          },
          "te-link-attributes": {
           "ietf-microwave-topology:mw-link": {
            "microwave-radio-link": {
             "rlt-mode": {
              "num-bonded-carriers": 2,
              "num-protecting-carriers": 0
             }
            }
           }
          }
         }
        },
        {
         "link-id": "example:mwc-N1-N2-A",
         "source": {
          "source-node": "example:mw-N1",
          "source-tp": "example:mw-N1-CTP1"
         },
         "destination": {
          "dest-node": "example:mw-N2",
          "dest-tp": "example:mw-N2-CTP2"
         },
         "ietf-te-topology:te": {
          "te-link-attributes": {
           "ietf-bandwidth-availability-topology:link-availability": [
            {
             "availability": "0.99",
             "link-bandwidth": "998423"
            },
            {
             "availability": "0.95",
             "link-bandwidth": "1048576"
            }
           ],
           "ietf-microwave-topology:mw-link": {
            "microwave-carrier": {
             "tx-frequency": 10728000,
             "channel-separation": 28000
            }
           }
          }
         }
        },
        {
         "link-id": "example:mwc-N1-N2-B",
         "source": {
          "source-node": "example:mw-N1",
          "source-tp": "example:mw-N1-CTP3"
         },
         "destination": {
          "dest-node": "example:mw-N2",
          "dest-tp": "example:mw-N2-CTP4"
         },
         "ietf-te-topology:te": {
          "te-link-attributes": {
           "ietf-microwave-topology:mw-link": {
            "microwave-carrier": {
             "tx-frequency": 10528000,
             "channel-separation": 28000
            }
           }
          }
         }
        }
       ]
      }
     ]
    }
   }

Notes:

Fixed URI names to follow RFC8407bis guidelines.

See also https://mailarchive.ietf.org/arch/msg/ccamp/OQ-oLx2smsmdC4dcn6aB9i-hWE8/
```

## Explanation

The example in Annex A.2 uses an inconsistent tx-frequency value (10528000) for the mwc-N1-N2-B link, which should be the same as mwc-N1-N2-A (10728000). This inconsistency affects the understanding and implementation of the example configuration.
