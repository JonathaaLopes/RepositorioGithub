#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.



while True:
    print('-' * 40)
    print(f'{"TABUADA":^40}')  # Centraliza o título
    print('-' * 40)
    
    # Solicita o número para calcular a tabuada
    num = int(input('\nQual tabuada você quer ver? '))
    
    # Verifica se o número é negativo para interromper
    if num < 0:
        print('\nPrograma encerrado. Número negativo digitado!')
        break
    
    # Mostra a tabuada do número
    print(f'\nTabuada do {num}:')
    print('-' * 15)
    
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')
    
    print('-' * 15)
    
print('\nVolte sempre!')


#Guanabara

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('_' * 30)
print('Programa tabuada encerrado. VOlte sempre!')