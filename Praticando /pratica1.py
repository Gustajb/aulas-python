import os

os.system("cls || clear")

soma = 0

for i in range(5):
    idade = int(input("Digite sua idade: "))
    soma = soma + idade
    print(f"Soma: {soma}")

media = soma / 5
print(f"Média: {media}")



    