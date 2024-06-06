"""Faça um programa que, utilizando a mesma lógica do exercício anterior, retorne o maior elemento de cada uma das linhas da matriz
lembrando: Faça um programa que receba duas entradas: a quantidade de linhas e colunas, nessa ordem, de uma matriz. 
Após isso, solicite que ele digite o valor correspondente a cada posição dessa matriz: """

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

while(linhas <= 0 or colunas <= 0):
    print("A quantidade de linhas e de colunas tem que ser maior que zero")
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))

matriz = []

for i in range(0, linhas):
    aux = []
    for j in range(0, colunas):
        valor = int(input(F"Digite o valor para a linha {i} e coluna {j}: "))
        aux.append(valor)

    matriz.append(aux)

#para retornar o maior de cada linha
for i in range(0, linhas):
    maior = matriz[i][0]
    for j in range(0, colunas):
        if (matriz[i][j] > maior):
            maior = matriz[i][j]
    print(f"O maior da linha {i} é: {maior}")
