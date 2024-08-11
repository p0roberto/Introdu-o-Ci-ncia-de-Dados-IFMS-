# str (String)
# int (Inteiro)
# float (Decimal)
# bool (True/False)

nome_completo = input('Nome Completo: ')
# print(type(nome_completo))

idade = input('Idade: ')
idade = int(idade) # casting para inteiro
if(idade > 18): is_maior_idade = True
else: is_maior_idade = False

cidade: str # anotação, tipo da variável, não se impõe sobre o compilador
cidade = input('Cidade em que mora: ')

casas_pi = float(input('Digite o número Pi o quanto conseguir: ')) # outra forma de fazer casting para outro tipo

print(nome_completo)
if(is_maior_idade): print('Maior de idade')
print('Mora em',cidade)
print('Pi =',casas_pi)
