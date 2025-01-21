nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

tamanho = len(nome)
print("O comprimento do nome e:", tamanho)

nome = nome + " " + sobrenome
print("Apos concatenar as strings temos:", nome)

if sobrenome in nome:
    print("O sobrenome", sobrenome, "esta contido no nome", nome, ".")
    
print("O nome completo em minusculo e:", nome.lower())
print("O nome completo em maiusculo e:", nome.upper())