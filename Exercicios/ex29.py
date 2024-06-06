"""Faça um programa que calcule o IMC (Índice de Massa Corporal) e exiba a categoria correspondente 
(abaixo do peso, peso normal, sobrepeso, obesidade grau I, obesidade grau II ou obesidade grau III)."""

peso = float(input("Digite o peso (em kg): "))
altura = int(input("Digite a altura (em cm): "))  #pegando em cm para não ter perigo de colocar , no lugar do . (float)

alt_m = altura / 100

imc = peso/(alt_m**2)

print(f"O IMC é: {imc:.2f}")

if (imc >= 40):
    print("Obesidade classe III")
elif (imc >= 35):
    print("Obesidade classe II")
elif (imc >= 30):
    print("Obesidade classe I")
elif (imc >= 25):
    print("Excesso de peso")
elif (imc >= 18.5):
    print("Peso normal")
else:
    print("Abaixo do peso normal")