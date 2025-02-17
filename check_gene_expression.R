# Added gene expression classification function in R
# Function to classify gene expression levels
check_gene_expression <- function(expression) {
  if (expression >= 1000) {
    return("High")
  } else if (expression >= 500) {
    return("Moderate")
  } else if (expression >= 100) {
    return("Low")
  } else {
    return("Undetected")
  }
}

# Vector of gene expression values
gene_expression_values <- c(1200, 800, 450, 80)

# Apply the function to each value and print the results
for (value in gene_expression_values) {
  category <- check_gene_expression(value)
  cat("Expression value:", value, "- Category:", category, "\n")
}
