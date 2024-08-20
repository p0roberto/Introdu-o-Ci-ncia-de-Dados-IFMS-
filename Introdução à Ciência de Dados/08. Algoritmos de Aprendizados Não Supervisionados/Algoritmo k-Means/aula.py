# O algoritmo k-means é um algoritmo de agrupamento (clustering) não supervisionado amplamente utilizado em machine learning. 
# Ele agrupa os dados em k clusters, onde k é um número pré-definido pelo usuário. 
# O algoritmo k-means é um algoritmo iterativo que começa com k centroides aleatórios, 
# atribui cada ponto de dados ao cluster cujo centróide está mais próximo e, em seguida, recalcula o centróide de cada cluster. 
# Esse processo é repetido até que a diferença entre os centróides atuais e os anteriores seja inferior a um valor definido.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn import metrics

# Carregar o conjunto de dados Iris
x, y = load_iris(return_X_y=True, as_frame=True)

# Selecionar apenas as colunas relevantes para clustering
x = x[['petal length (cm)', 'petal width (cm)']]

# Aplicar o algoritmo K-Means
kmeans = KMeans(n_clusters=2, random_state=0).fit(x)
kmeans2 = KMeans(n_clusters=3, random_state=0).fit(x)
labels = kmeans.labels_
labels2 = kmeans2.labels_

# Percorrendo diferentes valores de K
valores_k = list(range(1, 15))
inercias = []
ARI = []
silhueta = []

for i in valores_k:
    kmeans = KMeans(n_clusters=i, random_state=0).fit(x)
    inercias.append(kmeans.inertia_)
    ARI.append(metrics.adjusted_rand_score(y, kmeans.labels_))
    if i > 1:
        silhueta.append(metrics.silhouette_score(x, kmeans.labels_))

# Criando a figura com subplots
fig, axs = plt.subplots(3, 2, figsize=(14, 10))

# Comparação de Clusters k=2
axs[0, 1].scatter(x['petal length (cm)'], x['petal width (cm)'], c=labels, cmap='viridis', label='k=2')
axs[0, 1].set_title('Clusters k=2')
axs[0, 1].set_xlabel('Comprimento da Pétala (cm)')
axs[0, 1].set_ylabel('Largura da Pétala (cm)')
axs[0, 1].legend()

# Comparação de Clusters k=3
axs[0,0].scatter(x['petal length (cm)'], x['petal width (cm)'], c=labels2, cmap='viridis', label='k=3')
axs[0,0].set_title('Clusters k=3')
axs[0,0].set_xlabel('Comprimento da Pétala (cm)')
axs[0,0].set_ylabel('Largura da Pétala (cm)')
axs[0,0].legend()

# Gráfico de ARI
axs[1, 1].plot(valores_k, ARI, marker='o', linestyle='-', label='ARI')
axs[1, 1].set_xlabel('Número de Clusters (k)')
axs[1, 1].set_ylabel('Adjusted Rand Index (ARI)')
axs[1, 1].set_title('ARI vs Número de Clusters')
axs[1, 1].legend()

# Gráfico de Coeficiente Silhueta
axs[2, 0].plot(range(2, 15), silhueta, marker='o', linestyle='-', label='Coeficiente Silhueta')
axs[2, 0].set_xlabel('Número de Clusters (k)')
axs[2, 0].set_ylabel('Coeficiente Silhueta')
axs[2, 0].set_title('Coeficiente Silhueta vs Número de Clusters')
axs[2, 0].legend()

# Gráfico de Elbow
axs[2, 1].plot(valores_k, inercias, marker='o', linestyle='-', color='r', label='Inércia')
axs[2, 1].set_xlabel('Número de Clusters (k)')
axs[2, 1].set_ylabel('Inércia')
axs[2, 1].set_title('Método do Cotovelo')
axs[2, 1].legend()

plt.tight_layout()
plt.show()
