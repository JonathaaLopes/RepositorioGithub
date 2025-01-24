#idade de carro

velocidade_carro = int(input('Qual a velocidade do seu carro? '))

limite_velocidade = 80


if velocidade_carro > limite_velocidade:
    excesso = velocidade_carro - limite_velocidade
    valor_multa = excesso * 5

    print(f'voce foi multado voce ultrapassou o limite em {excesso} km/h')
    print(f'o valor da multa e de R$ {valor_multa:.2f}.')
else :
    print('voce nao foi multado')

