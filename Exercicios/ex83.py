"""Cria uma nova coluna na tabela 'train' que seja o dobro do valor da coluna 'target'"""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")
caminho = "train.csv"

arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

arquivo['dobro_target'] = arquivo['target'] * 2

print(arquivo)