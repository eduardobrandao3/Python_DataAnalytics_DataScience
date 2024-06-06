"""Faça um programa que verifique se uma frase digitada pelo usuário é um palíndromo
 (se pode ser lida da mesma forma de trás para frente).
Imprima "É um palíndromo!" caso seja e "Não é um palíndromo!" caso não seja."""

frase = input("Digite uma palavra: ").lower().strip().replace(" ", "")

if (frase == frase[::-1]):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")