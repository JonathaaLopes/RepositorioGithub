produto = {
    'codigo': 0,
    'descricao': "",
    'preco': 0.0,
    'qtde': 0.0
}

produto['codigo'] = int(input("Digite o codigo do produto:\n"))
produto['desricao'] = input("Digite a descricao do produto:\n")
produto['preco'] = float(input("Digite o preco do produto:\n"))
produto['qtde'] = float(input("Digite a quantidade em estoque do produto:\n"))

print("codigo: ", produto['codigo'])
print("descricao: ", produto['descricao'])
print("preco: ", produto['preco'])
print("Quantidade estoque: ", produto['qtde'])