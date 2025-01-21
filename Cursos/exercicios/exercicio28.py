#Condicoes*
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar
if jogador == computador:
    print('Parabens! voce conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no numero {} e nao no {}!'.format(computador, jogador))
    