"""Objetivo
Criar um gráfico de dispersão que compare duas variáveis, como peso e altura.
Instruções:
Gere duas listas de valores aleatórios que representem peso e altura.
Use plt.scatter() para criar o gráfico de dispersão.
Adicione um título, rótulos para os eixos e personalize a cor e o estilo dos marcadores."""

import matplotlib.pyplot as plt
import numpy as np


altura = np.round(np.random.uniform(1, 2.20, 10), 2)
peso = np.round(np.random.uniform(40, 120, 10), 2)
print(f"Altura: {altura}")
print(f"Peso: {peso}")


plt.figure(figsize=(10,8))
plt.scatter(altura, peso, marker="o", color="#48D1CC")
plt.title("Peso X Altura")
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.xlim(0, max(altura)+0.5)
plt.ylim(0, max(peso)+10)
plt.show()