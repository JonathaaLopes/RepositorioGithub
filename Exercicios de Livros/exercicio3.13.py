#Escreva um programa que converta uma temperatura digitada em °C em °F. A formula para essa conversao  e:


#°F = 9 x c / 5 + 32



temperatura_Celsius = float(input('Digite a temperatura em Celsius: °C '))

Temperatura_convertida = (temperatura_Celsius * 9/5) + 15

print(f'a temperatura em °C foi de {temperatura_Celsius} esta temperatura em °F e de {Temperatura_convertida}')