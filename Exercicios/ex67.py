"""Crie uma matriz 3x3 com valores aleatórios entre 1 e 10. Em seguida, calcule a média dos valores em cada linha e imprima o resultado."""

import numpy as np

matriz = np.random.randint(1, 10, (3, 3))

print(f"Matriz: \n{matriz}")
for i in range(0, 3):
    media = np.mean(matriz[i])
    print(f"Média da {i+1}ª linha: {media:.2f}")