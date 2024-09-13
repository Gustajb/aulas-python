import os
os.system("cls || clear")

palavras = "python", "senai", "usuário", "programação"

maior_palavra = palavras [0]
menor_palavra = palavras [0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    else: 
        if len(palavra) < len(menor_palavra):
            menor_palavra = palavra 

print(f"Menor palavra: {menor_palavra}")
print(f"Maior palavra: {maior_palavra}")
