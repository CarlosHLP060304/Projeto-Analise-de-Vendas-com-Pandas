import pandas as pd

# Carregar o conjunto de dados de vendas
dados_vendas = pd.read_csv('dados_vendas.csv')

# Visualizar as primeiras linhas do conjunto de dados
print("Primeiras linhas do conjunto de dados:")
print(dados_vendas.head())

# Verificar informações sobre o conjunto de dados
print("\nInformações sobre o conjunto de dados:")
print(dados_vendas.info())

# Verificar estatísticas básicas dos dados numéricos
print("\nEstatísticas básicas dos dados numéricos:")
print(dados_vendas.describe())

# Verificar se há valores nulos no conjunto de dados
print("\nValores nulos no conjunto de dados:")
print(dados_vendas.isnull().sum())

# Limpar os dados (remover linhas com valores nulos)
dados_vendas_limpos = dados_vendas.dropna()

# Verificar o tamanho do conjunto de dados após a limpeza
print("\nTamanho do conjunto de dados após a limpeza:", dados_vendas_limpos.shape)

# Calcular a média das vendas por país
media_vendas_por_pais = dados_vendas_limpos.groupby('Country')['Sales'].mean()

# Visualizar a média das vendas por país
print("\nMédia das vendas por país:")
print(media_vendas_por_pais)

# Visualizar as vendas totais por categoria de produto
vendas_por_categoria = dados_vendas_limpos.groupby('Category')['Sales'].sum()

# Visualizar as vendas por categoria de produto
print("\nVendas totais por categoria de produto:")
print(vendas_por_categoria)

# Plotar um gráfico de barras das vendas por categoria de produto
import matplotlib.pyplot as plt

vendas_por_categoria.plot(kind='bar', color='skyblue')
plt.title('Vendas por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.xticks(rotation=45)
plt.show()
