'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:'''

from datetime import date
atual = date.today().year

nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade}')

if idade <= 9:
    print('Classificacao: MIRIN')
elif idade <= 19:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificacao: JUNIOR')
elif idade <= 25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')