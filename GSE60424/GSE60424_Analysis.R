# GSE60424 RNA-seq Pipeline: R Part
# Dataset: GSE60424 (Human CD8+ T-cell subsets)

# Load required libraries
library(DESeq2)
library(pheatmap)
library(ggplot2)
library(reshape2)
library(matrixStats)

# Step 1: Load expression matrix (exported from Python)
counts <- read.csv("GSE60424_normalized_counts.csv", row.names = 1, check.names = FALSE)

# Step 2: Create metadata (temporary grouping)
sample_info <- data.frame(
  row.names = colnames(counts),
  condition = rep(c("Naive", "Effector", "Memory", "Temra"), length.out = ncol(counts)) # Replace with actual sample groups if known
)

# Step 3: Create DESeq2 dataset and transform
dds <- DESeqDataSetFromMatrix(countData = round(counts),
                              colData = sample_info,
                              design = ~ condition)
vsd <- vst(dds, blind = TRUE)
vsd_mat <- assay(vsd)

# Step 4: Boxplot (with sampled genes)
set.seed(123)
vsd_sampled <- vsd_mat[sample(nrow(vsd_mat), 5000), ]
vsd_df <- as.data.frame(vsd_sampled)
vsd_df$Gene <- rownames(vsd_df)
vsd_melt <- melt(vsd_df, id.vars = "Gene", variable.name = "Sample", value.name = "VST")

ggplot(vsd_melt, aes(x = Sample, y = VST)) +
  geom_boxplot(outlier.size = 0.3, fill = "lightblue") +
  theme(axis.text.x = element_text(angle = 90, size = 5)) +
  labs(title = "Boxplot of VST-normalized Expression (Sampled Genes)",
       x = "Sample", y = "VST Counts")

# Step 5: PCA Plot
plotPCA(vsd, intgroup = "condition")

# Step 6: Heatmap of Top 100 Most Variable Genes
topVarGenes <- head(order(rowVars(vsd_mat), decreasing = TRUE), 100)
pheatmap(vsd_mat[topVarGenes, ],
         show_rownames = FALSE,
         annotation_col = as.data.frame(colData(vsd)),
         main = "Top 100 Variable Genes Heatmap")
