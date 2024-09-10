import os
os.system("cls || clear")

# Entrada. 
lista_numeros = []
quantidade_numeros = 10
negativos = 0
positivos = 0
soma_positivos = 0

print("\n=== Solicitando dados ===")
for i in range(quantidade_numeros):
    numero = int(input(f"Digte o {i+1}º número: "))
    lista_numeros.append(numero)
    
# Processamento.
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
        soma_positivos += numero


# Saída.
print("\n=== Exibindo Resultados ===")
for i, numero in enumerate(lista_numeros):
    print(f"{i+1}º número: {numero}")

print(f"\nNegativos: {negativos}")
print(f"Positivos: {positivos}")
print(f"Soma dos números positivos: {soma_positivos}")