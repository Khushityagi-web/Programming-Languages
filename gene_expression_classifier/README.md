# Gene Expression Classification in Python (Beginner Exercise)

This script defines a simple Python function that categorizes gene expression values into four levels: **High**, **Moderate**, **Low**, and **Undetected**. It forms part of my early programming practice, where biological examples are used to learn conditional logic and function design.

---

## Purpose

The aim of this exercise is to build foundational skills in:

- Writing Python functions  
- Using conditional statements (`if`, `elif`, `else`)  
- Iterating through lists  
- Formatting printed output  
- Translating biological thresholds into simple computational rules  

---

## What the Script Does

### Gene Expression Classification Function

The function `check_gene_expression()` uses numeric thresholds to assign categories.

#### Thresholds Used

| Expression Level | Category     |
|------------------|--------------|
| ≥ 1000           | High         |
| ≥ 500            | Moderate     |
| ≥ 100            | Low          |
| < 100            | Undetected  |

### Test Cases

A list of example expression values is looped through, and each value is classified.

**Example output:**

    Expression value: 1200 - Category: High
    Expression value: 800 - Category: Moderate
    Expression value: 450 - Category: Low
    Expression value: 80 - Category: Undetected

---

## File Structure

    gene_expression_classifier/
    │── script.py     # Python function for expression classification
    │── README.md

---

## Skills Practiced

- Python function creation  
- Conditional logic  
- Applying threshold-based rules  
- Looping through lists  
- Clean output formatting using f-strings  

---

## Requirements

- Python 3.x  

No external libraries are required.

---

## Author

**Khushi Tyagi**  
Building foundational Python skills for computational biology

