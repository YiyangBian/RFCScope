import json
import argparse
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import os
import tiktoken
from retrieval.references import __find_section, get_structured_rfc, __get_flat_sections_list
from collections import defaultdict

encoding = tiktoken.encoding_for_model("o3-mini")


def build_dependency_dict(section_dependencies, corpus):
    """
    Build a dictionary of dependencies from the section dependencies list. The 
    dictionary is closed in the sense that it includes all sections of all RFCs
    in the corpus, even if they have no dependencies (i.e., the dependency list is 
    an empty list).
    
    Args:
        section_dependencies (list): List of section dependencies
        corpus (list): List of RFC documents
        
    Returns:
        dict: Dictionary mapping source nodes to their RFC dependencies
    """
    dependency_dict = {}
    
    for dep in section_dependencies:
        source = (dep['source']['rfc_number'], dep['source']['section_id'])
        if source not in dependency_dict:
            dependency_dict[source] = []
        
        if dep["document_type"] == "RFC":
            target = ("RFC", dep["document_tag"], dep["reference_value"])
            
            if target not in dependency_dict[source]:
                dependency_dict[source].append(target)

        if dep["document_type"] == "EXTERNAL":
            if dep["reference_text"]: 
                target_name = f"{dep['reference_text']} ({dep['document_tag']})"
            else:
                target_name = dep["document_tag"]
            target = ("EXTERNAL", target_name, dep["reference_summary"])

            if target not in dependency_dict[source]:
                dependency_dict[source].append(target)

    # take the closure of the dependency dict
    for rfc in corpus:
        rfc_number = rfc["rfc_number"]
        sections_list = __get_flat_sections_list(rfc["structured_content"])

        for section in sections_list:
            section_id = section["identifier"]
            if (rfc_number, section_id) not in dependency_dict:
                dependency_dict[(rfc_number, section_id)] = []
    
    return dependency_dict


def analyze_dependencies(section_dependencies, corpus):
    """
    Analyze dependencies for each section and count tokens in combined text.
    
    Args:
        section_dependencies (list): List of section dependencies
        corpus (list): List of RFC documents
        
    Returns:
        list: List of dictionaries with source info and token counts
    """    
    # Build a dictionary of dependencies
    dependency_dict = build_dependency_dict(section_dependencies, corpus)
    
    results = []
    
    for source, dependencies in tqdm(dependency_dict.items(), desc="Analyzing dependencies"):
        source_rfc, source_section = source
        
        # organize the dependencies by RFC
        deps = {}
        for dep_type, dep_tag, dep_value in dependencies:
            if dep_type == "RFC":
                dep_rfc = dep_tag
                dep_section = dep_value

                if dep_rfc not in deps:
                    deps[dep_rfc] = []
                deps[dep_rfc].append(dep_section)
        
        for dep_rfc, dep_sections in deps.items():
            sections_to_remove = set()
            
            # remove sections whose parent is also in deps
            for i, dep_section in enumerate(dep_sections):
                if any(parent_section.startswith(dep_section) for parent_section in dep_sections if parent_section != dep_section):
                    sections_to_remove.add(i)

            # remove duplicates
            for i, dep_section in enumerate(dep_sections):
                if dep_section in dep_sections[:i]:
                    sections_to_remove.add(i)
            
            deps[dep_rfc] = [dep_sections[i] for i in range(len(dep_sections)) if i not in sections_to_remove]

        # collect the texts
        texts = []
        
        def get_text(sections):
            for section_id in sections:
                texts.append(sections[section_id]["title"])
                texts.append(sections[section_id]["content"])
                get_text(sections[section_id]["children"])

        # include the section itself
        rfc_contents = get_structured_rfc(source_rfc)
        source_section_contents = __find_section(rfc_contents, source_section)
        get_text({source_section: source_section_contents})
        
        # Get all dependency texts
        for dep_rfc, dep_sections in deps.items():
            dep_rfc_contents = get_structured_rfc(dep_rfc)
            dep_contents_sections = {
                dep_section: __find_section(dep_rfc_contents, dep_section)
                for dep_section in dep_sections
            }           

            get_text(dep_contents_sections)

        # now get external references too
        for dep_type, dep_tag, dep_value in dependencies:
            if dep_type == "EXTERNAL":
                texts.append(dep_tag)
                texts.append(dep_value)

        # Combine all texts
        combined_text = "\n".join(texts)

        # Count tokens
        token_count = len(encoding.encode(combined_text))

        results.append({
            "source_rfc": source_rfc,
            "source_section": source_section,
            "token_count": token_count
        })

    return results


