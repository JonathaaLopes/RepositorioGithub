'''
Escreva um programa que calcule o preco a pagar pelo fornecimento de energia eletrica. Pergunte a quantidade de kWh consumida e o tipo de instalacao: R para residencias, I para industrias e C para comercios. Calcule o preco a pagar de acordo com a tabela a seguir.

'''
print('\n')
print('Preco por tipo e faixa de consumo')
print('\n')
print('=-' * 20)
print('\n')
print('Tipo           Faixa (kWh)       Preco  ')
print('Residencial    Ate 500           R$ 0.40')
print('Residencial    Acima de 500      R$ 0.65')
print('Comercial      Ate 1000          R$ 0.55')
print('Comercial      Acima 1000        R$ 0.60')
print('Industrial     Ate 5000          R$ 0.55')
print('Industrial     Acima de 5000     R$ 0.60')

while True:
    try:
        consumo = float(input('Digite a qualtidade em kHw consumida: '))
        tipo = (input('Digite o tipo de instalacao (R para Residencial, C Comercio, e I Industrias)')).strip().upper()

        if tipo not in ['R', 'C', 'I']:
            print('Tipo de instalacao invalida. Use R, C ou I')
        else:
            if tipo == 'R':  # Residencial
                if consumo <= 500:
                    preco = consumo * 0.40
                else:
                    preco = consumo * 0.65
            elif tipo == 'C':  # Comercial
                if consumo <= 1000:
                  preco = consumo * 0.55
                else:
                    preco = consumo * 0.60
            elif tipo == 'I':  # Industrial
                if consumo <= 5000:
                    preco = consumo * 0.55
                else:
                    preco = consumo * 0.60            
            
            print(f'\nValor a pagar: R$ {preco:.2f}')
            break
    except ValueError:
        print('Por favor digite um numero valido para o consumo')