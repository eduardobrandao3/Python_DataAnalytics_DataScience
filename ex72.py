"""Carregue o arquivo 'gas_prices.csv' e visualize as 5 primeiras linhas, a dimensão dos dados e os tipos de dados de cada coluna. 
Verifique se há colunas que representam datas. Se sim, transforme-a(s) para o formato adequado."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "gas_prices.csv"

precos_gas = pd.read_csv(caminho, parse_dates=['forecast_date', 'origin_date'])

print(f"Primeiras 5 linhas: \n{precos_gas[0:5][:]}\n")
print(f"Dimensões: {precos_gas.shape}\n")
print(f"Informações: {precos_gas.info()}")