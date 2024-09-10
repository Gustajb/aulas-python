import os
os.system("cls || clear")

# Entrada. 
lista_notas = []
quantidade_notas = 4

print("\n=== Solicitando dados ===")
for i in range(4):
    nota = float(input("Digite a nota: "))
    lista_notas.append(nota)

# Processamento.
soma = sum(lista_notas)
media = soma / quantidade_notas

if media >= 7:
    situacao = "Aprovado."
elif media >= 5:
    situacao = "Recuperação."
else:
    situacao = "Reprovado."
    
# Saída.
print("\n=== Exibindo resultados ===")
for i, nota in enumerate(lista_notas):
    print(f"{i+1}ª nota: {nota}")

print(f"Média: {media}")
print(f"Resultado: {situacao}")
