"""Faça um programa que leia a temperatura em graus Celsius e exiba a temperatura em graus Fahrenheit.
 A fórmula para converter de Celsius para Fahrenheit é: F = (9/5)*C + 32"""

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (9/5)*celsius + 32

print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")