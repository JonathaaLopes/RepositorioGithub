'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_da_casa = float(input('Digite o valor da casa R$: '))
salario_do_comprador = float(input('Digite o salario do comprador R$: '))
quantos_anos_vai_pagar = int(input('Em quantos anos pretende pagar: '))


prestacao_mensal = valor_da_casa / quantos_anos_vai_pagar * 12

limite_prestacao = salario_do_comprador * 0.30

if prestacao_mensal <= limite_prestacao:
    print(f'Seu emprestimo foi aprovado, a prestacao mensal sera de R$ {prestacao_mensal}')

else:
    print(f"Seu emprestimo nao foi aprovado, seu limite de prestacao esta muito alto em R$ {limite_prestacao} excede 30% do salário")