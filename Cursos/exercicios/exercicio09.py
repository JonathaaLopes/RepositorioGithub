#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.40
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))
