# Errata 6301 - RFC 8281

- **RFC Title:** Path Computation Element Communication Protocol (PCEP) Extensions for PCE-Initiated LSP Setup in a Stateful PCE Model
- **RFC Publication Date:** December 2017
- Link to original errata report: [rfc-editor.org/errata/eid6301](https://www.rfc-editor.org/errata/eid6301)

```
Section 5.1 says:


     <PCE-initiated-lsp-request> ::= (<PCE-initiated-lsp-instantiation>|
                                      <PCE-initiated-lsp-deletion>)

     <PCE-initiated-lsp-instantiation> ::= <SRP>
                                           <LSP>
                                           [<END-POINTS>]
                                           <ERO>
                                           [<attribute-list>]

     <PCE-initiated-lsp-deletion> ::= <SRP>
                                      <LSP>


It should say:

     <PCE-initiated-lsp-request> ::= (<PCE-initiated-lsp-instantiation>|
                                      <PCE-initiated-lsp-deletion-or-reclamation>)

     <PCE-initiated-lsp-instantiation> ::= <SRP>
                                           <LSP>
                                           [<END-POINTS>]
                                           <ERO>
                                           [<attribute-list>]

     <PCE-initiated-lsp-deletion-or-reclamation> ::= <SRP>
                                                     <LSP>


Notes:

Update needed to solve ambiguity for any extra object included after SRP and LSP objects in reclaim delegation request, which is coming from:

https://tools.ietf.org/html/rfc8281#section-6
A PCE (either the original or one of its backups) sends a PCInitiate
   message that includes just the SRP and LSP objects and carries the
   PLSP-ID of the LSP it wants to take control of.
```

## Explanation

The original specification is ambiguous about the content of PCE-initiated-lsp-deletion requests.  The correction introduces a new production, <PCE-initiated-lsp-deletion-or-reclamation>, to clarify that both deletion and reclamation requests can include additional objects beyond SRP and LSP.
