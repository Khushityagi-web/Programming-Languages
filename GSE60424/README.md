# 🧬 Hybrid Python–R Workflow for Exploring the GSE60424 CD8+ T-Cell Transcriptome

This repository presents a modular hybrid scripting workflow for transcriptomic analysis of the **GSE60424** dataset:  
**"Transcriptome analysis of CD8+ T cell subsets in humans"**.

---

## 📌 Dataset Overview

**GSE60424** is a public RNA-seq dataset available from [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60424).  
It includes normalized expression counts for **134 human CD8+ T cell samples** across four key subsets:

- Naïve CD8+ T cells  
- Effector CD8+ T cells  
- Memory CD8+ T cells  
- TEMRA (terminally differentiated effector memory cells)

We used the processed count file:  
📁 `GSE60424_GEOSubmit_FC1to11_normalized_counts.txt.gz`

---

## 🔁 Workflow Overview

A **hybrid scripting strategy** was used to combine Python’s ease of file handling with R’s powerful statistical packages.

### 🐍 Python (Preprocessing)
- Extract `.gz` file using `gzip` and `shutil`
- Load normalized counts using `pandas`
- Export as `.csv` for use in R

### 📊 R (Analysis & Visualization)
- Load the matrix with `read.csv()`
- Create a sample metadata table
- Apply `vst()` from **DESeq2** for variance-stabilizing transformation
- Generate:
  - ✅ Boxplot of VST-normalized counts (5000 sampled genes)
  - ✅ PCA plot by T cell subset
  - ✅ Heatmap of top 100 variable genes

📎 See `workflow.png` for the visual pipeline.

---

## 🗂 Folder Structure

GSE60424/
├── GSE60424_Preprocessing.py # Python script for file handling
├── GSE60424_Analysis.R # R script for statistical analysis and plots
├── GSE60424_normalized_counts.csv # Preprocessed matrix (from Python)
├── Visualizations.pdf # Contains boxplot, PCA plot, and heatmap
├── workflow.png # Flowchart of full hybrid workflow
└── README.md # This file

## 🔧 Requirements

### Python
- pandas
- gzip
- shutil

### R
- DESeq2
- pheatmap
- ggplot2
- reshape2
- matrixStats

## 📚 References

- [GSE60424 - NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60424)  
- Love et al., 2014 – *Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2*  
- [pheatmap – CRAN](https://cran.r-project.org/web/packages/pheatmap/index.html)  
- [pandas – Python Docs](https://pandas.pydata.org)  
- [GEOparse – Python GEO Utilities](https://geoparse.readthedocs.io)

---

## 🤝 Author

**Khushi Tyagi**  
📍 Bioinformatics and Genomics Enthusiast  
🔗 [GitHub](https://github.com/Khushityagi-web/Programming-Languages/tree/main/GSE60424)

---

> This pipeline was built to support reproducible, scalable analysis of immune transcriptomes using a clear, modular structure.  
> Contributions and suggestions are welcome!
