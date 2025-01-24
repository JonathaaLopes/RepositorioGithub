#escreva um programa que leia a quantidade de dias, horas,minutos e segundos do usuario. Calcule o total em segundos.

dias = int(input('Digite o numero de dias: '))
horas = int(input('Digite o numero de horas: '))
minutos = int(input('Digite a quantidade de minutos:'))
segundos = int(input('Digite a quantidade de segundos:'))

total_de_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos

print(f'o total de segundos e {total_de_segundos}')