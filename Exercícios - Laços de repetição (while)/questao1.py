"""
 Desenvolva um programa que conte quantos números 
 negativos foram inseridos pelo usuário usando um 
 laço while. O programa deve parar quando o usuário 
 inserir 0 ou um número positivo. Mostre a 
 quantidade de números negativos.
"""

import os
os.system("cls || clear")

contador = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        contador +=1
        break

print(f"{contador} números negativos.")




