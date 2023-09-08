library(M3Drop)
library(M3DExampleData)


table <- read.table("/home/thais/Área de Trabalho/Doc/Files_to_Clustering/Gene_id/276R.txt",sep = "\t", header = T)

row.names(table)<-table$tracking_id

table<-table[,2:length(table)]

counts <- table

labels <- colnames(counts)
total_features <- colSums(counts >= 0)
counts <- counts[,total_features >= 2000]
labels <- labels[total_features >= 2000]
norm <-  M3DropCleanData(counts, labels = labels, is.counts = TRUE, suppress.plot = FALSE, pseudo_genes = NA, min_detected_genes = NA)
M3Drop_genes <- M3DropFeatureSelection(norm$data, mt_method="fdr", mt_threshold=0.05, suppress.plot=FALSE)
head_out <- M3DropExpressionHeatmap(M3Drop_genes$Gene, norm$data, cell_labels = labels)
cell_populations <- M3DropGetHeatmapClusters(head_out, k=4)
marker_genes <- M3DropGetMarkers(norm$data, cell_populations)

write.table(format(cell_populations), quote = FALSE, sprintf("/home/thais/Área de Trabalho/%s", "teste2.txt"),sep= "\t")
write.table(format(marker_genes), quote = FALSE, sprintf("/home/thais/Área de Trabalho/%s", "marker_M3.txt"),sep= "\t")
write.table(format(M3Drop_genes), quote = FALSE, sprintf("/home/thais/Área de Trabalho/%s", "Differential_M3.txt"),sep= "\t")