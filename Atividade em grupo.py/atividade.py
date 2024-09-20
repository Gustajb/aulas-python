"""
Gustavo Batista e João Gabriel
"""
import os 
os.system("cls || clear")


lista_de_numeros = []
QUANTIDADE_DE_NUMEROS = 5

for i in range(QUANTIDADE_DE_NUMEROS):
    numero = int(input("Digte o número: "))
    lista_de_numeros.append(numero)

def media (a):
    QTD=len(a)
    soma = sum(a)
    media = soma / QTD
    for numero in a:
        if (numero>=0) or (numero <0):
            media = soma/QTD
            return media
        else:
            return 0

def verificar_pares_e_impares(lista_de_numeros):
    pares = 0
    impares = 0
    lista_par=[]
    lista_impar = []
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            pares += 1
            lista_par.append(numero)
        else:
            impares += 1
            lista_impar.append(numero)
    return pares, lista_par, impares, lista_impar

def verificar_positivos_negativos(lista_de_numeros):
    positivos = 0
    negativos = 0

    for numero in lista_de_numeros:
        if numero > 0:
            positivos += 1
        else:
            negativos +=1
    return positivos, negativos


pares_qtd, lista_par, impar_qtd, lista_impar = verificar_pares_e_impares(lista_de_numeros)
quantidade_positivos, quantidade_negativos = verificar_positivos_negativos(lista_de_numeros)
total = len(lista_de_numeros)

maior=max(lista_de_numeros)
menor = min(lista_de_numeros)
media_par=media(lista_par)
media_imp=media(lista_impar)
media_total=media(lista_de_numeros)
print(f"Quantidade de números: {total}")
print(f"Quantidade de pares: {pares_qtd}")
print(f"Quantidade de ímpares: {impar_qtd}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos ímpares: {media_imp}")
print(f"Média pares: {media_par}")
print(f"Média total: {media_total}")
for i, numero in enumerate(reversed(lista_de_numeros)):
    print(f"{total-i}º número: {numero}")