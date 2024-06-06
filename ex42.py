"""Faça um programa que solicite ao usuário digitar um número e, em seguida, imprima a sequência de Fibonacci até esse número."""

qnt = int(input("Digite quantos itens da sequencia de Fibonacci deseja ver: "))

while qnt <= 0:
    qnt = int(input("Digite um número maior que 0(zero): "))

if(qnt == 1):
    print(1)
elif(qnt == 2):
    print(1)
    print(1)
else:
    print (1)
    print (1)
    primeiro = 1
    segundo = 1
    prox = primeiro + segundo
    for cont in range(3, qnt+1, 1):
        print(prox)
        primeiro = segundo
        segundo = prox
        prox = primeiro + segundo