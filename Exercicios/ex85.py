"""Identifique e exclua as linhas onde temos dados faltantes na coluna 'target' do DataFrame 'train'"""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")
caminho = "train.csv"

arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

indices_nulos = arquivo[arquivo['target'].isnull()].index

arquivo = arquivo.drop(index=indices_nulos)

print(arquivo)
