"""Faça um programa que peça ao usuário o raio de um círculo e exiba na tela a área e o perímetro desse círculo 
(considere pi = 3.14). Aproxime para 2 casas decimais"""

raio = float(input("Digite o raio do círculo (em cm): "))
area = 3.14 * (raio**2)
perimetro = 2*3.14*raio

print(f"A área do círculo é: {area:.2f} cm²\nO perímetro do círculo é: {perimetro:.2f} cm²")