# GSE60424 RNA-seq Pipeline: Python Part
import gzip
import shutil
import pandas as pd
# Step 1: Extract .gz expression matrix from GEO
# Source: GSE60424_GEOSubmit_FC1to11_normalized_counts.txt.gz
with gzip.open("GSE60424_data/GSE60424_GEOSubmit_FC1to11_normalized_counts.txt.gz", 'rb') as f_in:
    with open("GSE60424_data/GSE60424_normalized_counts.txt", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print("File extracted successfully.")

# Step 2: Load the expression matrix as a pandas DataFrame
df = pd.read_csv("GSE60424_data/GSE60424_normalized_counts.txt", sep="\t", index_col=0)
print("Matrix shape:", df.shape)
print(df.head())

# Step 3: Save as CSV to import into R easily
df.to_csv("GSE60424_data/GSE60424_normalized_counts.csv")
