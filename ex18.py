"""Escreva um programa Python que leia o valor de dois catetos e retorne o valor da hipotenusa, 
assumindo que seja possível formar um triângulo"""

c1 = float(input("Informe o valor do primeiro cateto: "))
c2 = float(input("Informe o valor do segundo cateto: "))

hip = ((c1**2) + (c2**2))**(1/2)

print(f"A hipotenusa vale: {hip:.2f}")