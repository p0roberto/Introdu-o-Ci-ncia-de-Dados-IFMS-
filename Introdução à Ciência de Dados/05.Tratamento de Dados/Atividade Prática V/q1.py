# Você é um cientista de dados que está trabalhando com o conjunto de dados "Breast Cancer Wisconsin".
# Você precisa limpar os dados do conjunto de dados e remover as linhas com valores ausentes (NaN) antes de começar a fazer as análises. 
# Escreva um programa em Python utilizando a biblioteca Scikit-learn (sklearn) e a função dropna() do Pandas para realizar essa tarefa.

import pandas as pd
import sklearn as sk

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
breast_cancer_df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)

print("\nInformações sobre o DataFrame:")
print(breast_cancer_df.info())

breast_cancer_df = breast_cancer_df.dropna()
print('\n\n')

print(breast_cancer_df.head())
