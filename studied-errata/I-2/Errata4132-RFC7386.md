# Errata 4132 - RFC 7386

- **RFC Title:** JSON Merge Patch
- **RFC Publication Date:** October 2014
- Link to original errata report: [rfc-editor.org/errata/eid4132](https://www.rfc-editor.org/errata/eid4132)

```
Section 2 says:


define MergePatch(Target, Patch):
       if Patch is an Object:
         if Target is not an Object:
       Target = {} # Ignore the contents and set it to an empty Object
         for each Name/Value pair in Patch:
       if Value is null:
         if Name exists in Target:
           remove the Name/Value pair from Target
       else:
         Target[Name] = MergePatch(Target[Name], Value)
         return Target
       else:
         return Patch

It should say:

   define MergePatch(Target, Patch):
     if Patch is an Object:
       if Target is not an Object:
         Target = {} # Ignore the contents and set it to an empty Object
       for each Name/Value pair in Patch:
         if Value is null:
           if Name exists in Target:
             remove the Name/Value pair from Target
         else:
           Target[Name] = MergePatch(Target[Name], Value)
       return Target
     else:
       return Patch

Notes:

Indentation of the pseudo-code example was correct in the Internet-Drafts but was messed up in the final version. For instance, "Target = {}" should be under the two ifs. (Reported by James H. Manger on the appsawg mailing list.)

This is a technical erratum, rather than editorial, because the correct indentation is essential to understanding the pseudocode.
```

## Explanation

The incorrect indentation in the pseudocode example of Section 2 changes the algorithm's logic. The original, incorrectly indented code does not correctly implement the intended merge operation.  The erroneous indentation affects the interpretation of the conditional statements, leading to an incorrect merge algorithm and thus impacting the implementation of JSON Merge Patch.  The correction ensures that the pseudocode accurately reflects the intended behavior, resolving the inconsistency.
