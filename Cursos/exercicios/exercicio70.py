'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

'''



total_gasto = 0
produtos_mais_1000 = 0
nome_mais_barato = ''
preco_mais_barato = float('inf')  # Começamos com infinito para garantir que qualquer preço será menor

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    
    # Calculando o total gasto
    total_gasto += preco
    
    # Verificando produtos que custam mais de R$1000
    if preco > 1000:
        produtos_mais_1000 += 1
    
    # Verificando se é o produto mais barato
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome
    
    # Perguntando se quer continuar
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('-' * 40)
print(f'O total gasto na compra foi R${total_gasto:.2f}')
print(f'Temos {produtos_mais_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${preco_mais_barato:.2f}')