def aggregate_by_section_level(results):
    """
    Aggregate token counts by section level.
    
    Args:
        results (list): Analysis results with token counts
        
    Returns:
        dict: Dict containing aggregated results by section level
    """
    # Group sections by RFC and level
    rfc_sections = defaultdict(lambda: defaultdict(list))
    
    # First, categorize all sections by RFC and level
    for result in results:
        rfc = result["source_rfc"]
        section_id = result["source_section"]
        level = section_id.count(".") + 1
        
        rfc_sections[rfc][level].append({
            "section_id": section_id,
            "token_count": result["token_count"]
        })
    
    # Prepare aggregated results
    level_aggregates = {1: [], 2: [], 3: []}
    
    # Process each RFC
    for rfc, levels in rfc_sections.items():
        # Process level 1 sections (aggregate their children)
        if 1 in levels:
            for l1_section in levels[1]:
                section_id = l1_section["section_id"]
                total_tokens = l1_section["token_count"]
                
                # Add tokens from all children sections
                for level in [2, 3, 4, 5]:  # Check all possible child levels
                    if level in levels:
                        for section in levels[level]:
                            if section["section_id"].startswith(section_id + "."):
                                total_tokens += section["token_count"]
                
                level_aggregates[1].append({
                    "rfc": rfc,
                    "section_id": section_id,
                    "token_count": total_tokens
                })
        
        # Process level 2 sections (aggregate their children)
        if 2 in levels:
            for l2_section in levels[2]:
                section_id = l2_section["section_id"]
                total_tokens = l2_section["token_count"]
                
                # Add tokens from all children sections
                for level in [3, 4, 5]:  # Check all possible child levels
                    if level in levels:
                        for section in levels[level]:
                            if section["section_id"].startswith(section_id + "."):
                                total_tokens += section["token_count"]
                
                level_aggregates[2].append({
                    "rfc": rfc,
                    "section_id": section_id,
                    "token_count": total_tokens
                })
        
        # Process level 3 sections (aggregate their children)
        if 3 in levels:
            for l3_section in levels[3]:
                section_id = l3_section["section_id"]
                total_tokens = l3_section["token_count"]
                
                # Add tokens from all children sections
                for level in [4, 5]:  # Check all possible child levels
                    if level in levels:
                        for section in levels[level]:
                            if section["section_id"].startswith(section_id + "."):
                                total_tokens += section["token_count"]
                
                level_aggregates[3].append({
                    "rfc": rfc,
                    "section_id": section_id,
                    "token_count": total_tokens
                })
    
    # Sort each level by token count
    for level in level_aggregates:
        level_aggregates[level].sort(key=lambda x: x["token_count"], reverse=True)
    
    return level_aggregates

def plot_histogram(data, title, xlabel, ylabel, output_path, bins=20):
    """
    Create and save a histogram with annotated bars.
    
    Args:
        data (list): Data to plot
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        output_path (str): Path to save the plot
        bins (int): Number of bins for the histogram
    """
    plt.figure(figsize=(12, 8))
    
    # Create the histogram
    counts, bins, patches = plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    
    # Add numbers on top of each bar
    for count, patch in zip(counts, patches):
        if count > 0:  # Only annotate non-empty bars
            plt.text(
                patch.get_x() + patch.get_width()/2,
                count + (max(counts) * 0.02),  # Slightly above the bar
                f'{int(count)}',
                ha='center',
                va='bottom',
                fontsize=10
            )
    
    # Add title and labels
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()  # Close the figure to free memory
    
    print(f"Saved histogram to {output_path}")

