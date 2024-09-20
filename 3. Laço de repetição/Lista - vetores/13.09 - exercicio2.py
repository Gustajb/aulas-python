import os
os.system("cls || clear")
import time

QUANTIDADE_NUMEROS = 6
lista_pares_positivos = []

def solicitar_numeros():
    for i in range(QUANTIDADE_NUMEROS):
        while True:
            numero = int(input(f"Digite o {i+1}º número: "))

            if numero % 2 == 0 and numero > 0:
                lista_pares_positivos.append(numero)
                break
            else:
                print("Número inválido. \nTente novamente.")
    
    return lista_pares_positivos
lista_numeros = solicitar_numeros()

for i, numero in enumerate(reversed(lista_numeros)):
        print(f"{len(lista_numeros) - i}º - {numero}")
        time.sleep(2)

        
