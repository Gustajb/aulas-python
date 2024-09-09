import os
os.system("cls || clear")

soma = 0

# Entrada.

def verificar_media(n1, n2, n3):
   soma = n1 + n2 + n3
   media = soma / 3
   return media

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += 1

# Processamento.
print(f"Média: {media}")

