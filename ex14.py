"""Faça um programa que leia o peso e a altura de uma pessoa e exiba o índice de massa corporal (IMC) dela. 
A fórmula para calcular o IMC é: IMC = peso/altura², com aproximação em 3 casas decimais."""

peso = float(input("Informe o peso (em kg): "))
altura = float(input("Informe a altura (em m): "))

imc = peso / (altura**2)

print(f"O IMC é: {imc:.3f}")