"""Faça um programa que imprima os números de 1 a 100, mas substitua os múltiplos de 3 pela palavra "Fizz", 
os múltiplos de 5 pela palavra "Buzz" e os múltiplos de 3 e 5 pela palavra "Fizz Buzz"."""

for cont in range(1, 101, 1):
    if(cont % 3 == 0 and cont % 5 != 0):    
        print("Fizz")
    elif (cont % 5 == 0 and cont % 3 != 0):
        print("Buzz")
    elif (cont % 3 == 0 and cont % 5 == 0):
        print("Fizz Buzz")
    else:
        print(cont)