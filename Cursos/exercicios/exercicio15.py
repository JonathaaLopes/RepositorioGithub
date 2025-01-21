#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#importou tudo de matematica mas so usou o trunc TRUNCAR remove a parte fracionária do número
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porcao inteira e {}'.format(num, math.trunc(num)))


#importou somente 1 modulo 
from math import trunc 
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porcao inteira e {}'.format(num, trunc(num)))


#realizou com numero inteiro

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porcao inteira e {}'.format(num, int(num)))
