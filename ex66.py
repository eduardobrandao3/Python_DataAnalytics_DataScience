"""Crie um array unidimensional com os primeiros 10 números primos e, em seguida, imprima apenas os números ímpares desse array."""

import numpy as np

a1 = np.array(list(), dtype=int)
cont = 0
i = 2
while cont < 10:
    divisores = 0
    for d in range(1, i+1):
        if i % d == 0:
            divisores += 1
    
    if divisores == 2:
        a1 = np.append(a1, i)
        cont += 1
    
    i += 1

print(a1)
primos_impares = a1[np.where(a1 % 2 != 0)]

print(f"Primos ímpares: {primos_impares}")
