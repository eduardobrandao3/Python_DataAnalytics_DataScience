"""Desenvolva um programa que inclua uma função chamada media_ponderada que calcula a média ponderada de três notas, 
sendo os pesos 2, 3 e 5, respectivamente."""

def media_ponderada (nota1, nota2, nota3):
    p1 = 2
    p2 = 3
    p3 = 5
    return (nota1*p1 + nota2*p2 + nota3*p3)/(p1 + p2 + p3)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

print(f"A média ponderada entre as 3 notas é: {media_ponderada(n1, n2, n3)}")