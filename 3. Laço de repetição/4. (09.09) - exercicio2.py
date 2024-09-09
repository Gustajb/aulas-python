import os
os.system("cls || clear")

def verificar_idade(nascimento):
    return 2024 - nascimento
    
# Entrada.
nascimento = int(input("Digite o ano em que você nasceu: "))

# Processamento.
idade = verificar_idade(nascimento)

# Saída.
print("=== RESULTADO ===")
print(f"Idade: {idade}")

