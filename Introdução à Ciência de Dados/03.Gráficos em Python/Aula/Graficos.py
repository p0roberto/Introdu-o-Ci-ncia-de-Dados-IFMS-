# Matplotlib é uma biblioteca para vizualização de dados para python.

import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
z = [45, 123, 7, 1]

# Linhas
# ls = '-' ; ':' ; '--' ; '-.'
# color = 'r' ; 'g' ; 'hexadecimal'
# linewidth = largura da linha. ex: 3.0

# Marcadores: marker = '*' ; 'p' ; etc

# Títulos, Rótulos, Legendas
# plt.title(); label = 'legenda desejada'; plt.legende(); plt.xlabel('nomeia eixo x); plt.ylabel(nomeia eixo y)

# plt.figure(): é usado para criar uma nova janela de figura, que é onde o gráfico é desenhado.
# Útil quando se quer exibir vários gráficos na mesma janela

figura = plt.figure(figsize = (20,6) )
figura.suptitle('Flamengo')

figura.add_subplot(131) # 1 linha com 3 colunas, na primeira coluna
plt.style.use('ggplot') # Estilos padrões no cheatsheets
plt.bar(x, y, ls = ':', color = 'b', label =  'Valor') # bar = gráfico de barras
plt.title("Meu primeiro gráfico")
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('Aceleração')

figura.add_subplot(132) # 1 linha com 3 colunas, na segunda coluna
plt.style.use('seaborn-v0_8')
plt.plot(x, z, ls = ':', color = 'g', marker = 'p', linewidth = 1.0, label =  'Valor')
plt.title("Meu segundo gráfico")
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('Aceleração')

figura.add_subplot(133) # 1 linha com 3 colunas, na terceira coluna
plt.style.use('seaborn-v0_8') # scatter = gráfico de pontos
plt.scatter(y, z, ls = ':', color = 'r', marker = '*', linewidth = 3.0, label =  'Valor')
plt.title("Meu terceiro gráfico")
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('Aceleração')

plt.show()