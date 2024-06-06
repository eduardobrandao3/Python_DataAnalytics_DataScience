"""Crie uma função que recebe dois números como parâmetros e realiza a divisão. No programa principal, 
chame essa função e utilize um bloco try e except para capturar exceções. No bloco except, 
inclua uma cláusula para lidar com exceções de divisão por zero e outra cláusula para capturar qualquer outra exceção. 
Exiba mensagens adequadas para cada situação."""

def divide(a, b):
    return a/b

try:
    n1 = int(input("Digite o dividendo: "))
    n2 = int(input("Digite o divisor: "))
    resultado = divide(n1, n2)
except ZeroDivisionError as e:
    print("ERRO! Você não pode dividir por zero")
except Exception as e:
    print(f"HOUVE ERRO! {e}")
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Fim de execução!")