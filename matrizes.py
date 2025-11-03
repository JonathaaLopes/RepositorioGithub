




# Criando uma matriz vazia
# Inicializa uma lista vazia para armazenar a matriz
mat = []

# Loop para criar 3 linhas
for i in range(3):
    linha = []  # Inicializa uma lista vazia para cada linha
    for j in range(3):
        # Solicita ao usuário que insira um elemento para a posição atual
        print(f"Insira o elemento da linha {i} coluna {j}:")
        dado = int(input())  # Converte a entrada para inteiro
        linha.append(dado)   # Adiciona o elemento à linha
    mat.append(linha)  # Adiciona a linha completa à matriz

# Exibe cada elemento individualmente
print("\nElementos da Matriz:")
for i in range(3):
    for j in range(3):
        print(f"O elemento da linha {i} coluna {j} é {mat[i][j]}")

# Exibe a matriz completa de forma mais legível
print("\nMatriz completa:")
for linha in mat:
    print(linha)
