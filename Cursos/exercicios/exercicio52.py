# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Variável para contar quantas vezes o número é divisível
divisores = 0

# Verifica se o número é divisível por algum valor entre 1 e ele mesmo
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1  # Conta quantas vezes ele foi divisível

# Se foi divisível apenas por 1 e ele mesmo, é primo
if divisores == 2:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} NÃO é primo.")
