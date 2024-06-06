"""Crie um programa que solicite ao usuário que insira um número inteiro. Utilize tratamento de exceções para garantir que o programa 
não quebre se o usuário inserir algo que não seja um número. Se ocorrer uma exceção, 
imprima uma mensagem informando que houve um erro."""

try:
    num = int(input("Digite um número: "))
except ValueError as e:
    print("ERRO! Você precisa digitar um número!")
    print(e)
else:
    print(f"O número digitado foi: {num}")
finally:
    print("Fim de execução!")