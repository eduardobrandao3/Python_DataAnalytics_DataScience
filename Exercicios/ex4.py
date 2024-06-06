"""Faça um programa que realize a soma e subtração de duas variáveis, sendo uma do tipo inteiro e outra do tipo decimal, 
exibindo o valor da soma e da subtração no seguinte formato: "O valor da soma é: <soma>" & "O valor da subtração é: <subtracao>''"""

num1 = int(input("Digite um número inteiro: "))
num2 = float(input("Digite um número decimal: "))

soma = num1 + num2 
subt = num1 - num2

print(f"O valor da soma é: {soma:.2f}")
print(f"O valor da subtração é: {subt:.2f}")
