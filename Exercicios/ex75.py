"""Filtre os registros onde 'lowest_price_per_mwh' é maior que 46."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "gas_prices.csv"

precos_gas = pd.read_csv(caminho, parse_dates=['forecast_date', 'origin_date'])

print(precos_gas.query("lowest_price_per_mwh > 46"))
