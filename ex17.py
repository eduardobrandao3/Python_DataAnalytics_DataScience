"""Escreva um programa Python que leia um número e retorne seu quadrado, sua raíz quadrada e sua raíz cúbica,
 com aproximação em 2 casas decimais."""

num = float(input("Digite um número: "))

print(f"O quadrado do número é: {num**2:.2f}\nA raiz quadrada é: {num**(1/2):.2f}\nA raiz cúbica é: {num**(1/3):.2f}")