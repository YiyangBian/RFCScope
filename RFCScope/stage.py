import os
import argparse

from context_constructor.get_reference_relations import main as stage_references
from context_constructor.generate_corpus import main as generate_corpus
from context_constructor.chunkify_structured_corpuses import main as extract_references
from context_constructor.get_section_dependencies import (
    main as resolve_section_dependencies,
)

parser = argparse.ArgumentParser(
    description="Stage an RFC for analysis by constructing its context."
)
parser.add_argument("rfc_number", type=str, help="The RFC number of the RFC to stage")
parser.add_argument(
    "output_directory",
    type=str,
    help="Path to the directory where the output files will be saved",
)

args = parser.parse_args()

print(f"Preparing RFC {args.rfc_number} for analysis by constructing its context.")
print(f"Output directory: {args.output_directory}")

# Create the output directory if it does not exist
os.makedirs(args.output_directory, exist_ok=True)

# Process the references in the RFC
print(f"\nExtracting references from the references section of the RFC.")
stage_references(args.rfc_number, args.output_directory)
print(
    f"References extracted and saved to {os.path.join(args.output_directory, 'references.json')}"
)

# Generate the corpus for the RFC
print(f"\nParsing the contents of the RFC.")
generate_corpus(args.rfc_number, args.output_directory)
print(
    f"Contents parsed and saved to {os.path.join(args.output_directory, 'corpus.json')}"
)

# Extract references from the RFC
print(f"\nExtracting references from the RFC content.")
extract_references(
    os.path.join(args.output_directory, "corpus.json"),
    os.path.join(args.output_directory, "references.json"),
)
print(
    f"References extracted and {os.path.join(args.output_directory, 'corpus.json')} updated with extracted references."
)

# Resolve section dependencies in the RFC
print(f"\nConsolidating and resolving all references in the RFC.")
resolve_section_dependencies(
    os.path.join(args.output_directory, "corpus.json"),
    os.path.join(args.output_directory, "references.json"),
    args.output_directory,
)
print(
    f"References resolved and saved to {os.path.join(args.output_directory, 'section_dependencies.json')}"
)

print(
    f"\nRFC {args.rfc_number} staged successfully for analysis. All files are saved in {args.output_directory}."
)
