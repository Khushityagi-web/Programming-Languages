# GC Content & Reverse Complement in Python (Beginner Exercise)

This script computes the GC content of a DNA sequence and generates its reverse complement. It is part of my foundational Python exercises, where I practiced applying basic string operations and dictionaries to biologically meaningful tasks.

These are essential concepts in genomics and form the building blocks for more advanced FASTA parsing and sequence analysis later.

---

## Purpose

The goal of this exercise is to practice:

- Writing modular Python functions  
- Counting nucleotides and computing percentages  
- Reversing strings using slicing  
- Using dictionaries to map nucleotide complements  
- Handling user input and printing clean results  

---

## What the Script Does

### GC Content Calculation
- Counts the number of `G` and `C` bases  
- Computes and returns GC percentage  

### Reverse Complement
- Reverses the DNA sequence  
- Maps each base to its complement using a dictionary  
- Joins the result into a final reverse-complement string  

### Example

    Input:
    AATCGGGACTTCAT

    Output:
    GC Content: 42.86%
    Reverse Complement: ATGAAGTCCCGATT

---

## File Structure

    gc_content_reverse_complement/
    │── script.py     # GC content and reverse complement functions
    │── README.md

---

## Skills Practiced

- Python function design  
- String reversal and indexing  
- Dictionary-based base pairing  
- Simple biological sequence manipulation  
- Console interaction with user-defined input  

---

## Requirements

- Python 3.x  

No external libraries are required.

---

## Author

**Khushi Tyagi**  
Building early Python foundations for computational biology
