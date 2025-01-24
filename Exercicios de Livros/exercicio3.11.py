#Faca um programa que solicite o preco de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preco a pagar.

mercadoria = float(input('Digite o preco da mercadoria: R$ '))
percentual_desconto = float(input('Digite o percentual de desconto ex: 5%, 10%: '))

valor_desconto = mercadoria * (percentual_desconto / 100)

preco_atualizado = mercadoria - valor_desconto

print(f'o preco da mercadoria e de {mercadoria} e foi dado {percentual_desconto}% de desconto e ficou por {preco_atualizado}')