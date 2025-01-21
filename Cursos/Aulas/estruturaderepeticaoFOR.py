'''Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender.'''


## For se sabe o limite, o while nao.


#exemplo


#for variável in sequencia: 
    
    # bloco de código a ser repetido

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)


#Isso irá imprimir os números de 1 a 5, cada um em uma nova linha.




numeros = [10, 20, 30, 40, 50]
soma = 0  # Variável que armazenará o valor da soma

# Iterar sobre a lista de números
for numero in numeros:
    soma += numero  # Adiciona o valor de 'numero' à variável 'soma'

print(f"A soma dos números é: {soma}")










