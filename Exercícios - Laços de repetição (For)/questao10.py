"""
Escreva um programa que calcule a soma dos números 
ímpares de 1 a 9 utilizando um laço `for`.
"""
soma = 0
pares = 0
impares = 0

import os
os.system("cls || clear")

for i in range(5):
    numero = int(input("Digite o número ímpar: "))

    if numero % 2 == 0:
        print(f"Esse número é par!")
    else:
        soma = soma + numero
        impares = impares + 1
        print(f"Soma: {soma}")
        
        
    
    