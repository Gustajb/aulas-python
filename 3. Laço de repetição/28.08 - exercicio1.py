import os
os.system("cls || clear")

nota = float(input("Digite uma nota: "))

while nota < 0 or nota > 10:
    print("A nota deve ser maior que 0 e menor ou igual a 10.")

    nota = float(input("Digite a nota: "))

print(f"Nota {nota}")
