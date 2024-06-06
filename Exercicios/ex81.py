"""Concatene os DataFrames 'gas_prices' e 'train' horizontalmente (não faz sentido nesse caso, mas é apenas para fins de prática)"""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")
caminho = "train.csv"
caminho_gas = "gas_prices.csv"

train = pd.read_csv(caminho, parse_dates=['datetime'])
gas = pd.read_csv(caminho_gas, parse_dates=['forecast_date', 'origin_date'])

juncao = pd.concat((train, gas), axis=1)
print(juncao)