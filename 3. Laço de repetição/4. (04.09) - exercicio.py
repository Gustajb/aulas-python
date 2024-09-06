import os
os.system("cls || clear")

def calcular_media(n1, n2):
    soma = n1 + n2
    resultado = soma / 2
    return resultado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
print(f"Média: {media}")