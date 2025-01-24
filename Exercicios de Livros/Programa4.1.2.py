# Loop para garantir que o usuário insira um plano válido
while True:
    plano = str(input('Qual é seu plano de celular (falopouco ou falomuito): ')).lower()

    if plano == 'falopouco':
        minutos_do_plano = 100
        extra = 0.20
        mensalidade = 50
        break  # Sai do loop quando o plano é válido
    elif plano == 'falomuito':
        minutos_do_plano = 500
        extra = 0.15
        mensalidade = 99
        break  # Sai do loop quando o plano é válido
    else:
        print('Plano inválido. Digite novamente.')

# Solicita o número de minutos consumidos
while True:
    try:
        minutos_consumidos = int(input('Quantos minutos você consumiu? '))
        if minutos_consumidos < 0:
            print('O número de minutos não pode ser negativo. Tente novamente.')
        else:
            break  # Sai do loop quando o valor é válido
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

# Calcula o suplemento, caso ultrapasse o limite do plano
suplemento = 0
if minutos_consumidos > minutos_do_plano:
    suplemento = extra * (minutos_consumidos - minutos_do_plano)

# Calcula o total a ser pago
total = mensalidade + suplemento

# Exibe os resultados detalhados
print(f'\nPlano escolhido: {plano.capitalize()}')
print(f'Mensalidade: R${mensalidade:.2f}')
print(f'Suplemento por minutos extras: R${suplemento:.2f}')
print(f'Total a pagar: R${total:.2f}')