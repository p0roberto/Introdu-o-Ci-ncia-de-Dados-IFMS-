# Preparar os dados para que eles possam ser analizados

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Arquivos/football_players.txt', sep = '\t', skiprows = 27)
# separador dos dados é um espaço em branco ('\t); skirows = 27, pula as 27 primeiras linahs
print(data)
print("\n\n")

# Tratas dados faltantes
# Tipos de Cópia de dataframe
import copy

data_copia = copy.copy(data) # passagem por referencia, como um ponteiro
data_copia2 = copy.deepcopy(data) # copia de fato os dados para um novo dataframe

print(data.info()) 
print("\n\n")
print(data.isnull().any()) # possui dados faltantes em alguma coluna?
print("\n\n")

# Removendo linhas e colunas de dados faltantes
data_copia2.dropna(axis = 0, inplace = True) # Axis = 0, linhas; Axis = 1, colunas; inplace, modifica o dataframe
print(data_copia2)
print('\n\n')

data_copia3 = copy.deepcopy(data)
data_copia3.dropna(axis = 1, inplace = True)
print(data_copia3)
print('\n\n')
# print(data_copia3.isnull().any()) # possui dados faltantes em alguma coluna?

# Substituir dados faltantes por valor médio, mediana ou moda

print(data['cm'].isnull().any()) # Possui alturas faltantes?
print('\n\n')

if data['cm'].isnull().any(): # Substituir dados faltantes na coluna 'cm' pela média
    data['cm'] = data['cm'].fillna(data['cm'].mean())

print(data['cm'])
print('\n\n')

print(data['kg'].isnull().any()) # Possui dados de kg faltantes?
print('\n\n')

if data['kg'].isnull().any(): # Substituir dados faltantes na coluna 'kg' pela mediana
    data['kg'] = data['kg'].fillna(data['kg'].median())

print(data['kg'])
print('\n\n')

print(data['goal'].isnull().any()) # Possui dados de kg faltantes?
print('\n\n')

if data['goal'].isnull().any(): # Substituir dados faltantes na coluna 'goal' por 0, visto que não fizeram gol
    data['goal'] = data['goal'].fillna(0)

print(data['goal'])

if data['ass'].isnull().any(): # Substituir dados faltantes na coluna 'ass' por 0, visto que não deram assistencia
    data['ass'] = data['ass'].fillna(0)

plt.scatter(x = data['kg'], y = data['cm'])
plt.xlabel('peso')
plt.ylabel('altura')
plt.title('Peso x Altura')
plt.show()

plt.hist(data['age'], bins = 42)
plt.xlabel('Idade')
plt.ylabel('Quantidade')
plt.title('Idades')
plt.show()

plt.scatter(x = data['goal'], y = data['pos'])
plt.xlabel('gols')
plt.ylabel('posição')
plt.title('Gols x Posição')
plt.show()
