'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:'''


n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O PRIMEIRO valor e maior')
elif n2 > n1:
    print('O SEGUNDO valor e maior')
else:
    print('Os dois valores sao IGUAIS')