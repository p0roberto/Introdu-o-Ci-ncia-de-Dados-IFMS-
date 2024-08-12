# Pandas forne várias funções para ler lidar com tipos de arquivos, incluindo CSV, Excel, JSON, etc.

import pandas as pd

# Arquivos e DataFrame

col_names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Species']
iris = pd.read_csv('02.Bibliotecas de Apoio/Arquivos/iris/iris.data', names = col_names) # Podemos usar read_json, read_exel, etc
print(iris)

# Vizualizar e inspecionar dados

print(iris.head()) # Exibe as 'n' primeiras informações
print(iris.tail()) # Exeve as 'n' ultimas informações
print(iris.info()) # Informações do dataframe
print(iris.describe()) # Mais informações complementares

# Formato dos dados

print(iris.shape) # Formato da 'matriz' 

# Estatísticas

# mean(): calcula a média dos valores de uma coluna
# median(): cacula a mediana dos valores de uma coluna
# mode(): calcula a moda dos valores de uma coluna
# min(): calcula o valor minimo de uma coluna
# max(): calcula o valor máximo de uma coluna 
# sum(): reotrna a soma do valores de uma coluna
# cout(): retorna a contagem de valores não-nulos de uma coluna
# std(): calcula o desvio padrão dos valores de uma coluna
# var(): calcula a variancia dos valores de uma coluna
# quantile(): calcula o percentil especifico dos valores de uma coluna
# cov(): calcula a covariancia entre colunas de um dataframe
# corr(): calcula a correlação entre colunas de um dataframe

# Seleção de Dados

print(iris['Petal_Length'])
print(iris[['Petal_Length','Sepal_Width']])
print(iris.loc[54]) # Acessa uma linha em específico
print(iris.iloc[0:10, 1:3]) # Acessa a coluna 1 a 3, da linha 0 a 10

# Filtrar, classificar e agrupar

print(iris[iris['Species'] == 'Iris-virginica']) # Traz as informações apenas das linhas que contem a espécie virginica
print(iris.sort_values('Sepal_Length', ascending = True )) # Ordena as linhas pela Sepal Length
