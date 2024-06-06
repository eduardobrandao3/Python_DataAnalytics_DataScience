"""Objetivo:
Criar um histograma para visualizar a distribuição de uma variável contínua, como o salário.
Instruções:
Gere uma lista de salários usando uma distribuição aleatória.
Use plt.hist() para criar o histograma.
Especifique o número de bins.
Adicione um título, rótulos para os eixos e personalize a cor do histograma."""

import matplotlib.pyplot as plt
import numpy as np

salario = np.random.exponential(scale= 1300, size= 1000)

plt.figure(figsize=(8, 6))
plt.hist(salario, bins=30, color="#FF15F4", edgecolor="black")
plt.title("Quantidade de funcionarios X salário")
plt.xlabel("Salário")
plt.ylabel("Quantidade de funcionários")
plt.show()