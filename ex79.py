"""Analise a quantidade e quais são de valores únicos na coluna 'is_business'."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "train.csv"

arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

print(f"Quantidade de únicos na coluna 'is_business': {arquivo['is_business'].nunique()}")

print(f"Valores que são únicos na coluna 'is_business': {arquivo['is_business'].unique()}")

print(arquivo.is_business.value_counts())