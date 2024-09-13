import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 6
lista_pares_positivos = []

for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero = int(input(f"Digite o {i+1}º número: "))

        if numero % 2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("Número inválido. \nTente novamente.")

for numero in lista_pares_positivos:
    print(numero)


        
