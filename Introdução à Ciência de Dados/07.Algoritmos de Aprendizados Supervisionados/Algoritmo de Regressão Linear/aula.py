# A regressão linear é um algoritmo de machine learning supervisionado utilizado para modelar a relação entre uma variável independente (ou variáveis) e uma variável dependente contínua. 
# É uma técnica simples, mas poderosa, que permite prever valores de uma variável dependente com base em valores de uma ou mais variáveis independentes.

# Variável independente ou preditora: é aquela que será passada para o modelo, tendo influência na variável que queremos encontrar. 
# Por exemplo: Se queremos prever as vendas de sorvete, a estação do ano pode interferir nas vendas.
# Variável alvo ou dependente: é a variável que queremos prever. No exemplo acima seria as vendas de sorvete.

# Esse tipo de algoritmo é aplicado quando há uma boa correlação linear (positiva ou negativa) entre os dados, 
# ou seja, quando o relacionamento ou associação entre os dados pode ser definido com uma reta.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [1.3, 1.8, 3.5, 4, 4.6]
})

dados['y_reta'] = dados.X

# Importando a regressão linear
from sklearn.linear_model import LinearRegression

# Criando o regressor
reg = LinearRegression().fit(dados.X.values.reshape(-1,1), dados.Y)

# Coeficiente angular
print('Coeficiente Angular:')
print(reg.coef_)
print('\n')

# Coeficiente linear
print('Coeficiente Linear:')
print(reg.intercept_)
print('\n')

# Plotar gráfico com regressor
fig,ax = plt.subplots()

ax.scatter(dados.X, dados.Y)
ax.plot(dados.X, dados.y_reta, '--r')

x = dados.X.values
y = (reg.coef_)*x + reg.intercept_ # Equação da reta
ax.plot(x, y)

plt.show()

# Fazendo a previsão e adinando na base
dados['y_pred'] = reg.predict(dados.X.values.reshape(-1,1))
print(dados)
print('\n')

# Calculando o erro da reta vermelha e da regressão
print((dados.Y - dados.y_reta)**2)
print('\n')

print((dados.Y - dados.y_pred)**2)
print('\n')

dados['erro_reta'] = ((dados.Y - dados.y_reta)**2)
dados['erro_pred'] = ((dados.Y - dados.y_pred)**2)

print(dados)
print('\n')

# Qual a melhor reta? verificar qual média é menor
print(dados[['erro_reta', 'erro_pred']].sum())

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

print('Erro abs e quadrado de y_reta')
print(mean_absolute_error(dados.Y, dados.y_reta))
print(mean_squared_error(dados.Y, dados.y_reta))
print('\n')

print('Erro abs e quadrado de y_pred')
print(mean_absolute_error(dados.Y, dados.y_pred))
print(mean_squared_error(dados.Y, dados.y_pred))
print('\n')


