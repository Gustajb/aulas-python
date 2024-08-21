import os
os.system("cls || clear")

print("""
1 - Domingo
2 - Segunda-feira
3 - Terça-feira
4 - Quarta-feira
5 - Quinta-feira
6 - Sexta-feira
7 - Sábado
      """)

resultado = 0

opcao = int(input("Digite o número que representa o dia da semana: "))

match(opcao):
    case 1:
        resultado = "Domingo (final de semana)"
    case 2:
        resultado = "Segunda-feira (dia útil)"
    case 3:
        resultado = "Terça-feira (dia útil)"
    case 4:
        resultado = "Quarta-feira (dia útil)"
    case 5:
        resultado = "Quinta-feira (dia útil)"
    case 6:
        resultado = "Sexta-feira (dia útil)"
    case 7:
        resultado = "Sábado (final de semana)"
    case _:
        print(f"Opção inválida.")

print(f"{resultado}")
    

