#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

# Loop para solicitar 6 números ao usuário
for c in range(1, 7):
    while True:  # Laço para garantir que a entrada seja válida
        try:
            num = int(input(f'Digite o {c}º valor: '))
            break  # Se a conversão for bem-sucedida, sai do laço
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
    
    # Verifica se o número é par
    if num % 2 == 0:
        soma += num  # Adiciona o número à soma
        cont += 1    # Conta mais um número par

# Exibe o resultado final
print(f'Você informou {cont} números PARES e a SOMA foi {soma}')
