# NumPy é uma biblioteca matemática, que nos permite fazer computação de forma eficiente e eficaz.

import numpy as np

arr = [1, 2, 3]
print(arr)

arr2 = np.array([1, 2, 3])
print(arr2)

arr3 = np.arange(0, 100, 1, 'int') # Função que cria uma progressão aritmética de números
print(arr3)

arr3 = np.reshape(arr3, (10,10)) # Função que modifica a forma de um array existente sem alterar seus dados
print(arr3) # Neste exemplo, arr3 passa a ser apresentado como uma matriz 10x10 

print(arr3[1,4]) # Printa o elemento na posição linha 1 coluna 4 (indexado no 0)

# A biblioteca NumPY fornece uma série de operações matemáticas para trabalhar com matrizes.
# Incluindo adição, sbutração, multiplicação, divisão, etc.
matriz1 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matriz2 = np.array([[1, 0, 2], [0, 1, 2], [4, 1, 6]])
matriz3 = matriz1 - matriz2
matriz3 = matriz3 * 2
print(matriz3)

soma = np.sum(matriz3) # Função que soma todos os elementos de um array
print(soma)

matriz4 = np.zeros((3, 3, 3, 3), 'int') # Função que cria um array de zeros com a forma especificada
print(matriz4)

matrizidentidade_r9 = np.eye(9, 9, 0, 'int') # Função que cria uma matriz identidade com a forma especificada
print(matrizidentidade_r9)

aleatorio = int(np.random.rand()*1000) # Função que gera números aleatŕios de uma distruição uniforme no intervalo [0,1]
print(aleatorio)

matriz6 = np.random.rand(3, 3)*100 # Criando uma matriz de números aleatórios
print(matriz6)

arr4 = np.random.rand(5)*100
print(arr4)
arr4 = np.append(arr4, 20.14235) # Adiciona um valor ao array
print(arr4)

diff = np.diff(arr4) # Função que calcula a diferença entre elementos consecutuvos de um array
print(diff)

arr5 = np.array([1, 2, 3])
arr6 = np.array([3, 4, 5])
arr_vs = np.vstack((arr5, arr6)) # Empilha arrays
print(arr_vs)

arr_colm = np.column_stack((arr5, arr6)) # Gera a forma transposta
print(arr_colm)