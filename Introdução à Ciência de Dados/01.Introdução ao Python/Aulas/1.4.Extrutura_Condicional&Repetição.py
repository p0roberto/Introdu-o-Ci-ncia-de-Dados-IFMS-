# if, else, elif

a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))

teste = a <= b

if teste:
    if a == b:
        print(a,'é igual a',b)
    else:
        print(a,'é menor que', b)
else: 
    print(a,'é maior que',b)


if a == b:
   print(a,'é igual a',b)
elif a < b:
    print(a,'é menor que',b)
elif a > b:
    print(a,'é maior que',b)  


# for

lista = ['manga', 'goiaba', 'melão']

for fruta in lista: # Printa os elementos da lista
    print(fruta)

for i, fruta in enumerate(lista): # Printa os elementos da lista de forma enumerada
    print(i , fruta)

for x in range(10): # Printa os números de 0 a 9
    print(x)

for x in range(6, 12): ## Printa os números de 6 a 11
    print(x)

for x in range(6, 12, 2): # Printa os números de 6 a 11, incrementando +2 posições
    print(x)


for x in range(12, 6, -2): # Printa os números de 12 a 7, incrementando -2 posições
    print(x)
