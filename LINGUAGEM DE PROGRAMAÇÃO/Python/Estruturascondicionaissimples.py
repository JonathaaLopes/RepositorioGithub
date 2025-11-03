'''
O comando if

- O bloco de comandos definido pelo if so e executado caso sua
condicao seja verdadeira

- A condicao deve ser expressa de uma expressao logico-relacional

- Ha varias formas de ser organizar a sintaxe do comando if
simples
composta 
aninhada


 Exemplo

if <condicao> : # elabora a condicao e dois pontos.
    <Bloco de comandos> # Atencao a identacao! tab


'''

'''

** Estrutura condicional composta **

- A condicao de um comando if pode ser falsa. Nesse caso, pode-se
capturar tal evento com um comando else aliado ao respectivo if.

- Sintaxe do if-else em python

if <condicao> :
    <Bloco de comando 1>
else:
    <Bloco de comando 2>    



* Desenvolva um algoritmo que peca para o usuario informar um numero.
- O algoritmo devera informar se o numero e par ou impar.

* Construcao do programa
- Entrada: valor numerico
- Saida: mensagens que informam se o numero e par ou impar
- Passo a passo:
    - informar o numero
    - se o numero for par: imprimir "numero par"
    - caso contrario: imprimir "numeri impar"

'''
num = int(input('Digite um numero inteiro: '))

resto = int(num / 2)
resto = num - (resto * 2)

if resto == 0:
    print('numero Par.')
else:
    print('numero Impar.')
    
    
 # fazendo com operador resto %
 
num = int(input('Digite um numero inteiro: '))
 
resto = num % 2
 
if resto == 0:
    print('numero Par.')
else:
    print('numero Impar.')
    

'''
# ** Estruturas condicionais aninhadas **

    Pode-se compor uma estrutura condicional mais complexa
    
- Coloca-se um "if-else" dentro do outro, de acordo com a 
necessidade do algoritmo

- Pode-se utilizar estruturas simples, compostas e
multiplas, todas elas de maneira aninhada

- Criam-se varios niveis de decisoes em que, a decisao mais interna
so sera conferida caso a decisao mais externa tenha 
resultado verdadeiro.


'''

# exemplo

media = float(input('Digite um numero inteiro: '))

if media >= 7.0:
    print('Aprovado direto.')
else:
    if media >= 4.0:
        print('Tem direito a sub(recuperacao.)')
    else:
        print('Reprovou direto.')
        
'''

# ** elif **
if + else
    com if, elif e else em python
 Construa um programa que permite ao usuario escolher qual
 operacao deseja realizar com dois numeros distintos, como em uma
 calculadora.
 
    - Caso o usuario escolha a opcao 1, deve-se realizar a soma:
    - Caso seja escolhida a opcao 2, entao o programa deve calcular
    a subtracao entre os dois numeros;
    - Se o usuario escolhera opcao 4, ai teremos o calculo da divisao
    entre os dois numeros;
    - Caso nenhuma das opcoes 1,2,3 ou 4 sejam escolhidas, entao o
    programa mostrara a mensagem "Opcao invalida."

'''

# Exemplo de programa de calculadora simples

# Solicita ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Exibe o menu de operações disponíveis
print("Escolha a operação que deseja realizar:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Solicita ao usuário que escolha uma operação
opcao = input("Digite o número da operação desejada (1, 2, 3 ou 4): ")

# Realiza a operação escolhida pelo usuário
if opcao == "1":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif opcao == "2":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif opcao == "3":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif opcao == "4":
    # Verifica se o divisor é zero antes de realizar a divisão
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Opção inválida")
    
    

