#Escreva um programa que leia tres numeros e que imprima o maior e o menor.

print('***********************        ************************')

print('Digite tres numeros para somar e mostrar o menor e maior numero')

numero_1 = int(input('escreva o primeiro numero: '))
numero_2 = int(input('escreva o segundo numero: '))
numero_3 = int(input('escreva o segundo terceiro: '))

soma = numero_1 + numero_2 + numero_3

maior = max(numero_1, numero_2, numero_3)
menor = min(numero_1, numero_2, numero_3)

print('\nResultados')
print(f'A soma dos tres numeros e {soma}')
print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')