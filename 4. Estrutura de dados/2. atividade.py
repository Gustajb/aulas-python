import os
from dataclasses import dataclass
os.system("cls || clear")


# Estrutura de dados.
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_DE_CLIENTES = 4

lista_de_clientes = []

for i in range(QUANTIDADE_DE_CLIENTES):
    cliente = Cliente(
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    lista_de_clientes.append(cliente)

print("=== Exibindo dados do cliente ===")
for cliente in lista_de_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Sobrenome: {cliente.sobrenome}")
    print(f"Idade: {cliente.idade}")
    print(f"Peso: {cliente.peso}")
    print(f"Altura: {cliente.altura}")

nome_do_arquivo = "carteira_de_clientes.txt"
with open(nome_do_arquivo, "a") as arquivo_clientes:
    for cliente in lista_de_clientes:
        arquivo_clientes.write(f"{aluno.nome}, {aluno.sobrenome}, {aluno.idade}, {aluno.peso}, {aluno.altura})




# Salvar em um arquivo chamado: carteira_de_clientes.txt

# Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal.