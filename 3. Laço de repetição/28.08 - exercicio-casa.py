import os
os.system("cls || clear")

soma = 0

for i in range (3):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("A nota deve ser maior que 0 e menor ou igual a 10.")
        else:
            soma += nota
            break

media = soma / 3

if media >= 7:
    print("Aprovado.")
elif media >= 5: # else if.
     print("Recuperação.")
else: 
      print("Reprovado.")



