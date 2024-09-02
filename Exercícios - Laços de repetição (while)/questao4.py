"""
Crie um programa que ajude um usuário a controlar 
seus gastos mensais. O programa deve permitir que 
o usuário insira gastos diários até que o total 
gasto no mês exceda um orçamento inicial fornecido. 
O programa deve exibir o total gasto e o valor 
excedente.
"""

import os
os.system("cls || clear")

gasto_total = 0

orcamento = int(input("Digite seu orçamento: "))

while True:
    gasto_diario = int(input("Digite seu gasto diário: "))
    gasto_total = gasto_total + gasto_diario
    
    if gasto_total > orcamento:
        print(f"O gasto é maior que o orçamento.")
    else: 
        print(f"Total: {orcamento - gasto_total}")
