"""Faça um programa que leia algo digitado pelo usuário, mostre seu tipo e tudo a respeito dele (dica: utiliza as funções is)"""

user = input("Digite algo: ")

print(f"O que você digitou é do tipo {type(user)}")
print(f"É formado apenas por dígitos: {user.isdigit()}")
print(f"É formado apenas por letras do alfabeto: {user.isalpha()}")
print(f"É formado por letras ou dígitos: {user.isalnum()}")
print(f"Está tudo em maiúsculo: {user.isupper()}")
print(f"Está tudo em minúsculo: {user.islower()}")
print(f"É formado apenas por espaços: {user.isspace()}")

