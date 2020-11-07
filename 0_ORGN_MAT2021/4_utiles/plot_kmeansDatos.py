import sys
import os
import json
import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

archivoDeEntrada =  "/Users/ottocastro/Desktop/PruebaCodigo/datosDescriptoresTodos.csv"
print(archivoDeEntrada)
	
todoDatos = []

file = open(archivoDeEntrada, 'r')
Lines = file.readlines() 

# Strips the newline character 
for line in Lines: 
	lineaFormateada = np.array(line.strip().split(",")).astype(np.float)
	todoDatos.append(lineaFormateada)
todoDatos = np.array(todoDatos)
print(todoDatos)

n_clusters = 8
# Runs in parallel 4 CPUs
kmeans = KMeans(n_clusters=n_clusters, n_init=20, n_jobs=4)
# Train K-Means.
y = kmeans.fit_predict(todoDatos)
# Evaluate the K-Means clustering accuracy.
print(y)


lista = np.array([ n[1]  for n in todoDatos  ])
lista_reshape = lista.reshape(-1,1)
X = np.array(lista_reshape)
col = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
kmeans = KMeans(n_clusters=8, random_state=0).fit(X)    
    
print(kmeans.labels_)

for i,l in enumerate(kmeans.labels_):
    plt.plot(lista[i],color=col[l],marker='o',ls='None')

plt.show()



