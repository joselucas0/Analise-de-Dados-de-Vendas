# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Função principal para carregar, limpar e analisar dados
def main():
    # Carregar os dados de vendas
    vendas_df = pd.read_csv('vendas.csv')

    # Limpar os dados
    vendas_df = limpar_dados(vendas_df)

    # Analisar os dados
    analisar_dados(vendas_df)

    # Visualizar os dados
    visualizar_dados(vendas_df)

# Função para limpar os dados
def limpar_dados(df):
    # Remover duplicatas
    df = df.drop_duplicates()

    # Tratar valores nulos (exemplo: removendo linhas com valores nulos)
    df = df.dropna()

    return df

# Função para analisar os dados
def analisar_dados(df):
    # Produtos mais vendidos
    produtos_mais_vendidos = df['Produto'].value_counts().head(10)
    print("Produtos mais vendidos:")
    print(produtos_mais_vendidos)

    # Meses com maior volume de vendas
    df['Data'] = pd.to_datetime(df['Data'])
    df['Mes'] = df['Data'].dt.month
    vendas_por_mes = df.groupby('Mes')['Quantidade'].sum()
    print("Vendas por mês:")
    print(vendas_por_mes)

    # Regiões com maior faturamento
    faturamento_por_regiao = df.groupby('Região')['Faturamento'].sum()
    print("Faturamento por região:")
    print(faturamento_por_regiao)

# Função para visualizar os dados
def visualizar_dados(df):
    # Produtos mais vendidos
    produtos_mais_vendidos = df['Produto'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=produtos_mais_vendidos.values, y=produtos_mais_vendidos.index, palette='viridis')
    plt.title('Top 10 Produtos Mais Vendidos')
    plt.xlabel('Quantidade Vendida')
    plt.ylabel('Produto')
    plt.show()

    # Vendas por mês
    df['Mes'] = df['Data'].dt.month
    vendas_por_mes = df.groupby('Mes')['Quantidade'].sum()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=vendas_por_mes.index, y=vendas_por_mes.values, marker='o')
    plt.title('Vendas por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade Vendida')
    plt.show()

    # Faturamento por região
    faturamento_por_regiao = df.groupby('Região')['Faturamento'].sum()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=faturamento_por_regiao.values, y=faturamento_por_regiao.index, palette='viridis')
    plt.title('Faturamento por Região')
    plt.xlabel('Faturamento')
    plt.ylabel('Região')
    plt.show()

# Executar a função principal
if __name__ == "__main__":
    main()
