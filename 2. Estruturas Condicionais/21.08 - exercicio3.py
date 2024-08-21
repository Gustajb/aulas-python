import os
os.system("cls || clear")

resultado = 0

primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
opcao = input("Digite uma opção (+ - * /): ")

match(opcao):
    case "+":
        resultado = primeiro + segundo
    case "-":
        resultado = primeiro - segundo
    case "*":
        resultado = primeiro * segundo
    case "/":
        resultado = primeiro / segundo
    case _:
        print("Opção inválida. ")
   
print(f"Resultado: {resultado}")
print("=== FIM ===")

