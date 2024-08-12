# Escreva um programa que crie uma matriz aleatória de 3x3 utilizando a biblioteca NumPy, e, em seguida, imprima a matriz transposta.

import numpy as np

matriz = np.random.rand(3, 3)*10
matriz = matriz.astype(int)
print(matriz)

matriz = np.transpose(matriz)
print('\n')
print(matriz)