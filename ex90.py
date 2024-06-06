"""Objetivo:
Combinar gráficos de linha, barra, dispersão e histograma em um layout de subplot.
Instruções:
Crie uma figura com plt.figure() e especifique um tamanho adequado.
Use plt.subplot() para criar um layout de 2x2.
No primeiro subplot, crie um gráfico de linha.
No segundo subplot, crie um gráfico de barra.
No terceiro subplot, crie um gráfico de dispersão.
No quarto subplot, crie um histograma.
Para cada subplot, adicione um título e rótulos apropriados para os eixos."""

import matplotlib.pyplot as plt
import numpy as np

#dados para gráfico de linha
cidades = ['SP', 'MG', 'RJ', 'RN', 'RS', 'ES', 
          'MS', 'MT', 'GO', 'SC']
precipitacoes = np.random.randint(80, 1000, 10)

#dados para gráfico de barras
ano = np.arange(1940, 2011, 10)
habitantes_porkm2 = np.random.randint(0, 30, 8)

#dados para gráfico de dispersão
altura = np.round(np.random.uniform(1.30, 2.2, 10), 2)
peso = np.round(np.random.uniform(40, 115, 10), 2)

#dados para o histograma
tempo_inspecionar = np.round(np.random.uniform(0, 300, 400), 2)


plt.figure(figsize=(10, 5))
#grafico de linhas
plt.subplot(2, 2, 1)
plt.plot(cidades, precipitacoes, color='#00FFFF', label="linha")
plt.legend()
plt.title("Precipitações X Capitais")
plt.xlabel("Capitais")
plt.ylabel("Precipitações (ml)")
plt.xlim(0, len(cidades))
plt.ylim(80, 1000)

#grafico de barras
plt.subplot(2, 2, 2)
plt.bar(ano, habitantes_porkm2, color="#CD853F", width=3, label="Barras")
plt.legend()
plt.title("Densidade demográfica")
plt.xlabel("Ano")
plt.ylabel("Habitantes/km²")
plt.xlim(1940, 2010)
plt.ylim(0, 31)

#grafico de dispersão
plt.subplot(2, 2, 3)
plt.scatter(altura, peso, marker="o", s=30, color="#FF4500", label="Dispersão")
plt.legend()
plt.title("Peso X Altura")
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.grid(True)
plt.xlim(1, 2.5)
plt.ylim(30, 125)

#histograma 
plt.subplot(2, 2, 4)
plt.hist(tempo_inspecionar, bins=20, color="#D8BFD8", edgecolor="gray", label="histograma")
plt.legend()
plt.title("Histograma de tempo para inspecionar(s)")
plt.xlabel("Tempo para inspecionar (s)")
plt.ylabel("Frequência")
plt.xlim(0, 300)
plt.ylim(0, 50)

plt.tight_layout()
plt.show()