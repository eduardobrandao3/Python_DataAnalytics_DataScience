"""Faça um programa que solicite ao usuário digitar uma palavra e verifique se a palavra é um palíndromo utilizando um loop "for"."""

palavra = input("Digite uma palavra: ").lower().strip().replace(" ", "")


aux = len(palavra) - 1
iguais = 0

for i in range(0, len(palavra), 1):
    if(palavra[i] == palavra[aux]):
        iguais += 1
    aux -= 1

if(iguais == len(palavra)):
    print("É palíndromo")
else:
    print("Não é palíndromo")