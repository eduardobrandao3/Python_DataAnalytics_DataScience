"""Faça um programa que calcule a média de três notas e exiba a situação do aluno 
(aprovado - maior ou igual a 70 -, em recuperação - entre 60 e 70 - ou reprovado - menor que 60)."""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3
print(f"Média: {media}")

if (media >= 70):
    print("APROVADO")
elif (media >= 60):
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
    