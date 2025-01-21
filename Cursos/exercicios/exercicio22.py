#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Escreva seu nome: ')).strip() #.strip remove os espacos dos lados dos nomes digitados pois espacos contam no python
print('Analisando seu nome...')
print('Seu nome em maiusculo e {}'.format(nome.upper()))
print('Seu nome em minusculas e {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
