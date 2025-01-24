''' Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores
 a R$ 1.250, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%. '''

salario = float(input('Digite o valor de seu salario: '))

if salario > 1250:
    aumento = salario * 0.10
    print(f'seu aumento foi de 10% do salario {salario} e seu aumento foi de {aumento} e seu novo salario sera de {salario+aumento}')
else:
    salario <= 1250
    aumento = salario * 0.15
    print(f'seu aumento foi de 15% do valor do {salario} e seu aumento foi de {aumento} e seu novo salario sera de {salario+aumento}')




