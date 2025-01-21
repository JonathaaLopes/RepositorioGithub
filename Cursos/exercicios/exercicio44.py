'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

 à vista dinheiro/cheque: 10% de desconto

 à vista no cartão: 5% de desconto

 em até 2x no cartão: preço formal 

 3x ou mais no cartão: 20% de juros'''


# Entrada de dados

preco = float(input("Digite o preço do produto: R$ "))

print('''
Escolha a condição de pagamento:
[1] À vista no dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)
''')

opcao = int(input("Digite a opção de pagamento: "))

# Condições de pagamento

if opcao == 1:
    valor_final = preco * 0.90
    print(f"Pagamento à vista no dinheiro/cheque. Valor com 10% de desconto: R$ {valor_final:.2f}")
    
elif opcao == 2:
    valor_final = preco * 0.95
    print(f"Pagamento à vista no cartão. Valor com 5% de desconto: R$ {valor_final:.2f}")
    
elif opcao == 3:
    valor_final = preco
    print(f"Pagamento em até 2x no cartão. Valor total: R$ {valor_final:.2f}")
    
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    if parcelas >= 3:
        valor_final = preco * 1.20
        valor_parcela = valor_final / parcelas
        print(f"Pagamento em {parcelas}x no cartão. Valor total com 20% de juros: R$ {valor_final:.2f}")
        print(f"Cada parcela será de: R$ {valor_parcela:.2f}")
        
    else:
        print("Número de parcelas inválido para essa opção.")
else:
    print("Opção inválida. Tente novamente.")


