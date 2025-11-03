lista = []

for i in range(10):
    print("Digite o elemento da posicao", i)
    dado = int(input())
    lista.append(dado)
    
print("Lista preenchida:")

for i in range(10):
    print("O elemento da posicao", i, "e", lista[i])