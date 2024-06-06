"""Faça um programa que peça ao usuário para digitar dois números e mostre na tela o resultado da soma, 
subtração, multiplicação, divisão e resto da divisão desses números"""

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print(f"""{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} x {num2} = {num1 * num2}
{num1} / {num2} = {(num1 / num2):.2f}
{num1} % {num2} = {num1 % num2}""")