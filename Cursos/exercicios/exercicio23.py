#Faça um programa que leia um número de 0 a 9999 e mostre 
#na tela cada um dos dígitos separados.

num = int(input('Escreva um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


##De outra maneira


# Solicita ao usuário que insira um número de 0 a 9999
numero = input("Digite um número de 0 a 9999: ")

# Preenche o número com zeros à esquerda, caso necessário, para garantir que tenha 4 dígitos
numero = numero.zfill(4)

# Exibe cada dígito separadamente
print("Milhar:", numero[0])
print("Centena:", numero[1])
print("Dezena:", numero[2])
print("Unidade:", numero[3])
