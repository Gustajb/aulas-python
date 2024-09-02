"""
Escreva um programa que use um laço while para 
encontrar o primeiro número maior que 50 que seja 
divisível por 7. Exiba esse número.
"""

import os
os.system("cls || clear")

while True:
    numero = int(input("Digite um número: "))
    if numero <50:
        break
    elif numero % 7 == 0:
        print(f"{numero} é divisível por 7")