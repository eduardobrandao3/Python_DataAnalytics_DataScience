"""Faça um programa que receba palavras de um usuário até que ele digite "goiabada" e adicione todas essas palavras em uma lista. 
Após isso, retorne uma lista com todas as palavras que não possua vogal (utilize a função filter())."""

def naoVogal(palavras):
    if(('a' or 'e' or 'i' or 'o' or 'u') in palavras):
        return False
    else:
        return True

print("Digite goiabada para parar!")
palavra = input("Digite uma palavra: ").strip().lower().capitalize()
lista = []

while(palavra != 'Goiabada'):
    lista.append(palavra)
    palavra = input("Digite uma palavra: ").strip().capitalize()

resultado = list(filter(naoVogal, lista))

print(resultado)
