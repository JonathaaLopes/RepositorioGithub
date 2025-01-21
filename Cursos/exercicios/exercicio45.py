'''Crie um programa que faça o computador jogar Jokenpô com você.'''


from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura     
''')
jogador = int(input('Qual e a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada invalida!')
        
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada invalida!')
        
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida!')