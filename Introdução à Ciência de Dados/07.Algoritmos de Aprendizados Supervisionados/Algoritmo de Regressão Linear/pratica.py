import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# Configurando o Pandas para mostrar todas as colunas
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Criando o DataFrame
dados = fetch_california_housing()
casas = pd.DataFrame(dados.data)
casas.columns = dados.feature_names

# Adicionando a coluna target
casas['MedHouseVal'] = dados.target

print(casas)

X = casas.MedInc
Y = casas.MedHouseVal

# Separando nossa base em treino e teste para criarmos o modelo
X_train, X_teste, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# Usando a regressão linear
reg = LinearRegression().fit(X_train.values.reshape(-1,1), y_train)

# Previsão usando o conjunto de teste
y_pred = reg.predict(X_teste.values.reshape(-1,1))

# Avaliando o erro
print("Erro Absoluto Médio:", mean_absolute_error(y_test, y_pred))
print("Erro Quadrático Médio:", mean_squared_error(y_test, y_pred))
print('\n')

# Visualizando a relação entre y_test e y_pred
fig, ax = plt.subplots()

ax.scatter(y_pred, y_test)
ax.set_xlabel("Valores Preditos (y_pred)")
ax.set_ylabel("Valores Reais (y_test)")
ax.set_title("Relação entre Valores Preditos e Reais (Reg Simples)")

plt.show()

# Regresão Linear Múltipla
X = casas.drop('MedHouseVal', axis =1)
Y = casas.MedHouseVal

X_train, X_teste, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

reg = LinearRegression().fit(X_train, y_train)
y_pred = reg.predict(X_teste)

print("Erro Absoluto Médio:", mean_absolute_error(y_test, y_pred))
print("Erro Quadrático Médio:", mean_squared_error(y_test, y_pred))
print('\n')

fig, ax = plt.subplots()

ax.scatter(y_pred, y_test)
ax.set_xlabel("Valores Preditos (y_pred)")
ax.set_ylabel("Valores Reais (y_test)")
ax.set_title("Relação entre Valores Preditos e Reais (Reg Multipla)")
ax.plot([1, 5], [1, 5], '--r')

plt.show()