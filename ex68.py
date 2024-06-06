"""Crie um array unidimensional com números inteiros de 1 a 20. Em seguida, substitua todos os números pares por zero e 
imprima o array resultante."""

import numpy as np

a1 = np.arange(1, 21)

print(f"Array: {a1}")

a1 = np.where(a1 % 2 == 0, 0, a1)
print(f"Trocando os pares por 0: {a1}")