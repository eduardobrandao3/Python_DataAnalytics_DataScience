"""Desenvolva um programa que inclua uma função chamada numeros_unicos que recebe duas listas como parâmetros e retorna 
uma lista contendo apenas os elementos que são únicos em ambas as listas. Teste a função com diferentes conjuntos de listas. 
As listas não tem o mesmo tamanho necessariamente."""

def numeros_unicos(lista1, lista2):
    setA = set(lista1)
    setB = set(lista2)
    
    setC = setA & setB
    return list(setC)

listaA = [1, 2, 3]
listaB = [9, 8, 3, 3, 7, 1]

print(numeros_unicos(listaA, listaB))