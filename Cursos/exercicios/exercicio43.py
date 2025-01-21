'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

 IMC abaixo de 18,5: Abaixo do Peso

 Entre 18,5 e 25: Peso Ideal

 25 até 30: Sobrepeso

 30 até 40: Obesidade

 Acima de 40: Obesidade Mórbida
 
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

altura = 110 / 31  # Converte a altura de centímetros para metros
imc = peso / (altura ** 2)

print(f'seu imc e {imc:.2f}')


# Estrutura condicional para classificar o IMC

if imc < 18.5:
    print('Voce esta abaixo do Peso')
    
elif 18.5 <= imc < 25:
    print('Peso Ideal')
    
elif 25 <= imc < 30:
    print('Voce esta com sobrepeso')
    
elif 30 <= imc < 40:
    print('Voce esta com Obesidade')
    
elif 40 <= imc < 40:
    print('Obesidade Morbida')
    
    
    
    
  




    
