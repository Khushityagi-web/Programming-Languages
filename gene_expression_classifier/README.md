# Gene Expression Classification in Python (Beginner Exercise)

This script defines a simple Python function that categorizes gene expression values into four levels: High, Moderate, Low, and Undetected.
It forms part of my early programming practice, where I used biological examples to learn conditional logic and function design.

## 🎯 Purpose

The aim of this exercise is to build foundational skills in:

🔹 writing Python functions

🔹 using conditional statements (if, elif, else)

🔹 iterating through lists

🔹 formatting printed output

🔹 translating biological thresholds into simple computational rules

## What the Script Does
1. Gene Expression Classification Function

The function check_gene_expression() uses numeric thresholds to assign categories:

Expression Level	Category
≥ 1000	High
≥ 500	Moderate
≥ 100	Low
< 100	Undetected
2. Test Cases

A list of example expression values is looped through, and each value is classified.

Example Output:
Expression value: 1200 - Category: High
Expression value: 800 - Category: Moderate
Expression value: 450 - Category: Low
Expression value: 80 - Category: Undetected

## 📂 File Structure
gene_expression_classifier/
│── script.py      # Python function for expression classification
└── README.md

## Skills Practiced

🔹 Python function creation

🔹 Conditional logic

🔹 Applying threshold-based rules

🔹 Looping through lists

🔹 Clean output formatting with f-strings

## Requirements

Python 3.x
(No external libraries required)

## 🤝 Author

Khushi Tyagi — building foundational Python skills for computational biology.
