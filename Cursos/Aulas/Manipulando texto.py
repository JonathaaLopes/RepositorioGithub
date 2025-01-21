#Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), upper(),
# lower(), capitalize(), title(), strip(), junção com join().

# 1 Fatiamento de String:

#O fatiamento permite extrair partes específicas de uma string.
# Você pode usar colchetes [] para acessar caracteres individuais ou intervalos de caracteres.
#Exemplo:

texto = "Python"
print(texto[0:2])  # Saída: "Py"
print(texto[:3])   # Saída: "Pyt"
print(texto[2:])   # Saída: "thon"
print(texto[-1])   # Saída: "n"

# 2 Análise com len:

#A função len() retorna o comprimento (número de caracteres) de uma string.

texto = "Python"
print(len(texto))  # Saída: 6

# 3 Análise com count:

#A função count() conta quantas vezes um determinado caractere ou sequência de caracteres aparece na string.

texto = "banana"
print(texto.count("a"))  # Saída: 3

# 4 Análise com find:

#A função find() encontra a posição de uma substring dentro da string. Retorna o índice da primeira ocorrência ou -1 se não encontrar.

texto = "Python"
print(texto.find("th"))  # Saída: 2
print(texto.find("x"))   # Saída: -1


# 5 Transformações com replace:

# O método replace() substitui uma parte da string por outra.

texto = "Python é legal"
novo_texto = texto.replace("legal", "incrível")
print(novo_texto)  # Saída: "Python é incrível"

# 6 Transformações com upper e lower:

# upper(): Converte todos os caracteres para maiúsculas.
# lower(): Converte todos os caracteres para minúsculas.

texto = "Python"
print(texto.upper())  # Saída: "PYTHON"
print(texto.lower())  # Saída: "python"

# 7 Transformações com capitalize e title:

#capitalize(): Converte o primeiro caractere para maiúscula e o restante para minúsculas.
#title(): Converte o primeiro caractere de cada palavra para maiúscula.

texto = "python é incrível"
print(texto.capitalize())  # Saída: "Python é incrível"
print(texto.title())       # Saída: "Python É Incrível"

# 8 Transformações com strip:

#O método strip() remove espaços em branco no início e no fim da string.
#Também existem lstrip() (remove apenas do início) e rstrip() (remove apenas do fim).

texto = "   Python   "
print(texto.strip())   # Saída: "Python"
print(texto.lstrip())  # Saída: "Python   "
print(texto.rstrip())  # Saída: "   Python"


#9 Junção com join:

# O método join() une elementos de uma lista ou tupla em uma única string, usando um separador.




