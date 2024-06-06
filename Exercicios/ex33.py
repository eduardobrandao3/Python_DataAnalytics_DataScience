"""Faça um programa que receba a temperatura em graus Celsius e converta para Fahrenheit ou vice-versa,
 de acordo com a escolha do usuário."""

temp = float(input("Digite a temperatura: "))
unidade = input("A temperatura está em Celsius (C) ou em Fahrenheit (F)? [C/F]: ").upper().strip()[0]

if (unidade == 'F'):
    conversao = (temp - 32)*(5/9)
    print(f"{temp}°F equivale a {conversao:.2f}°C")
elif(unidade == 'C'):
    conversao = (9/5)*temp + 32
    print(f"{temp}°C equivale a {conversao:.2f}°F")
else:
    print("Unidade de medida inválida")