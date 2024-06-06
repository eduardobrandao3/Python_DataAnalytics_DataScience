"""Faça um um programa que receba uma frase como entrada e conte quantas vezes uma determinada palavra aparece na frase."""

frase = input("Digite uma frase: ").strip().lower()
palavra = input("Digite a palavra que você quer contar: ").strip().lower()
qnt_palav = frase.count(palavra)

print(f"A palavra '{palavra}' aparece {qnt_palav} vezes na frase '{frase}'")