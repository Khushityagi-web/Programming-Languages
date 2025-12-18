# Counting Gene Occurrences in R (Beginner Exercise)

This script demonstrates how to count repeated gene names in a vector using R’s built-in `table()` function. It is part of a set of foundational programming tasks where I practiced applying basic R operations to simple biological examples.

---

## Purpose

This exercise helps build early R skills, including:

- Working with vectors  
- Using `table()` to summarize categorical data  
- Converting tabular output into lists  
- Printing structured results  

Although gene names are used, the goal is to understand how R handles frequency counting, which is essential for many downstream bioinformatics workflows.

---

## What the Script Does

- Defines a function `count_gene_occurrences()`  
- Takes a vector of gene names  
- Counts how many times each gene appears  
- Returns the results as a list  
- Tests the function using an example vector  
- Prints the output in a readable format  

### Example Output

    $GeneA
    [1] 2

    $GeneB
    [1] 3

    $GeneC
    [1] 1

---

## File Structure

    count_gene_occurrences/
    │── script.R     # R function to count occurrences of gene names
    │── README.md

---

## Skills Practiced

- Frequency counting using `table()`  
- Converting data structures (table → list)  
- Writing simple functions in R  
- Basic vector manipulation  
- Applying biological labels to foundational logic  

---

## Requirements

- R 3.6+  

No external packages are required.

---

## Author

**Khushi Tyagi**  
Strengthening foundational R skills for bioinformatics
