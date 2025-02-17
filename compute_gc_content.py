# Added function to compute GC content of DNA sequence
def compute_gc_content(dna_sequence):
    """
    Computes the GC content of a given DNA sequence.

    Args:
        dna_sequence (str): A string representing a DNA sequence.

    Returns:
        float: The GC content as a percentage.
    """
    # Count occurrences of 'G' and 'C' in the sequence
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')

    # Calculate GC percentage
    gc_percentage = (g_count + c_count) / len(dna_sequence) * 100
    return gc_percentage

# Test the function with a sample DNA sequence
dna_sequence = "ATGCGTACG"
gc_percentage = compute_gc_content(dna_sequence)

# Print the result
print(f"GC Content: {gc_percentage:.2f}%")

# Output:
GC Content: 55.56%