def analyze_dependency_graph(graph_path, corpus_path):
    """
    Analyze the section dependency graph and calculate token counts.
    
    Args:
        graph_path (str): Path to the dependency graph JSON file
        corpus_path (str): Path to the corpus JSON file
    """
    # Load the graph and corpus
    print(f"Loading section dependencies from {graph_path}")
    with open(graph_path, 'r') as f:
        section_dependencies = json.load(f)
    
    with open(corpus_path, 'r') as f:
        corpus_data = json.load(f)

    # Analyze dependencies
    print("Analyzing section dependencies...")
    results = analyze_dependencies(section_dependencies, corpus_data)
    
    # Sort results by token count
    results.sort(key=lambda x: x["token_count"], reverse=True)
    
    # Print summary
    print(f"\nAnalyzed {len(results)} source sections")
    
    # Base output directory
    output_dir = os.path.dirname(graph_path)
    base_filename = os.path.basename(graph_path).rsplit('.', 1)[0]
    
    # Calculate statistics
    if results:
        token_counts = [r["token_count"] for r in results]
        avg_tokens = sum(token_counts) / len(token_counts)
        median_tokens = sorted(token_counts)[len(token_counts) // 2]
        max_tokens = max(token_counts)
        min_tokens = min(token_counts)
        
        print(f"Token count statistics:")
        print(f"  Average: {avg_tokens:.2f}")
        print(f"  Median: {median_tokens}")
        print(f"  Max: {max_tokens}")
        print(f"  Min: {min_tokens}")
        
        # Create histogram for all sections
        plot_histogram(
            token_counts,
            "Distribution of Token Counts Across All Sections",
            "Token Count",
            "Number of Sections",
            os.path.join(output_dir, f"{base_filename}_all_sections_histogram.png"),
            bins=min(20, len(set(token_counts)))  # Adjust bins based on data variety
        )
        
        # Print top 10 sections by token count
        print("\nTop 10 sections by dependency token count:")
        for i, result in enumerate(results[:10], 1):
            print(f"{i}. RFC {result['source_rfc']}, Section {result['source_section']}: {result['token_count']} tokens")
            
        # Aggregate and analyze by section level
        print("\nAnalyzing token counts by section hierarchy...")
        level_aggregates = aggregate_by_section_level(results)
        
        # Report level-1 sections
        if level_aggregates[1]:
            l1_tokens = [r["token_count"] for r in level_aggregates[1]]
            print("\nTop 10 level-1 sections (including children):")
            for i, result in enumerate(level_aggregates[1][:10], 1):
                print(f"{i}. RFC {result['rfc']}, Section {result['section_id']}: {result['token_count']} tokens")
            
            # Create histogram for level-1 sections
            plot_histogram(
                l1_tokens,
                "Distribution of Token Counts for Level-1 Sections (Including Children)",
                "Token Count",
                "Number of Sections",
                os.path.join(output_dir, f"{base_filename}_level1_histogram.png"),
                bins=min(20, len(set(l1_tokens)))
            )

        # Report level-2 sections
        if level_aggregates[2]:
            l2_tokens = [r["token_count"] for r in level_aggregates[2]]
            print("\nTop 10 level-2 sections (including children):")
            for i, result in enumerate(level_aggregates[2][:10], 1):
                print(f"{i}. RFC {result['rfc']}, Section {result['section_id']}: {result['token_count']} tokens")
            
            # Create histogram for level-2 sections
            plot_histogram(
                l2_tokens,
                "Distribution of Token Counts for Level-2 Sections (Including Children)",
                "Token Count",
                "Number of Sections",
                os.path.join(output_dir, f"{base_filename}_level2_histogram.png"),
                bins=min(20, len(set(l2_tokens)))
            )
                
        # Report level-3 sections
        if level_aggregates[3]:
            l3_tokens = [r["token_count"] for r in level_aggregates[3]]
            print("\nTop 10 level-3 sections (including children):")
            for i, result in enumerate(level_aggregates[3][:10], 1):
                print(f"{i}. RFC {result['rfc']}, Section {result['section_id']}: {result['token_count']} tokens")
            
            # Create histogram for level-3 sections
            plot_histogram(
                l3_tokens,
                "Distribution of Token Counts for Level-3 Sections (Including Children)",
                "Token Count",
                "Number of Sections",
                os.path.join(output_dir, f"{base_filename}_level3_histogram.png"),
                bins=min(20, len(set(l3_tokens)))
            )


def main():
    parser = argparse.ArgumentParser(description='Analyze section dependency graph for connected components')
    parser.add_argument('graph_path', type=str, help='Path to the dependency graph JSON file')
    parser.add_argument('corpus_path', type=str, help='Path to the corpus JSON file')
    
    args = parser.parse_args()
    
    analyze_dependency_graph(args.graph_path, args.corpus_path)


if __name__ == "__main__":
    main()
