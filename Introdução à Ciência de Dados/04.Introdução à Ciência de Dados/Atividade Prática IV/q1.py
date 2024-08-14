# Você é um cientista de dados e precisa analisar a relação entre as variáveis altura e peso em uma amostra de pessoas. 
# Escreva um programa contendo as informações de altura e peso de cada pessoa, calcule a correlação entre as duas variáveis e exiba um gráfico de dispersão com as duas variáveis.

import pandas as pd
import matplotlib.pyplot as plt

# Dados
pesos = [60.2, 73.5, 64.0, 68.1, 87.0, 75.4, 70.0, 76.8, 81.2, 58.9, 69.7, 92.5, 78.6, 66.3, 71.8, 79.5, 63.7, 72.5, 83.0, 76.1]
alturas = [1.65, 1.75, 1.68, 1.72, 1.90, 1.80, 1.77, 1.82, 1.87, 1.60, 1.74, 2.00, 1.78, 1.67, 1.73, 1.83, 1.62, 1.76, 1.90, 1.79]

# Criar um DataFrame
df = pd.DataFrame({
    'Peso (kg)': pesos,
    'Altura (m)': alturas
})

# Correlação
correlacao = df.corr().iloc[0, 1]
print('\nDataFrame:\n')
print(df)
print('\nCorrelção entre peso e altura:\n')
print(df.corr())

# Criar o gráfico de dispersão e exibir correlação
figura = plt.figure(figsize=(12, 6))

figura.add_subplot(121)
plt.style.use('seaborn-v0_8')
plt.scatter(alturas, pesos, color='blue', marker='o')
plt.title('Gráfico de Dispersão: Peso vs Altura')
plt.xlabel('Altura (m)')
plt.ylabel('Peso (kg)')

ax2 = figura.add_subplot(122)
ax2.axis('off')
ax2.text(0.5, 0.5, f'Correlação: {correlacao:.5f}', fontsize=16, ha='center', va='center', color = 'blue')

# Exibir o gráfico
plt.show()
