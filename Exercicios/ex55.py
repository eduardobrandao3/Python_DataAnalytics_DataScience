"""Desenvolva um programa que inclua uma função chamada ordena_lista que ordena uma lista de números em ordem crescente. 
Teste a função com diferentes listas. Não utilize a função sorted nem o método sort."""

def ordena_lista (lista):
    """
    A funcao 'ordena_lista' ordena os elementos de forma crescente sem utilizar a função sorted ou o método sort

    Parâmetros:
    lista: lista de números
    """
    for i in range(0, len(lista)-1):
        menor = lista[i]
        pos = i
        for j in range(i+1, len(lista)):
            if lista[j] < menor:
                menor = lista[j]
                pos = j
        
        aux = lista[i]
        lista[i] = menor
        lista[pos] = aux

    return lista


numeros = [15, 9, 27, 1, 18, 41, 30, 12, 4, 22]
print(f"Em ordem de entrada: \n{numeros}\n")
print("Em ordem crescente: \n")
print(ordena_lista(numeros))