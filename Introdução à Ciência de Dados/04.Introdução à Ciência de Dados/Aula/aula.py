# Ciencia de dados é o processo de extrair insights e conhecimento útel de dados,
# utilizando técnicas de estátisica, aprendizado de máquina e outras disciplinas relacionadas, isso inclui Colet: Limpeza; Análise e Vizualização de Dados.
# Workflow:
# Etapa 1: Acquire (adquirir os dados)
# Etapa 2: Prepare (preparar os dados)
# Etapa 3: Analyze (analisar os dados)
# Etapa 4: Report (Conclusão com base nos dados)
# Etapa 5: Actions (Soluções com base nos dados)

# Faça a pergunta certa: Qual o probelma que tentaremos resolver?, Esse problema é um problema de Ciencia de dados?
# Avaliar a situação: riscos, benefícios, contingências, regulamentos, recursos, requisito
# Definir Meta: Qual o objetivo? Qual o critério de sucesso?

# Habilidades desejadas:
# Técnico: Matemática e Estatística; Python ou R; Conhecimendo do domínio; Conhecimento de dados
# Interpessoal: Curiosidade; Storytelling Skills; Pensamento Estruturado

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configurações para exibir todo o DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

# Entender os dados: tamanho do conjunto de dados; atributos; existe valores faltantes?
data = pd.read_csv('Arquivos/student/student-mat.csv', delimiter=';')
print("\n\n")
print(data.info()) # Verifica o tamanho e os tipos de dados
print("\n\n")
print(data.head()) # Mostra as primeiras linhas do DataFrame
print("\n\n")
print(data.isnull().sum()) # Mostra quantos valores nulos existem em cada coluna
print("\n\n")

# Correlação dos Atributos: -1 a 1
# Mede se há e qual o grau de dependencia entre variáveis
# Correlação positiva: possuem relação direta, crescem ou decrescem juntas
# Correlação negativa: quando há correlação mas crescem e decrescem inversamente
# Não ter correlação

numeric_data = data.select_dtypes(include=[np.number])
print(numeric_data.corr()) # Calcula e imprime a correlação entre colunas numéricas
print("\n\n")

print(numeric_data.corr()['G3']) # Correalação dos atributos em relação a terceira nota
print("\n\n")

# Investigação sobre os dados:
# O desejo de fazer faculdade interfere nas notas?
# 21 higher - wants to take higher education (binary: yes or no)
# 31 G1 - first period grade (numeric: from 0 to 20)
# 32 G2 - second period grade (numeric: from 0 to 20)
# 33 G3 - final grade (numeric: from 0 to 20, output target)

print(data.groupby('higher')[numeric_data.columns].mean()) # Correlação de higher com as demais colunas
print("\n\n")
print(data['G3'].mean()) # Media geral na G3
print("\n\n")
print(data.groupby('higher')['higher'].count()) # Quantidade de yes e no
print("\n\n")
nvp = (20 / 395)*100 # quantos porcento nao desejam ir para a faculdade
print('Não desejam ir para a faculdade (em %): ', nvp)
print("\n\n")
print(data.groupby('higher')['G3'].std()) # Calcula o desvio padrão da N3

# Histograma
plt.style.use('seaborn-v0_8')
plt.hist(data['G3'], bins = 20, label = 'Número de Alunos')
plt.title('Histograma Nota 3')
plt.legend()
plt.xlabel('Nota')
plt.ylabel('Quantidade')
plt.show()