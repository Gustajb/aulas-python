"""
Crie um programa que solicite ao usuário criar uma senha. 
O programa deve então pedir para confirmar a senha e 
garantir que ambas as senhas coincidam. Se as senhas não 
coincidirem, o programa deve continuar pedindo para o 
usuário inserir e confirmar a  tenha até que ambas sejam 
iguais.
"""

import os
os.system("cls |\ clear")

senha1 = 0
senha2 = 0

while True:
    senha1 = input("Crie uma senha: ")
    senha2 = input("Confirme a senha: ")
    if senha1 == senha2:
        print("Senha criada com sucesso!")
        break
    else:
        print("As senhas não coincidem.")
        

