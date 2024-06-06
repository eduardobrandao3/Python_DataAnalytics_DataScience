"""Faça um programa que receba os seguintes dados de um funcionário: nome, idade e salario. Na empresa que esse funcionário trabalha, 
seu salário é aumentado de ano em ano em R$ 800,90.

Sabendo disso, imprima o nome, idade e salário do funcionário daqui a 1 ano no seguinte formato: 
"O funcionário <nome>, daqui a 1 ano, terá <idade> anos, recebendo um salário igual a R$<salario>."""

nome = str(input("Informe o nome: "))
idade = int(input("Informe a idade: "))
salario = float(input("Informe o salário: R$"))

print(f"O funcionário {nome}, daqui a 1 ano, terá {idade + 1} anos, recebendo um salário igual a R${salario + 800.90:.2f}")
