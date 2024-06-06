"""Crie uma função chamada divisao_personalizada que recebe dois números como parâmetros. 
Se o segundo número for zero, a função deve gerar uma exceção personalizada chamada DivisaoPorZeroException. 
No programa principal, chame essa função e capture a exceção, exibindo uma mensagem adequada."""

class DivisaoPorZeroException(Exception):
    pass

def divisao_personalizada(n1, n2):
    if n2 == 0:
        raise DivisaoPorZeroException("Você NÃO pode dividir por zero!")
    return n1/n2

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    resultado = divisao_personalizada(n1, n2)
except DivisaoPorZeroException as e:
    print(f"Erro! {e}")
except Exception as e:
    print(f"Houve erro: {e}")
else:
    print(f"O resultado da divisão é: {resultado}")
finally:
    print("FIM DE EXECUÇÃO")