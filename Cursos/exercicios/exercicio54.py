#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

# Ano atual
ano_atual = date.today().year

# Contadores para maioridade
maiores = 0
menores = 0

# Loop para coletar o ano de nascimento de 7 pessoas
for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores += 1  # Contabiliza os maiores de idade
    else:
        menores += 1  # Contabiliza os menores de idade

# Resultado final
print(f"\nTotal de maiores de idade: {maiores}")
print(f"Total de menores de idade: {menores}")
