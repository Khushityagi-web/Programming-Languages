Added gene expression classification function with test cases.
  
def check_gene_expression(expression):
    """
    Classifies gene expression levels into categories.

    Args:
        expression (int or float): A numeric gene expression value.

    Returns:
        str: A string indicating the expression category.
    """
    if expression >= 1000:
        return "High"
    elif expression >= 500:
        return "Moderate"
    elif expression >= 100:
        return "Low"
    else:
        return "Undetected"

# List of gene expression values to test
expression_values = [1200, 800, 450, 80]

# Iterate over the list and print the classification for each value
for value in expression_values:
    expression_category = check_gene_expression(value)
    print(f"Expression value: {value} - Category: {expression_category}")

# Sample Output
Expression value: 1200 - Category: High
Expression value: 800 - Category: Moderate
Expression value: 450 - Category: Low
Expression value: 80 - Category: Undetected
