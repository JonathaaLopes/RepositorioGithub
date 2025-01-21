#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.


nome = str(input('Escreva seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) #em lower case, pode ser em Uppercase tbm