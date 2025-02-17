# Added gene expression analysis scripts using for and while loops in R

# For Loop: Compute Average Gene Expression
# Vector of gene expression values
gene_expression_values <- c(1500, 2000, 2500, 3000, 3500)

# Initialize a variable to store the sum of values
total_expression <- 0

# Loop through the vector to calculate the sum
for (value in gene_expression_values) {
  total_expression <- total_expression + value
}

# Calculate the average
average_expression <- total_expression / length(gene_expression_values)

# Print the result
cat("The average gene expression value is:", average_expression, "\n")
The average gene expression value is: 2500  (Output)

# While Loop: Count Genes Above Threshold
# Vector of gene expression values
gene_expression_values <- c(1, 1, 2, 3, 5, 8, 13, 21)

# Threshold value
threshold <- 10

# Initialize counters
count <- 0
index <- 1

# While loop to iterate through the vector
while (index <= length(gene_expression_values)) {
  if (gene_expression_values[index] > threshold) {
    count <- count + 1
  }
  index <- index + 1
}

# Print the result
cat("The number of genes with expression values above", threshold, "is:", count, "\n")
The number of genes with expression values above 10 is: 2  (Output)
