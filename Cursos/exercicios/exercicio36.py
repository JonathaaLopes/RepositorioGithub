# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.




valor_casa = float(int(input('Qual e o valor da casa: R$ ?')))
salario_comprador = float(int(input('Qual e o seu salario: R$ ?')))
anos_pagar = int(input('Em quantos anos quer pagar: ?'))

# calculo da prestacao mensal
prestacao_mensal = valor_casa / anos_pagar * 12

# calculo de 30% do salario
limite_prestacao = salario_comprador * 0.30

# verificacao se o emprestimo pode ser aprovado

if prestacao_mensal <= limite_prestacao:
    print(f"Empréstimo aprovado! A prestação mensal será de R$ {prestacao_mensal:.2f}.")
    
else:
    print(f"Empréstimo negado! A prestação de R$ {prestacao_mensal:.2f} excede 30% do salário.")
    
