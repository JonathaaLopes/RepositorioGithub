#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ").strip().lower()

# Remove os espaços da frase
frase_sem_espacos = frase.replace(" ", "")

# Verifica se a frase sem espaços é igual ao seu inverso
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase NÃO é um palíndromo.")
