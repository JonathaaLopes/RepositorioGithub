n1 = int(input('digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2


#metodo antigo ainda valido.

print('A soma entre', n1, 'e', n2, 'vale', s) 

#metodo novo

print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
