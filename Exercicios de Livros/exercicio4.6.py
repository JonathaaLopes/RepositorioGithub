"""Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km. Calcule o preco da passagem, cobrando R$ 0.50 por km para viagens de ate 200km, e R$ 0.45 para viagens mais longas."""


distancia = int(input('Qual a distancia que voce percorrera (em km)? '))

if distancia < 200:
    preco = distancia * 0.50

else:
   preco = distancia * 0.45

print(f'O preco da sua viagem foi de {preco:.2f}')