'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
nascimento = int(input('ano de nascimento? '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('voce tem que se alistar IMEDIATAMENTO!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {}anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter se alistado ha {} anos.'.format(saldo))

###     com f string    ###

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento? '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
