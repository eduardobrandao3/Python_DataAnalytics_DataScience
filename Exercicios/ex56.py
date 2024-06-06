"""Crie um programa que contenha uma função chamada fatorial que recebe um número como parâmetro e retorna o fatorial desse número."""

def fatorial(num):
    """
    A funcao 'fatorial' retorna o fatorial desse numero, ou seja, num.(num-1).(num-2). ... .1

    Parâmetros:
    num: número inteiro
    """
    if ((num == 0) or (num == 1)):
        return 1
    else:
        fat = 1
        for n in range(num, 1, -1):
            fat *= n

        return fat

numero = int(input("Digite um número: "))
if(numero < 0):
    print("Não existe fatorial de número negativo")
else:
    print(f"O fatorial de {numero} é: {fatorial(numero)}")