"""Na coluna 'datetime' do DataFrame 'train', extraia o ano, a hora e o dia da semana."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")
caminho = "train.csv"

arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

print(arquivo['datetime'].dt.year)
print(arquivo['datetime'].dt.hour)
print(arquivo['datetime'].dt.dayofweek)
