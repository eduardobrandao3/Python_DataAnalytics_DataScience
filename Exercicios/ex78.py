"""Veja uma análise estatística breve dos seus dados."""

import pandas as pd
import os

os.chdir("C:/Users/edub_/OneDrive/Área de Trabalho/EXERCÍCIOS FCCD/PYTHON/arquivos_csv/")

caminho = "train.csv"

arquivo = pd.read_csv(caminho, parse_dates=['datetime'])

print(f"Análise estatística breve: {arquivo.describe().T}")
