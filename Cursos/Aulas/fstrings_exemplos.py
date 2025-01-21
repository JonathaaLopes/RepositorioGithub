
# Exemplos de f-strings

# Exemplo básico de f-string
nome = "João"
idade = 30
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Cálculos dentro de f-strings
a = 5
b = 10
print(f"A soma de {a} e {b} é {a + b}.")

# Formatação de números
pi = 3.14159
print(f"O valor de pi com duas casas decimais é {pi:.2f}.")

# Preenchimento com zeros
numero = 42
print(f"O número formatado é {numero:04d}.")

# Incluindo expressões complexas
x = 10
y = 5
print(f"O maior valor entre {x} e {y} é {max(x, y)}.")

# Escapando chaves
print(f"Mostrando chaves literais: {{ e }}")

# Converter um número em diferentes bases
num = 255
print(f"Em binário: {bin(num)[2:]}, em octal: {oct(num)[2:]}, em hexadecimal: {hex(num)[2:]}")

# Exemplo prático com salário
funcionario = "Carlos"
salario = 3500.456
print(f"O funcionário {funcionario} recebe um salário de R${salario:.2f}.")
