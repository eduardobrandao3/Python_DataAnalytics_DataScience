"""Crie um programa que contenha uma função chamada potencia que recebe dois números como parâmetros e 
retorna o resultado da potenciação do primeiro pelo segundo. Utilize expressões lambda."""

potencia = lambda num1, num2: num1**num2
#a funcao potencia calcula o num1 elevado ao num2

numero1 = float(input("Informe a base: "))
numero2 = float(input("Informe o expoente: "))

print(f"{numero1} elevado {numero2} = {potencia(numero1, numero2)}")