import os
os.system("cls || clear")

lista_numeros = []
quantidade_de_numeros = 5
numero_vetorizado = []

print("=== Solicitando dados. ===")
for i in range(quantidade_de_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero < 0:
        numero = 0

    lista_numeros.append(numero)

print(f"=== Exiibindo dados ===")
for i, numero in enumerate(lista_numeros):
    print(f"{i+1}º número: {numero}")




    










