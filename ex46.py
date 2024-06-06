"""Faça um programa que receba duas entradas: a quantidade de linhas e colunas, nessa ordem, de uma matriz. 
Após isso, solicite que ele digite o valor correspondente a cada posição dessa matriz: 
"Digite o valor para a linha {i} e coluna {j}: ". Ao final, retorne a multiplicação de todos os elementos dessa matriz."""

qnt_linhas = int(input("Digite a quantidade de linhas: "))
qnt_colunas = int(input("Digite a quantidade de colunas: "))

matriz = []
for i in range(0, qnt_linhas):
    aux = []
    for j in range(0, qnt_colunas):
        valor = float(input(f"Digite o valor para a linha {i} e coluna {j}: "))
        aux.append(valor)
    matriz.append(aux)

multp = 1
for i in range(qnt_linhas):
    for j in range(qnt_colunas):
        multp *= matriz[i][j]


print(f"A multiplicação de todos os elementos é: {multp}")