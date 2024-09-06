import os
os.system("cls || clear")

def tabuada(n1, n2):
    calculo = n1 * n2
    resultado = print(f"{n1} x {n2} = {calculo}")
    return calculo

numero = int(input("Digite o número: "))

for i in range(1,11):
    
    resultado = tabuada(numero, i)