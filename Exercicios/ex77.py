"""Carregue o arquivo 'train.csv' e visualize as 5 primeiras linhas, a dimensão dos dados e os tipos de dados de cada coluna. 
Verifique se há colunas que representam datas. Se sim, transforme-a(s) para o formato adequado."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "train.csv"

arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

print(arquivo.head(5))
print(f"\nDimensão: {arquivo.shape}\n")
print(f"Informações: {arquivo.info()}\n")