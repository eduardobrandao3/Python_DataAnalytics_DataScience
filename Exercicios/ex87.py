"""Objetivo
Criar um gráfico de barra para exibir as vendas de diferentes produtos.
Instruções:
Crie uma lista de produtos (por exemplo, "Produto A", "Produto B", "Produto C").
Associe um valor de vendas para cada produto.
Use plt.bar() para criar o gráfico de barras.
Adicione um título, rótulos para os eixos e personalize as cores das barras."""

import matplotlib.pyplot as plt

produtos = ['Produto A', 'Produto B', 'Produto C']
valor = [375000.50, 147000.98, 37152.00]

plt.figure("Grafico Vendas X Produto", figsize= (10, 7))
plt.bar(produtos, valor, color="#6959CD")
plt.title("Vendas X Produto")
plt.xlabel("Produtos")
plt.ylabel("R$")
plt.show()