'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''


import time

# Contagem regressiva de 10 até 0
for count in range(10, -1, -1):
    print(count)
    time.sleep(0.5)  # Pausa de 1 segundo entre os números

print("Feliz Ano Novo! 🎆🎇")



