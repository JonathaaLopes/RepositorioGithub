#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


# Solicita ao usuário o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Exibe os 10 primeiros termos da PA
print("Os 10 primeiros termos da Progressão Aritmética são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=' → ' if i < 9 else 'Fim\n')
