# Machine Learning:
# Habilidade da máquina de melhorar sua performance em uma tarefa e aprender durante o processo.
# A inferência lógica indutiva é a base do Aprendizado Indutivo de Máquina,
# que, a partir de um conjunto de instâncias específicas, busca generalizar uma expressão de conceito
# para classificar novas instâncias ou agrupá-las de forma mais homogênea.
# O conjunto de instâncias fornecido a um algoritmo indutivo é chamado de conjunto de treinamento.

# Tipos de Aprendizado de Máquina:
#   Aprendizado Supervisionado:
#       - Classificação: Detecção de Fraudes, Classificação de Imagens, Retenção de Clientes, Diagnósticos.
#         (Previsão da categoria de uma amostra com base em características de entrada)
#       - Regressão: Previsões, Predições, Otimização de Processos, Precificação.
#         (Previsão do valor de uma variável dependente com base em variáveis independentes)
#   Aprendizado Não-supervisionado:
#       - Redução Dimensional: Seleção de Recursos, Descoberta de Estruturas, Visualização de Big Data.
#         (Transformação de dados de alta para baixa dimensão, mantendo a informação essencial)
#       - Clusterização: Sistemas de Recomendação, Marketing Direcionado, Segmentação de Clientes.
#         (Agrupamento de dados com base em similaridade)
#   Aprendizado por Reforço:
#       - Aplicações: Navegação de Robôs, Decisões em Tempo Real.

# Biblioteca sklearn:
# O scikit-learn (sklearn) é uma biblioteca poderosa e de fácil uso para aprendizado de máquina em Python.
# Ela oferece ferramentas eficientes para análise de dados e modelagem preditiva, incluindo
# algoritmos de classificação, regressão, clusterização, e redução de dimensionalidade.

import pandas as pd
from sklearn.datasets import load_iris

# Carregamento do conjunto de dados Iris como um DataFrame do pandas
data = load_iris(as_frame=True)
print(data.data)