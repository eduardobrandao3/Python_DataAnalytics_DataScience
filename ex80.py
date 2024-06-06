"""Selecione as linhas 10 a 20 e as colunas 'county' e 'target'"""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "train.csv"
arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

print("Linhas de 10 a 20 e colunas 'county' e 'target'")
print(arquivo.loc[10:20, ('county', 'target')])