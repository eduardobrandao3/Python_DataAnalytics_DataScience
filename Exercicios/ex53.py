"""Desenvolva um programa que inclua uma função chamada conta_caracteres que recebe uma string como parâmetro e 
retorna um dicionário com a contagem de cada caractere"""

def conta_caracteres(texto):
    dicionario = dict()
    for caract in texto:
        aparece = texto.count(caract)
        dicionario[caract] = aparece

    return dict(sorted(dicionario.items(), key=lambda x: x[1], reverse=True))

frase = input("Digite alguma string(texto/frase/palavra/caracter): ").strip()

print(conta_caracteres(frase))