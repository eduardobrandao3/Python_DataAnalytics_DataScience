"""Verifique a quantidade de valores nulos na coluna 'forecast_date'. A porcentagem e a quantidade total de nulos."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "gas_prices.csv"

precos_gas = pd.read_csv(caminho, parse_dates=['forecast_date', 'origin_date'])

qnt_nulos_forecast = precos_gas['forecast_date'].isnull().sum()

print(f"Quantidade de nulos em 'forecast_date': {qnt_nulos_forecast}\nPorcentagem: {qnt_nulos_forecast/len(precos_gas) * 100}%")