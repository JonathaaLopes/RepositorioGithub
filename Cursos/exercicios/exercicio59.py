'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar      
    [3] maior
    [4] novos numeros     
    [5] sair do programa''')
    opcao = int(input('>>>>>> Qual e a sua opcao ? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} e {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} e {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor e {maior}')
    elif opcao == 4:
        print(f'Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
    print('=-= *10')
    sleep(1.5)
print('Fim do programa! volte sempre!')                   