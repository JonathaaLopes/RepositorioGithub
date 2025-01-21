#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('insira o valor de seu salario em R$'))

valor = salario + (salario * 15 / 100)

print(' seu salario de R${:.2f}, com aumento de 15% por cento  fica R${:.2f}'.format(salario, valor))