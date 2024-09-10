import os
os.system("cls || clear")

# Entrada. 
notas = []

for i in range(3):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

for i, nota in enumerate(notas):
    print(f"{i+1}ª nota: {nota}") 

