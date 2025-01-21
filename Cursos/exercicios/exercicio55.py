#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.



# Variáveis para armazenar o maior e menor peso
maior_peso = 0
menor_peso = 0

# Loop para coletar o peso de 5 pessoas
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))

    # Para a primeira pessoa, inicializamos o maior e menor peso
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        # Atualiza o maior e o menor peso
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

# Resultado final
print(f"O maior peso lido foi {maior_peso:.2f} kg")
print(f"O menor peso lido foi {menor_peso:.2f} kg")
