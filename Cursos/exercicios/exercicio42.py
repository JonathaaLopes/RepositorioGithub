'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

 EQUILÁTERO: todos os lados iguais

 ISÓSCELES: dois lados iguais, um diferente

 ESCALENO: todos os lados diferentes'''
 
 
 
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  ### A regra é que a soma de dois lados deve ser sempre maior que o terceiro. Se isso for verdade para todos os lados
    
    print('Os segmentos acima podem formar um triângulo', end=' ')
    
    if r1 == r2 == r3: ### Triângulo Equilátero: Todos os lados são iguais.
        print('Equilátero!') 
        
    elif r1 != r2 and r2 != r3 and r1 != r3: ### Triângulo Escaleno: Todos os lados são diferentes.
        print('Escaleno!')
        
    else:
        print('Isósceles!') ### Triângulo Isósceles: Dois lados são iguais.
        
else:
    print('Os segmentos acima não podem formar um triângulo')
