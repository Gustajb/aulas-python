import os
os.system("cls || clear")

# Função com retorno.
def somar(n1, n2):
    soma = n1 + n2
    return soma

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite a sua segunda nota: "))

soma = somar(primeiro_numero, segundo_numero)

print(f"Soma: {soma}")