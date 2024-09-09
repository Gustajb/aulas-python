import os
os.system("cls || clear") 

def notas(nota1, nota2):
    calculo = (nota1 + nota2) / 2 
    return calculo

def verificar_resultado(media):
    if media >= 7:
        return ("Aprovado.")
    else:
        return ("Reprovado.")
    
# Entrada.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento.
media = notas(nota1, nota2)
resultado = verificar_resultado(media)

# Saída.
print(f"=== RESULTADO ===")
print(f"Média: {media}")
print(f"Resultado: {resultado}")