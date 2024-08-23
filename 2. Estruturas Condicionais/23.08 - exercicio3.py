import os
os.system("cls || clear")

sexo = input("Digite seu sexo (M ou F): ").upper()
altura = float(input("Digite sua altura: "))

match sexo:
    case "M":
        peso_ideal = ((72.7 * altura) - 58)
    case "F":
        peso_ideal = ((62.1 * altura) - 44.7)
    case _:
        print("Opção inválida.")

print(f"Altura: {altura}")
print(f"Peso ideal: {peso_ideal:.2f}")

