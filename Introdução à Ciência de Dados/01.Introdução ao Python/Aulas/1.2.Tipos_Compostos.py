# Lista (Basicamente um vetor)

notas = [0,0,0]

notas[0] = float(input('Sua nota na p1: '))
notas[1] = float(input('Sua nota na p2: '))
notas[2] = float(input('Sua nota na p3: '))

media = (notas[0] + notas[1] + notas[2])/3

print('Notas:',notas)
print(f'Sua média artimética é:{media: .2f}')
if(media < 6): print('Reprovado!')
else: print('Aprovado!')

# Listas não necessariamente precisam armazenar variáveis de um mesmo tipo. Exemplo:

lista = ['Álgebra', 7.8, 'TAP', 7]
print('Exemplo de lista com vários tipos:',lista)

# Tuplas (Semelhante a Lista, porém não aceita alteração após sua declaraçã)

frutas_tupla = ('Uva', 'Manga', 7, 'Tamara')
print(frutas_tupla)

# Dicionário (Semelhante ao Map, ou Pair, em C++)
# Armazena a 'Chave' e o 'Valor'

primos = {1:2, 2:3, 3:5, 4:7, 5:11}
print(primos)