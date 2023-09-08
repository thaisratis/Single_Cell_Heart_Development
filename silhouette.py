from __future__ import print_function

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import AgglomerativeClustering

import numpy as np
import os


print(__doc__)

files = os.listdir('/home/thais/Área de Trabalho/Doc/Files_to_Clustering/Silhouette_files/')

for i_file in files:

  # Read the file
  print(i_file)
  X = np.loadtxt('/home/thais/Área de Trabalho/Doc/Files_to_Clustering/Silhouette_files/'+ str(i_file), delimiter='\t', dtype=bytes).astype(float)

  range_n_clusters = range(2,10)

  for n_clusters in range_n_clusters:
     
      #clusterer = KMeans(n_clusters=n_clusters, random_state=0) # Silhouette with KMeans

      # Silhouette with Hierarchical
      clusterer = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
      cluster_labels = clusterer.fit_predict(X)
      #print (cluster_labels)
      #centroids = clusterer.cluster_centers_
      #print(centroids)

      # The silhouette_score gives the average value for all the samples.
      # This gives a perspective into the density and separation of the formed clusters
      silhouette_avg = silhouette_score(X, cluster_labels)
      
      print("File "+ str(i_file) + ": For n_clusters =", n_clusters,
            "The average silhouette_score is :", silhouette_avg)

      # Compute the silhouette scores for each sample
      sample_silhouette_values = silhouette_samples(X, cluster_labels)
      #print (sample_silhouette_values)
