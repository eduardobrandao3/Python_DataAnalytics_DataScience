"""Desenvolva um programa que inclua uma função chamada cria_dataframe que recebe duas listas: uma com o nome das colunas e 
a outra com os valores que cada coluna terá. A função deve retornar um dataframe."""

import pandas as pd

def cria_dataframe (listaColuna, listaValores):
    tabela = pd.DataFrame(listaValores, columns=listaColuna)
    return tabela

colunas = ['Nome', 'Idade', 'Cidade']

# Lista de valores
valores = [
    ['João', 25, 'São Paulo'],
    ['Maria', 30, 'Rio de Janeiro'],
    ['Pedro', 28, 'Belo Horizonte']
]

print(cria_dataframe(colunas, valores))