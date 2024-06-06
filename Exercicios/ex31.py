"""Faça um programa que receba o salário de um funcionário e calcule o valor do seu aumento de acordo com as seguintes condições: 
salários até R$ 1.000, aumento de 20%; 
salários entre R$ 1.000 e R$ 3.000, aumento de 15%; 
salários acima de R$ 3.000, aumento de 10%."""

salario = float(input("Digite o salário: R$"))

if(salario  < 1000):
    print(f"Aumento de 20%. Novo salário = R${salario*1.2:,.2f}")
elif(salario <= 3000):
    print(f"Aumento de 15%. Novo salário = R${salario*1.15:,.2f}")
else:
    print(f"Aumento de 10%. Novo salário = R${salario*1.1:,.2f}")