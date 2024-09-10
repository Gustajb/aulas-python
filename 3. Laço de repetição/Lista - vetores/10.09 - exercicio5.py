import os
os.system("cls || clear")

# Entrada. 
lista_numeros = []
quantidade_numeros = 6
impares = 0
pares = 0

print("\n=== Solicitando dados ===")
for i in range(quantidade_numeros):
    numero = int(input(f"Digte o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Saída.
print("\n=== Exibindo Resultados ===")
for i, numero in enumerate(lista_numeros):
    print(f"{i+1}º número: {numero}")

print(f"\nPares: {pares}")
print(f"Ímpares: {impares}")
