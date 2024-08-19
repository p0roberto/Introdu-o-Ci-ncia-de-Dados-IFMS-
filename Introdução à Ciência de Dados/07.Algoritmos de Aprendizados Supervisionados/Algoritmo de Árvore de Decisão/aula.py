# Uma arvore de decisão é uma representação de um conjunto de regras criado para tomar qualquer decisão,
# nesse caso, classificar um registro ou estimar um valor.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

# Carregar o conjunto de dados Iris
dados = load_iris()
iris = pd.DataFrame(dados.data, columns=dados.feature_names)
iris['target'] = dados.target

# Definir características e alvo
x = iris.drop('target', axis = 1)
y = iris.target

# Dividir os dados em conjuntos de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.33, random_state=42)

# Plotagem dos dados de treino
fig, ax = plt.subplots()
dispersao = ax.scatter(x_treino['petal length (cm)'], x_treino['petal width (cm)'], c=y_treino, cmap='viridis', edgecolor='k')
plt.colorbar(dispersao, ax=ax, label='Target')
ax.set_xlabel('Comprimento da Pétala (cm)')
ax.set_ylabel('Largura da Pétala (cm)')
ax.set_title('Dados de Treino do Iris: Comprimento vs. Largura da Pétala')
plt.show()

# Criar o classificador de árvore de decisão
clf = tree.DecisionTreeClassifier(random_state=42).fit(x_treino, y_treino)

# Treinar o classificador com os dados de treino
clf = clf.fit(x_treino, y_treino)

# Verificar a acurácia no conjunto de treino
score = clf.score(x_treino, y_treino)
print(f"Acurácia no conjunto de treino: {score:.2f}")

# Visualizar a árvore de decisão
fig, ax = plt.subplots(figsize=(12, 8))  # Tamanho da figura ajustado para melhor visualização
tree.plot_tree(clf)
plt.show()

# Fazendo a previsão e avaliando o erro
y_pred = clf.predict(x_teste)
from sklearn.metrics import confusion_matrix
print('\nAvaliação do modelo: ')
print(confusion_matrix(y_teste, y_pred))
