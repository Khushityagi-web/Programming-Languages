# Added function to count gene occurrences in a vector
count_gene_occurrences <- function(gene_list) {
  # Count occurrences of each gene in the list
  gene_counts <- table(gene_list)
  
  # Convert the table output to a list
  return(as.list(gene_counts))
}

# Test the function with a sample vector of gene names
gene_list <- c("GeneA", "GeneB", "GeneA", "GeneC", "GeneB", "GeneB")
gene_counts <- count_gene_occurrences(gene_list)

# Print the result
print(gene_counts)

# Output:
$GeneA
[1] 2

$GeneB
[1] 3

$GeneC
[1] 1
