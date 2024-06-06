"""Faça um programa que solicite ao usuário digitar uma frase e conte quantas vogais existem na frase utilizando um loop "for"."""

frase = input("Digite uma frase: ").lower().strip()

qnt_vogais = 0

for carac in frase:
    if(carac == 'a' or carac == 'e' or carac == 'i' or carac == 'o' or carac == 'u'):
        qnt_vogais += 1
    
print(f"A frase digitada possui {qnt_vogais} vogais")