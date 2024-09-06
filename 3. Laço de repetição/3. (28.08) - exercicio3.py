import os
os.system("cls || clear")

login = "marta"
senha = 12345
contador = 3

while True:
        login = input("Digite seu login: ")
        senha = int(input("Digite sua senha: "))
        
        if login == "marta" and senha == 12345:
           print("Bem-vindo.")
           break
        else:
            print("Login ou senha inválidos.")
            print(f"Tentativa: {contador} \n")
            if contador == 3:
                 break

print("=== FIM ===")

        

                 