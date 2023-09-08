library(ggplot2)

## ---------------- NOTE: REAL SCRIPT IS IN THE END - BELOW IS THE RAW SCRIPT (line 68)

# leer archivo
data <- read.delim(file = "a_CvsL.tab",header = TRUE,
                   sep = "\t", stringsAsFactors = FALSE)

# Multiply if you want change de FC (for example Ctrl_vs_Cond1 -> Cond1_vs_Ctrl)
## NOTE: R take decimal values separates by dot (3.70) and not comma (3,70)
data$log2FoldChange <- data$log2FoldChange * (-1)



## aplicar el log solo a la columna 3 y agregar el resultado a "data"
#data[, 3:3] <- (-log10(data[3:3]))

## filtrar lineas por valor de pvalue (que se cambio antes a -log10)
#data <- data[data$pvalue != 0 & data$pvalue < 4, ]

# crea nueva columna en data. Cada linea tendra la palabra "Stable"
  # Mayor a 1.5 en columna "log2FoldChange" se cambiará "Stable" por "Up-regulated"
  # Menor a -1.5 en columna "log2FoldChange" se cambiará "Stable" por "Down-regulated"
data["group1"] <- "Stable"

data[which(data['log2FoldChange'] >= 2.0 & data['pvalue'] <= 0.05) ,"group1"] <- "Up-regulated"
data$threshold = as.factor(data$log2FoldChange >= 2.0 & data$pvalue <= 0.05)

data[which(data['log2FoldChange'] <= -2.0 & data['pvalue'] <= 0.05) ,"group1"] <- "Down-regulated"
data$threshold = as.factor(data$log2FoldChange <= -2.0 & data$pvalue <= 0.05)

# aplicar el log solo a la columna 3 y agregar el resultado a "data"
data[, 3:3] <- (-log10(data[3:3]))

# filtrar lineas por valor de pvalue (que se cambio antes a -log10)
data <- data[data$pvalue != 0 & data$pvalue < 4, ]


#data["group1"] <- "Stable"
#data[which(data['log2FoldChange'] > 1.5) ,"group1"] <- "Up-regulated"
#data$threshold = as.factor(data$log2FoldChange > 1.5)
#data[which(data['log2FoldChange'] < -1.5) ,"group1"] <- "Down-regulated"
#data$threshold = as.factor(data$log2FoldChange < -1.5)

#Crear el plot
g <- ggplot(data=data, 
            aes(x=log2FoldChange, y =pvalue, #y =-log10(pvalue), El log es aplicado al principio
                colour=group1, fill = group1)) +
  geom_point(alpha=0.4, size=1.75) +
  
  scale_colour_manual(values = c("Up-regulated"= "red", "Stable"="gray",  "Down-regulated"= 
                                   "blue")) +
  ylim(c(0,5)) +
  xlim(c(-10, 10)) +
  xlab("log2 fold change") + ylab("-log10 p-value") +
  theme_bw() + theme(legend.title = element_blank())
g + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
          panel.background = element_blank(),
           #panel.background = element_rect(fill = "white"),
           axis.text=element_text(size=6),
           axis.title=element_text(size=8,face="bold"))

ggsave("2_.pdf", width = 10, height = 4.5, dpi = 300)




#-----------------------------------------------------------------------
#----------------------------- REAL SCRIPT HERE ------------------------




data <- read.delim(file = "c_LvsG.tab",
                   header = TRUE,
                   sep = "\t",
                   stringsAsFactors = FALSE)

data$log2FoldChange <- data$log2FoldChange * (-1)

data["group1"] <- "Stable"

data[which(data['log2FoldChange'] >= 2.0 & data['pvalue'] <= 0.05) ,"group1"] <- "Up-regulated"
data$threshold = as.factor(data$log2FoldChange >= 2.0 & data$pvalue <= 0.05)

data[which(data['log2FoldChange'] <= -2.0 & data['pvalue'] <= 0.05) ,"group1"] <- "Down-regulated"
data$threshold = as.factor(data$log2FoldChange <= -2.0 & data$pvalue <= 0.05)

data[, 3:3] <- (-log10(data[3:3]))
data$pvalue[which(data$pvalue==Inf)] <- 2.2


data <- data[data$pvalue != 0, ]

g <- ggplot(data=data, 
            aes(x=log2FoldChange,
                y =pvalue,
                colour=group1,
                fill = group1)) +
  geom_point(alpha=0.4, size=1.75) +
  
  scale_colour_manual(values = c("Up-regulated"= "red",
                                 "Stable"="gray",
                                 "Down-regulated"= "blue")) +
  ylim(c(0,3)) +
  xlim(c(-5, 5)) +
  xlab("log2 fold change") + ylab("-log10 p-value") +
  theme_bw() + theme(legend.title = element_blank())
g + theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.background = element_blank(),
          #panel.background = element_rect(fill = "white"),
          axis.text=element_text(size=6),
          axis.title=element_text(size=8,face="bold"))

ggsave("test_.pdf", width = 10, height = 4.5, dpi = 300)
ggsave("test_.png", width = 10, height = 4.5, dpi = 300)









