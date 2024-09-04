"""
 Crie um programa para ajudar o usuário a acompanhar suas 
 metas de estudo. O usuário define uma meta de horas de 
 estudo e o programa deve permitir que o usuário insira o 
 número de horas estudadas até que o total atinja ou exceda
a meta. O programa deve  exibir o total de horas estudadas 
e o valor excedente.
"""

import os
os.system("cls || clear")

total_horas = 0

meta_de_horas = int(input("Digite a meta de horas de estudo: "))
while True:
    horas_estudadas = int(input("Digite as horas estudadas:"))
    total_horas = total_horas + horas_estudadas

    if total_horas >= meta_de_horas:
        print("As horas foram excedidas.")
        break
    else:
        print(f"Horas que faltam: {meta_de_horas - horas_estudadas}")
    

