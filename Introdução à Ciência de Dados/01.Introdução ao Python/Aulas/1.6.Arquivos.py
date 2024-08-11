f = open('Arquivos/teste.txt','a') # Abre o arquivo, ou o cria, caso não exista
# a = adicionar informação; w = sobrescrever informação; r = ler informação 
f.write('Teste bem sucecido!\n') # Grava no arquivo
f.close() # Fecha  o arquivo

with open('Arquivos/teste.txt', 'r') as f:
    # fecha o arquivo após sair do bloco identado
    s = f.read() # 's' recebe o conteúdo do arquivo
    print(s)

try:
    f = open('Arquivos/arquivo.txt')
    s = f.read()
    print(s)
    f.close()
except: print('Não foi possível abrir o arquivo (arquivo.txt)') 

print('\nFim\n')