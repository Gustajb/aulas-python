""""
Crie um programa que ajude um estudante a calcular a média
 de suas notas. O programa deve permitir que o usuário
insira notas de provas até que o usuário insira um valor 
negativo. O programa deve calcular e exibir a média das 
notas inseridas.
"""

import os
os.system("cls || clear")

nota = 0

while True:
    nota = float(input("Digite a nota:"))
    if nota < 0:
        print("A nota deve ser maior que 0.")
        break
    else:
        media =+ nota
        print(f"Média: {media}")
     
        
