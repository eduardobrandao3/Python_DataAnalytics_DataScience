"""Crie um programa que contenha uma função chamada eh_palindromo que verifica se uma palavra é um palíndromo.
 Teste a função com diferentes palavras."""

def eh_palindromo(palavra):
    if(palavra == palavra[::-1]):
        print("É palíndromo")
    else:
        print("NÃO é palíndromo")


print("Digite -1 para sair do programa")
palav = input("Digite uma palavra: ").strip().lower().replace(" ", "")

while palav != '-1':
    eh_palindromo(palav)
    palav = input("Digite uma palavra: ").strip().lower().replace(" ", "")