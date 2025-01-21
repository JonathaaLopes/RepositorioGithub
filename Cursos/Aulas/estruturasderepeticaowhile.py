#while condicao:
    # bloco de código a ser repetido
    
    
    
    #exemplo basico
    
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o valor de contador

'''O laço começa com contador valendo 0.
Enquanto contador < 5 for verdadeiro, o código dentro do while será executado.
A cada iteração, contador é incrementado em 1, até que a condição contador < 5 se torne False e o laço pare.


Cuidado com loops infinitos:
Se a condição dentro do while nunca for False, o laço continuará rodando indefinidamente. Isso é chamado de loop infinito.

Exemplo de um loop infinito (não execute!):

while True:
    print("Isso nunca vai parar!")




Dica:
Sempre tenha certeza de que há uma condição que fará o laço parar, como o incremento de uma variável ou outra alteração que torne a condição falsa em algum momento.

Esse é o conceito básico do while. Você pode combiná-lo com outras estruturas como if, listas, e muito mais para resolver problemas complexos!

'''

#Aqui está um exemplo mais completo usando o while em Python. Vamos criar um pequeno programa de adivinhação de números, onde o jogador tem que adivinhar um número escolhido aleatoriamente pelo programa.


import random  # Biblioteca para gerar números aleatórios

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativa = 0  # Contador de tentativas
chute = None  # Variável para armazenar o palpite do usuário

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.\n")

# Enquanto o jogador não adivinhar o número
while chute != numero_secreto:
    chute = int(input("Digite seu palpite: "))
    tentativa += 1  # Incrementa o número de tentativas

    if chute < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif chute > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativa} tentativas.")

print("\nFim do jogo.")

