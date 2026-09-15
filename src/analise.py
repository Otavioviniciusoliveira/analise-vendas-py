import pandas as pd

# Carrega os dados
df = pd.read_csv("data/dados.csv")

# Calcula o faturamento de cada venda
df["Faturamento"] = df["Quantidade"] * df["Preço"]

# Informações gerais
faturamento_total = df["Faturamento"].sum()
quantidade_total = df["Quantidade"].sum()
ticket_medio = df["Faturamento"].mean()

# Produto mais vendido
produto_mais_vendido = (
    df.groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# Categoria com maior faturamento
categoria_maior_faturamento = (
    df.groupby("Categoria")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

print("=== ANÁLISE DE VENDAS ===")
print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Quantidade total vendida: {quantidade_total}")
print(f"Ticket médio: R$ {ticket_medio:,.2f}")
print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Categoria com maior faturamento: {categoria_maior_faturamento}")