#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


n = int(input('escreva um numero: '))
d = n * 2
t = n * 3
r = n ** 0.5

print('numero digitado foi {0} dobro e {1} o triplo e {2} raiz quadrada {3}'.format(n, d, t, r))



#Guanabara

n = int(input('Digite um numero'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print(' O triplo de {} vale {}.\n A raiz quadrada de {} e igual a {:.2f}.'.format(n, t, n, r))


#outra forma direta

n = int(input('digite um numero: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} e igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))