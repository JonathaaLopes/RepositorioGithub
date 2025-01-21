

#Estruturas de Repeticao

'''
Estruturas condicionais aninhadas em Python permitem verificar múltiplas condições,
onde uma condição leva a outra. Aqui está um exemplo básico para demonstrar como usar if,
elif, e else em um programa com estruturas condicionais aninhadas:

'''

# Exemplo de estrutura condicional aninhada

idade = int(input("Digite sua idade: "))

if idade >= 18:  # Verifica se a pessoa é maior de idade
    
    print("Você é maior de idade.")
    
    if idade >= 60:  # Condição aninhada para verificar se a pessoa é idosa
        
        print("Você também é considerado idoso.")
    else:
        print("Você ainda não é considerado idoso.")
else:
    print("Você é menor de idade.")
    
    if idade >= 12:  # Condição aninhada para verificar se a pessoa é adolescente
        
        print("Você é um adolescente.")
    else:
        print("Você é uma criança.")
        
        
'''
Explicação:
Primeiro if: Verifica se a idade é maior ou igual a 18.
Primeiro else: Se a pessoa não for maior de idade, vai para a condição de "menor de idade".
Condições aninhadas: Dentro de cada bloco (if e else), há outro conjunto de condições para verificar se a pessoa é idosa ou adolescente.
Se você rodar este código, verá que as respostas mudam conforme o valor da idade.

Essas estruturas aninhadas ajudam quando há várias condições interdependentes, mas cuidado para não criar muitos níveis de aninhamento, pois pode tornar o código difícil de entender.

'''
