"""Realize um merge entre 'gas_prices' e 'train' usando a coluna 'origin_date' e 'datetime'"""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")
caminho = "train.csv"
caminho_gas = "gas_prices.csv"

train = pd.read_csv(caminho, parse_dates=['datetime'])
gas = pd.read_csv(caminho_gas, parse_dates=['forecast_date', 'origin_date'])

gas = gas.rename(columns = {'origin_date':'date'})
train['date'] = train['datetime'].dt.date
train['date'] = pd.to_datetime(train['date'])

merged = pd.merge(left=gas, right=train, on='date', how='left')
print(merged)