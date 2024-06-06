"""Crie um array unidimensional com 100 números inteiros aleatórios. Encontre o valor máximo, o valor mínimo, a 
média e o desvio padrão desses números e imprima os resultados."""

import numpy as np

a1 = np.random.randint(1, 100, 100)

print(f"Array: {a1}")

print(f"Valor máximo: {a1.max()}")
print(f"Valor mínimo: {a1.min()}")
print(f"Média (2 casas decimais): {np.mean(a1):.2f}")
print(f"Desvio padrão (2 casas decimais): {np.std(a1):.2f}")

