"""Faça um programa que receba informações de 4 pessoas. As informações são: "nome", "idade" e "cidade". 
Armazene essas informações em uma lista de dicionários e, ao final, retorne a seguinte mensagem:
 "{nome} é o mais velho e mora em {cidade}.''"""

def indiceMaisVelho (lista):
    """
    A funcao 'indiceMaisVelho' retorna o indice do elemento da lista que possui a maior idade

    Parametros:
    lista: lista de dicionarios que contem nome, idade e cidade de cada pessoa
    """
    velho = lista[0]["idade"]
    indice = 0
    for i in range(0, len(lista)):
        if (lista[i]["idade"] > velho):
            velho = lista[i]["idade"] 
            indice = i
    
    return indice


lista = list()

#receber informações de 4 pessoas
for i in range(0, 4):
    dicionario = dict()
    nome = input(f"Digite o nome do(a) {i+1}°: ").title()
    dicionario["nome"] = nome

    idade = int(input(f"Digite a idade do(a) {i+1}°: "))
    dicionario["idade"] = idade

    cidade = input(f"Digite a cidade do(a) {i+1}°: ").title()
    dicionario["cidade"] = cidade

    #colocando as informações(dicionario) na lista
    lista.append(dicionario)

pos_maisVelho = indiceMaisVelho(lista)

print(f"{lista[pos_maisVelho]["nome"]} é o(a) mais velho(a) e mora em {lista[pos_maisVelho]["cidade"]}")