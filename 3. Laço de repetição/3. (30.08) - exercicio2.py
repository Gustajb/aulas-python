import os
os.system("cls || clear")

soma = float = 0
quantidadeNotas = 0

while True:
    print(""""
          \t===MENU===
          S - Inserir uma nota
          P - Ver quantas notas foram inseridas
          N - Calcular média aritmética
          """)
    resposta = input("Deseja inserir uma nota: ").upper()

    match resposta:
        case "S"