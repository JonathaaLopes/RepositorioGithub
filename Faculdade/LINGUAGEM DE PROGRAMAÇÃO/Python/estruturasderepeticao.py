'''

 Em Python, estruturas de repetição são usadas para executar um bloco de código várias vezes,
até que uma condição seja atendida ou por um número específico de vezes. As duas principais estruturas
de repetição em Python são for e while.

 Tambem conhecidas como lacos ou loops.
 Utilidade: iterar um bloco de comandos.
 Toda estrutura de repeticao possui um criterio de parada:
 'Criterio de parada pode ser falho gerando um loop infinito'#CUIDADO
 
    O comando for

- Repeticao com contagem
    Repete um bloco de comandos por um numero finito de vezes.
    
- A quantia de repericoes e controlada por uma variavel
    Gera-se uma sequencia numerica
    Variavel contadora (laco contado)

'''
# Exemplo

palavra = "Python"

for letra in palavra:
    print(letra)
    
    '''palavra = "Python": Aqui, estamos definindo uma variável chamada palavra que contém a string "Python".
for letra in palavra: Esse for vai percorrer cada caractere (letra) da string "Python".
Na primeira iteração, letra será "P".
Na segunda iteração, letra será "y", e assim por diante até a última letra.'''

# outro exemplo

''' Exemplo de Programa com for - Somando Números Pares
Vamos criar um programa que percorre uma lista de números e soma apenas os números pares. '''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:  # Verifica se o número é par
        soma_pares += numero  # Adiciona o número par à soma

print("A soma dos números pares é:", soma_pares)

'''Explicação do Código:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: Criamos uma lista de números de 1 a 10.
soma_pares = 0: Inicializamos uma variável chamada soma_pares com o valor 0, que vai guardar a soma dos números pares.
for numero in numeros:: Usamos o for para percorrer cada número da lista numeros.
if numero % 2 == 0:: Dentro do loop, usamos um if para verificar se o número é par. A condição numero % 2 == 0 verifica se o resto da divisão do número por 2 é igual a 0, o que significa que o número é par.
soma_pares += numero: Se o número for par, ele é adicionado à variável soma_pares.
print("A soma dos números pares é:", soma_pares): Após o loop, o programa imprime a soma de todos os números pares.'''




''' O range é uma função muito útil em Python que gera uma sequência de números.

É frequentemente usada em loops for para iterar um número específico de vezes.

Como Funciona o range
A função range pode ser usada de várias maneiras, dependendo de quantos argumentos você fornece. Vamos ver os casos mais comuns:

range(stop): Gera uma sequência de números de 0 até stop - 1.
range(start, stop): Gera uma sequência de números de start até stop - 1.
range(start, stop, step): Gera uma sequência de números de start até stop - 1, mas pulando step números a cada vez.'''


# 1. Usando range(stop)

for i in range(5):
    print(i)

''' 

Explicação:

range(5) gera a sequência 0, 1, 2, 3, 4.
O loop for itera através desses números e imprime cada um.

'''

# 2. Usando range(start, stop)

for i in range(2, 6):
    print(i)

'''

Explicação:

range(2, 6) gera a sequência 2, 3, 4, 5.
O loop for itera de 2 até 5 e imprime cada número.

'''
# 3. Usando range(start, stop, step)

for i in range(1, 10, 2):
    print(i)


'''

Explicação:

range(1, 10, 2) gera a sequência 1, 3, 5, 7, 9.
Aqui, start é 1, stop é 10, e step é 2. O loop começa em 1 e incrementa de 2 em 2, parando antes de 10.

'''

'''

Usando range com Números Negativos
Você também pode usar range com números negativos, tanto para contagem para trás quanto para definir o passo como negativo.
'''

for i in range(10, 0, -2):
    print(i)
    
'''
   Explicação:

range(10, 0, -2) gera a sequência 10, 8, 6, 4, 2.
O loop começa em 10 e decrementa de 2 em 2 até que o número seja maior que 0.
'''


## For se sabe o limite, o while nao.