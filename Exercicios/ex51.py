"""Desenvolva um programa que inclua uma função chamada eh_primo que verifica se um número é primo ou não. 
Solicite ao usuário um número e utilize a função para determinar se é primo."""

def eh_primo(num):
    """
    A funcao 'eh_primo"' verifica se um num eh primo ou nao

    Parametros:
    num: numero inteiro
    """
    if(num < 2):
        print("Não é primo!")
    else:
        divisores = 0
        for i in range(1, num):
            if num % i == 0:
                divisores += 1
        
        if divisores > 1:
            print(f"{num} NÃO é primo")
        else:
            print(f"{num} É primo!")


numero = int(input("Digite um número: "))
eh_primo(numero)