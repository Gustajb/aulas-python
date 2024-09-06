import os
os.system("cls || clear")


def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

numero = int(input("Digite seu número: "))
numero = verificar_par_ou_impar(numero)


