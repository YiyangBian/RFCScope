import os
import argparse

from utils.analyze_rfcs import main as analyze

parser = argparse.ArgumentParser(description="Analyze an RFC")
parser.add_argument("rfc_number", type=str, help="The RFC number of the RFC to analyze")
parser.add_argument(
    "output_directory",
    type=str,
    help="Path to the directory where the output files will be saved",
)

args = parser.parse_args()
results_path = os.path.join(args.output_directory, f"results")

print(f"Starting analysis of RFC {args.rfc_number}.")
print(f"Output directory: {results_path}")

# Run for inconsistencies
print(f"\nAnalyzing RFC {args.rfc_number} for inconsistencies.")
analyze(
    rfc_number=args.rfc_number,
    section_dependency_graph_path=os.path.join(
        args.output_directory, "section_dependencies.json"
    ),
    corpus_path=os.path.join(args.output_directory, "corpus.json"),
    error_type=0,
    output_dir=os.path.join(results_path, "inconsistencies"),
)
print(
    f"Inconsistencies analysis completed. Results saved to {os.path.join(results_path, 'inconsistencies')}."
)

# Run for underspecifications
print(f"\nAnalyzing RFC {args.rfc_number} for underspecifications.")
analyze(
    rfc_number=args.rfc_number,
    section_dependency_graph_path=os.path.join(
        args.output_directory, "section_dependencies.json"
    ),
    corpus_path=os.path.join(args.output_directory, "corpus.json"),
    error_type=1,
    output_dir=os.path.join(results_path, "underspecifications"),
)
print(
    f"Underspecifications analysis completed. Results saved to {os.path.join(results_path, 'underspecifications')}."
)
