"""Crie um programa que contenha uma função chamada fibonacci que recebe um número como parâmetro e retorna a 
sequência de Fibonacci até o n-ésimo termo"""

def fibonacci(n):
    """
    A funcao fibonacci imprime a sequencia de fibonacci ate o n-ésimo termo
    """
    prim = 1
    segundo = 1
    if(n <= 0):
        print("Digite um número maior que 0(zero), pois é quantidade de termos")
    elif (n == 1):
        print(prim)
    elif (n == 2):
        print(prim)
        print(segundo)
    else:
        print(prim)
        print(segundo)
        for cont in range(3, n+1, 1):
            prox = prim + segundo
            print(prox)
            prim = segundo
            segundo = prox


termos = int(input("Digite a quantidade de termos que quer da sequencia de Fibonacci: "))
fibonacci(termos)