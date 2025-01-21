#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

vitorias = 0

while True:
    # Jogador escolhe um número
    jogador = int(input('Digite um número: '))
    
    # Computador escolhe um número aleatório entre 0 e 10
    computador = randint(0, 10)
    
    # Soma dos números
    total = jogador + computador
    
    # Jogador escolhe par ou ímpar
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}.')
    print(f'Total: {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)
    
    # Verifica quem ganhou
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
            
    print('Vamos jogar novamente...')
    print('=-' * 15)

print('=-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')