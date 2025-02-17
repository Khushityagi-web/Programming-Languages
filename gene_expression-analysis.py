# Added gene expression analysis scripts using for and while loops

# For Loop: Compute Average Gene Expression
# List of gene expression values
gene_expression_values = [1500, 2000, 2500, 3000, 3500]

# Initialize a variable to store the sum of values
total_expression = 0

# Loop through the list to calculate the sum
for value in gene_expression_values:
    total_expression += value

# Calculate the average
average_expression = total_expression / len(gene_expression_values)

# Print the result
print(f"The average gene expression value is: {average_expression}")
The average gene expression value is: 2500.0  (Output)

# While Loop: Count Genes Above Threshold
# List of gene expression values
gene_expression_values = [1, 1, 2, 3, 5, 8, 13, 21]

# Threshold value
threshold = 10

# Initialize counters
count = 0
index = 0

# While loop to count values above the threshold
while index < len(gene_expression_values):
    if gene_expression_values[index] > threshold:
        count += 1
    index += 1

# Print the result
print(f"The number of genes with expression values above {threshold} is: {count}")
The number of genes with expression values above 10 is: 2   (Output)
