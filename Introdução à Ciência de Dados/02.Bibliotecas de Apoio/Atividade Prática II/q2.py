# Escreva um programa que crie um dataframe com informações de produtos e preços e, em seguida, calcule a média de preços dos produtos.

import pandas as pd

dados = { # Cria um dicionário com os dados dos produtos e preços
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Preço': [10.50, 23.99, 5.75, 15.00]
}

# Cria o DataFrame a partir do dicionário
df = pd.DataFrame(dados)

print("DataFrame:")
print(df)

media_preco = df['Preço'].mean() # Calcula a média dos preços

print("\nMédia dos preços:")
print(media_preco)
