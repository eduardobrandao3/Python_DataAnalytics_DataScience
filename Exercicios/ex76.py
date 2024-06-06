"""Agrupe os dados por 'origin_date' e calcule a média do 'highest_price_per_mwh'"""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "gas_prices.csv"

precos_gas = pd.read_csv(caminho, parse_dates=['forecast_date', 'origin_date'])

precos_gas = precos_gas.groupby('origin_date').mean()['highest_price_per_mwh']

print(precos_gas)