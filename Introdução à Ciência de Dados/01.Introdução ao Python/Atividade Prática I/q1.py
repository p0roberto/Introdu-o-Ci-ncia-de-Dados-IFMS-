# Escreva um programa que leia uma lista de números inteiros do usuário e exiba a soma de todos os números ímpares na lista.

def soma_impar(lista: list) -> int: # Função para somar os números ímpares da lista
    soma = 0
    for i in lista:
        if i % 2 == 1:
            soma += i
    return soma

lista = []
quant = int(input('Quantos elementos voce quer inserir: '))

for _ in range(quant):
    lista.append(int(input("Digite um númeiro inteiro: ")))

print('Soma dos números ímpares da lista:',soma_impar(lista))