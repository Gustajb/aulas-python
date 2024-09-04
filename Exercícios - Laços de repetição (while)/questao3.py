"""
Escreva um programa que multiplique um número 
inicial por um fator dado pelo usuário até que o 
produto exceda 100. Exiba o produto final e o 
número de multiplicações realizadas.
"""

import os
os.system("cls || clear")

contador = 0
numero = int(input("Digite um número: "))
soma = 0

while True:
    fator = int(input("Digite o fator: "))
    produto = fator * numero
    soma += produto
    if produto < 100:
        print(f"Produto: {produto}")
        print(f"Soma dos produtos: {soma}")
        contador += 1
        if soma >= 100:
            print(f"Produto ultrapassou 100. ")
            break
print(f"Número de multiplicações: {contador}")
