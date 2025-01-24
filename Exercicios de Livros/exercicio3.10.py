#faca um programa que calcule o aumento de um salario. Ele deve solicitar o valor do salario e a porcentagem do aumento. Exiba o valor do aumento e do novo salario.


salario = float(input('Digite o valor do salario atual: '))
percentual_aumento = float(input('digite a porcentagem do aumento (ex: 10 para 10%): '))

percentual_aumento = salario * (percentual_aumento / 100)

salario_atual = salario + percentual_aumento

print(f'seu aumento foi de {percentual_aumento}')
print(f'seu novo salario e de {salario_atual}')