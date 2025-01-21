#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


#Criei um programa que:
'''
1.Usa um loop infinito (while True) para continuar pedindo números
2.Tem uma condição de parada quando o usuário digita 999
3.Mantém um contador para saber quantos números foram digitados
4.Soma todos os números (exceto o 999)
5.No final, mostra tanto a quantidade de números quanto a soma total

O programa é simples de usar - basta executá-lo e digitar números inteiros. Para parar, digite 999.

'''

contador = 0
soma = 0

while True:
    num = int(input('Digite um numero inteiro (999 para parar): '))
    
    if num == 999:
        break
    
    contador += 1
    soma += num
    

print(f'\nVoce digitou {contador} numeros.')
print(f'A soma entre eles e {soma}.')