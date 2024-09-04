"""
Crie um programa que peça ao usuário para inserir números 
inteiros até que a soma dos números ímpares inseridos seja 
maior que 200. O programa deve exibir o total de números 
ímpares inseridos e a soma desses números. 
"""

import os
os.system("cls || clear")

contador = 0
impares = 0

while impares <= 200:
    numero = int(input("Digite o número: "))

    if numero % 2 != 0:
        impares += numero
        contador += 1
    else:
        break

print(f"Soma dos números {impares}")
print(f"Números ímpares: {contador}")


    