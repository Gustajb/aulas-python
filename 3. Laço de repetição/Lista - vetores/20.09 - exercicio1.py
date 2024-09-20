import os
os.system("cls || clear")

QUANTIDADE_DE_NUMEROS = 5 
pares_positivos = 0
impares = 0
negativos = 0
total_numeros = 0

print("=== Solicitando dados ===")
while True: 
    numero = int(input(f"Digite o número: "))

    if numero == 0:
        break
    
    if numero % 2 == 0 and numero > 0:
        pares_positivos += 1
    else: 
        impares += 1

    if numero < 0:
        negativos += 1
    total_numeros += 1

print("\n=== Exibindo resultados ===")
print(f"Quantidade de pares positivos: {pares_positivos}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de números inseridos: {total_numeros}")


        




