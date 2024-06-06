"""Suponha que você tenha um modelo que retorna probabilidades contínuas e você deseja aplicar um threshold para atribuir 
classes binárias (0 ou 1). Crie um programa que simule esse processo usando a função np.where() do NumPy.

A lista de probabilidades é a seguinte: y_pred_probs = np.array([0.4, 0.6, 0.2. 0.3, 0.8, 0.9, 0.1, 0.8, 0.4, 0.5])"""

import numpy as np

y_pred_probs = np.array([0.4, 0.6, 0.2, 0.3, 0.8, 0.9, 0.1, 0.8, 0.4, 0.5])

print(np.where(y_pred_probs >= 0.5, 1, 0))