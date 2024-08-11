# Escreva um programa que crie uma lista de números inteiros aleatórios e, em seguida, imprima o maior e o menor número da lista.
# Para criar uma lista de números inteiros aleatórios, você pode usar a biblioteca random do Python.

import random

# Definindo o tamanho da lista e os limites dos números aleatórios
tamanho_da_lista = 10
limite_inferior = 1
limite_superior = 100

# Criando a lista de números aleatórios
lista_aleatoria = [random.randint(limite_inferior, limite_superior) for _ in range(tamanho_da_lista)]

min = 100
max = 0

print(lista_aleatoria)

for i in lista_aleatoria:
    if i < min:
        min = i
    if i > max:
        max = i

print('Menor elemento:',min,'\nMaior Elemento:',max)