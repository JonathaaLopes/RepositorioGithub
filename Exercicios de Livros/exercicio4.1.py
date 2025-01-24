#programa que le o valor mais alto

a = int(input('escreva o primeiro numero: '))

b = int(input('escreva o segundo nome: '))

if a > b:
    print(f'o valor de a {a} foi maior que o valor de b {b}')

if b > a:
    print(f'o valor de b {b} foi maior que o valor de a {a}')

if a == b and b == a:
    print('numeros iguais digitados')
