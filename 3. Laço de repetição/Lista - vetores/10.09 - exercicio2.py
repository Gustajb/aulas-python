import os
os.system("cls || clear")

# Entrada. 
lista_notas = []
quantidade_notas = 3

print("\n=== Solicitando dados ===")
for i in range(quantidade_notas):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Processamento.
soma = sum(lista_notas)
media = soma / quantidade_notas

# Saída.
print("\n=== Exibindo resultados ===")
for i, nota in enumerate(lista_notas):
    print(f"{i+1}ª nota: {nota}")
print(f"Média: {media}")

