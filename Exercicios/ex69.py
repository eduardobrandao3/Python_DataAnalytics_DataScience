"""Crie duas matrizes 2x2 e realize a multiplicação de matriz entre elas. Imprima a matriz resultante."""

import numpy as np

mat1 = np.random.randint(1, 20, (2, 2))
mat2 = np.random.randint(1, 20, (2, 2))

print(f"Matriz 1:\n{mat1}\n")
print(f"Matriz 2:\n{mat2}\n")

multp = np.matmul(mat1, mat2)

print(f"Multiplicação: \n{multp}")