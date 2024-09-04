"""
Crie um programa que permita ao usuário registrar o número 
de calorias consumidas em cada refeição. O programa deve 
continuar registrando as calorias até que o total de 
calorias consumidas ultrapasse 2000 calorias. Após exceder 
2000 calorias, exiba o total de calorias consumidas e o 
excesso.
"""

import os
os.system("cls || clear")

total_calorias = 2000
soma_calorias = 0
while True:
    calorias_consumidas = int(input("Digite a quantidade de calorias: "))
    soma_calorias = soma_calorias + calorias_consumidas
    if soma_calorias >= 2000:
        print("Calorias excedidas")
        break
    else:
        print(f"Calorias que faltam: {total_calorias - soma_calorias}")
    
    


