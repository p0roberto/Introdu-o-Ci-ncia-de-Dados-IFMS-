# Você é um analista de dados de uma empresa de alimentos e recebeu a tarefa de analisar as vendas de um novo produto em diferentes regiões do Brasil. 
# Você precisa criar um gráfico que mostre a quantidade de vendas do produto em cada região, de forma clara e objetiva. 
# Use a biblioteca Matplotlib do Python para criar um gráfico de barras que mostre a quantidade de vendas em cada região.

import matplotlib.pyplot as plt

# Dados
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
vendas = [1500, 2500, 1800, 3000, 2700]

plt.style.use('ggplot')
plt.bar(regioes, vendas, color = 'b', label =  'Quantidade de vendas') # bar = gráfico de barras
plt.title('Análise de vendas do novo produto')
plt.legend()
plt.xlabel('Regiões')
plt.ylabel('Vendas')
plt.show()