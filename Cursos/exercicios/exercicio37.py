'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para Binario e igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('opcao invalida, tente novamente.')