"""Objetivo
Criar um gráfico de linha que mostre a função seno para um intervalo de 0 a 2π.
Instruções:
Gere um conjunto de pontos x de 0 a 2π.
Calcule os valores de seno para esses pontos.
Crie um gráfico de linha utilizando plt.plot().
Adicione um título e rótulos para os eixos X e Y.
Personalize a cor e o estilo da linha."""

import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0, 2*np.pi + 0.02, 0.1)

y = np.sin(x)

plt.figure(figsize=(10, 8))
plt.plot(x, y, color="#48D1CC", linestyle="-")
plt.title("Seno de X")
plt.xlabel("x")
plt.ylabel("sen(x)")
plt.ylim(-1, 1)
plt.grid(True)
plt.show()

