#Crie um programa que leia um número
#inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} e PAR'.format(numero))
else:
    print('O numero {} e IMPAR'.format(numero))