"""
Escreva um programa que multiplique um número 
inicial por um fator dado pelo usuário até que o 
produto exceda 100. Exiba o produto final e o 
número de multiplicações realizadas.
"""

import os
os.system("cls || clear")

numero = int(input("Digite um número: "))
produto = 5 * numero

while produto <= 100:
    print(f"Produto: {produto}")
    break
