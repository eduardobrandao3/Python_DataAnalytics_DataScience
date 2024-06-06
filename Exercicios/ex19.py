"""Faça um programa que receba uma frase do usuário e retorne: (i) a quantidade de caracteres da frase (ii)
a quantidade de letras 'e' na frase (iii) o índice da primeira substring 'ou' (iv) a frase toda maiúscula (v) a frase toda minúscula."""

frase = input("Digite uma frase: ")

qnt_caracteres = len(frase)
qnt_e = frase.count('e')
indice_ou = frase.find('ou')
maiu = frase.upper()
minu = frase.lower()

print(f"""Quantidade de caracteres: {qnt_caracteres}
Quantidade de letras 'e': {qnt_e}
Índice da primeira substring 'ou': {indice_ou}
Frase toda maiúscula: {maiu}
Frase toda minúscula: {minu}""")