# Added script for biological and non-biological data types in Python.

# Biological Data (genes, proteins, etc.)
protein_name = "Hemoglobin"  # String
gene_id = 101  # Integer
protein_weight = 64.5  # Float (molecular weight in kDa)
is_protein_active = False  # Boolean
amino_acids = ['Glycine', 'Valine', 'Leucine', 'Threonine']  # List

# Non-Biological Data (environmental factors)
air_quality_index = 55  # Integer
avg_rainfall = 240.8  # Float (in mm)
city_name = "Delhi"  # String
is_rainfall_above_average = True  # Boolean
temperature_record = {'Jan': 15.2, 'Feb': 18.5, 'Mar': 25.6}  # Dictionary

# Print Biological Data
print("Biological Data:")
print(f"Protein Name: {protein_name}")
print(f"Gene ID: {gene_id}")
print(f"Protein Weight (kDa): {protein_weight}")
print(f"Protein Active: {is_protein_active}")
print(f"Amino Acids: {amino_acids}")

# Print Non-Biological Data
print("\nNon-Biological Data:")
print(f"Air Quality Index: {air_quality_index}")
print(f"Average Rainfall (mm): {avg_rainfall}")
print(f"City Name: {city_name}")
print(f"Rainfall Above Average: {is_rainfall_above_average}")
print(f"Temperature Record (°C): {temperature_record}")
