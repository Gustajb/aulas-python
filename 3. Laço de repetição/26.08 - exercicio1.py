import os
import time

os.system("cls || clear")

pares = 0
impares = 0
soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma = soma + numero
    print(f"Soma: {soma}")

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")


