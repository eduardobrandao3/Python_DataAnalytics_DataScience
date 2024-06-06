"""Faça um programa que peça ao usuário para digitar uma frase e retorne a frase ao contrário. 
Exemplo: ele digita "ola, mundo" e o programa retorna "odnum ,alo"."""

frase = input("Digite uma frase: ")

contrario = frase[::-1]

print(f"A frase: '{frase}' ao contrário é: '{contrario}'")