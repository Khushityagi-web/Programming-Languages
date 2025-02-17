# Added script for GC content calculation and reverse complement in DNA sequences.

def gc_content(dna_sequence):
    """Calculate GC content percentage in a given DNA sequence."""
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    gc_percentage = (g_count + c_count) / len(dna_sequence) * 100
    return gc_percentage

def reverse_complement(dna_sequence):
    """Find the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reversed_sequence = dna_sequence[::-1]
    return ''.join(complement[base] for base in reversed_sequence)

# Input DNA sequence from the user
dna_sequence = input("Enter a DNA sequence: ").upper()

# Calculate GC content and reverse complement
gc_percentage = gc_content(dna_sequence)
reverse_comp = reverse_complement(dna_sequence)

# Print results
print(f"GC Content: {gc_percentage:.2f}%")
print(f"Reverse Complement: {reverse_comp}")

# Sample Output
Enter a DNA sequence: AATCGGGACTTCAT
GC Content: 42.86%
Reverse Complement: ATGAAGTCCCGATT
