# PCA (Principal Component Analysis), ou Análise de Componentes Principais em português, 
# é um algoritmo de redução de dimensionalidade que transforma um conjunto de dados em um novo conjunto de dimensões menores, 
# chamados de componentes principais. O objetivo do PCA é reduzir a complexidade do conjunto de dados, 
# mantendo a maior parte da variação dos dados.
# Um componente principal é uma combinação linear das variáveis originais.

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

from sklearn.datasets import load_iris
data = load_iris()
x = data.data

# Criando o objeto PCA e ajustando para reduzir a dimensionalidade para 2 componentes
pca = PCA(n_components=2)
pca.fit(x)

# Imprimindo a proporção da variância explicada por cada componente principal
print("Proporção da Variância Explicada por cada Componente Principal:")
print(pca.explained_variance_ratio_)

# Imprimindo os valores singulares correspondentes aos componentes principais
print("Valores Singulares:")
print(pca.singular_values_)