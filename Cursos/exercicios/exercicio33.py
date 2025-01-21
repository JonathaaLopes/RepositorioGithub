# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#verificando quem e o menor

menor = a #ja diminuindo um if, ja informando que o a e menor.
if b < a and c < c:
    menor = b
if c < a and c < b:
     menor = c
     
#verificando que e o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))