import os
os.system("cls || clear")

def inflacionar(preco_produto):
    if preco_produto < 100:
        return preco_produto * 1.1
    else:
        return preco_produto * 1.2
# Entrada 
preco_produto = float(input("Digite o preço de um produto: "))

# Processamento.
preco_inflacionado = inflacionar(preco_produto)

print(f"\n=== RESULTADO ===")
print(f"Preço inflacionado {preco_inflacionado:.2f}")
