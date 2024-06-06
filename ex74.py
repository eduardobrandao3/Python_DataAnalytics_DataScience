"""Ordene o DataFrame pela coluna 'highest_price_per_mwh' em ordem decrescente."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "gas_prices.csv"

precos_gas = pd.read_csv(caminho, parse_dates=['forecast_date', 'origin_date'])

precos_gas = precos_gas.sort_values(by = 'highest_price_per_mwh', ascending=False)

print(precos_gas)