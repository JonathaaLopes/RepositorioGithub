"""Escreva um programa que leia dois numeros e que pergunte qual operacao voce deseja realizar. Voce deve poder calcular soma (+), subtracao (-), multiplicacao (*), e divisao (/). Exiba o resultado da operacao solicitada."""



numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

print('*********Escolha uma opcao*********')

print('1. Soma ')
print('2. Subtracao')
print('3. Multiplicacao')
print('4. Divisao')

opcao = int(input('Digite a opcao desejada: '))

if opcao == 1:
    resultado = numero1 + numero2
    print(f'O resultado da soma dos dois numeros e {resultado}')

elif opcao == 2:
    resultado = numero1 - numero2
    print(f'O resultado da subtracao dos numeros e {resultado}')

elif opcao == 3:

    resultado = numero1 * numero2
    print(f'O resultado da multiplicacao dos numeros e {resultado}')

elif opcao == 4:

    if numero2 and numero1 != 0:
        resultado = numero1 / numero2
        print(f'O resultado da divisao dos numeros e {resultado:.2f}')
    else:
        print('Erro: divisao por zero 0 nao e permitida')
else:
    print('Favor digite uma opcao valida')

