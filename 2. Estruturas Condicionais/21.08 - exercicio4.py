import os
os.system("cls || clear")

print("""
1 - Picanha
2 - Lasanha
3 - Strogonoff
4 - Bife acebolado
5 - Pão com ovo
           """)

opcao = int(input("Digite o número do prato desejado: "))

match(opcao):
    case 1:
        resultado = "Picanha - R$ 25,00"
    case 2:
        resultado = "Lasanha - R$ 20,00"
    case 3:
        resultado = "Strogonoff - R$ 18,00"
    case 4:
        resultado = "Bife acebolado - R$ 15,00"
    case 5:
        resultado = "Pão com ovo - R$ 5,00"
    case _:
        print("Opção inválida.")

print(f"{resultado}")

    