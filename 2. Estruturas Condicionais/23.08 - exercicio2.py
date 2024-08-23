import os
os.system("cls || clear")


print("""
1 - Pagamento à vista
2 - Pagamento à prazo
     """)

opcao = int(input("Digite a forma de pagamento: "))

match(opcao):
    case 1:
        print("Valor do produto: R$100 ")
        print("Forma de pagamento: À vista ")
        print("Total do desconto: R$10" )
        resultado = 100 - 100 * 0.1
        print(f"Total a pagar: {resultado}")
        print("=== FIM ===")
    case 2:
        resultado = 100
        print("Valor do produto: R$100" )
        print("Forma de pagamento: À prazo ")
        parcela = int(input("Digite o número de parcelas que deseja pagar (até 6): "))
        print(f"Quantidade de parcelas: {parcela}")
        print("=== FIM ===")

        
            
    

