import os
os.system("cls || clear")

# Entrada. 
lista_numeros = []
quantidade_numeros = 5

for i in range(quantidade_numeros):
    numero = int(input(f"Digte o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

# Saída.
print("\n=== Exibindo Resultados ===")
for i, numero in enumerate(lista_numeros):
    print(f"{i+1}º número: {numero}")

print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
