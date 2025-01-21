'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''


# Inicializa os contadores
maiores_18 = 0
total_homens = 0
mulheres_menos_20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    
    # Lê a idade com validação
    while True:
        try:
            idade = int(input('Idade: '))
            if idade > 0:
                break
            print('Digite uma idade válida!')
        except:
            print('Digite uma idade válida!')
    
    # Lê o sexo com validação
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            break
        print('Digite apenas M ou F!')
    
    # Análise dos dados
    if idade >= 18:
        maiores_18 += 1
    
    if sexo == 'M':
        total_homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    
    # Pergunta se quer continuar
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('Digite apenas S ou N!')
    
    # Se não quiser continuar, sai do loop
    if continuar == 'N':
        break

print(f'\n{"RESULTADOS":=^30}')
print(f'Total de pessoas com mais de 18 anos: {maiores_18}')
print(f'Total de homens cadastrados: {total_homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_20}')