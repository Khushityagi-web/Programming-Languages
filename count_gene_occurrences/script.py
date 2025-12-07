# Added function to count gene occurrences in a list
# Function: Count Gene Occurrences
def count_gene_occurrences(gene_list):
    """
    Counts the occurrences of each gene in a list.

    Args:
        gene_list: A list of gene names.

    Returns:
        A dictionary where the keys are gene names and the values are their counts.
    """
    gene_counts = {}
    
    # Iterate through the gene list and count occurrences
    for gene in gene_list:
        if gene in gene_counts:
            gene_counts[gene] += 1
        else:
            gene_counts[gene] = 1
    
    return gene_counts

# Test the function with a sample list of gene names
gene_list = ['GeneA', 'GeneB', 'GeneA', 'GeneC', 'GeneB', 'GeneB']
gene_counts = count_gene_occurrences(gene_list)

# Print the result
print(gene_counts)
{'GeneA': 2, 'GeneB': 3, 'GeneC': 1}
