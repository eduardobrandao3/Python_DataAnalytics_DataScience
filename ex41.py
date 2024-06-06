"""Faça um programa que solicite ao usuário digitar um número e, em seguida, calcule e imprima o fatorial desse número."""

num = int(input("Digite um número para calcular o fatorial: "))

if (num == 0):
    print("0! = 1")
elif (num == 1):
    print("1! = 1")
elif (num < 0):
    print("Não tem como calcular o fatorial de número negativo")
else:
    fatorial = 1
    for multp in range(num, 1, -1):
        fatorial *= multp
    print(f"{num}! = {fatorial}")