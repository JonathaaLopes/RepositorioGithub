



# Dicionário para armazenar os produtos
produtos = {}

# Função para cadastrar um novo produto
def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    # Adiciona o produto ao dicionário
    produtos[codigo] = {"nome": nome, "preco": preco}
    print("Produto cadastrado com sucesso!")

# Função para exibir todos os produtos cadastrados
def exibir_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for codigo, dados in produtos.items():
            print(f"Código: {codigo} | Nome: {dados['nome']} | Preço: R$ {dados['preco']:.2f}")

# Programa principal
while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar produto")
    print("2 - Exibir produtos")
    print("3 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        exibir_produtos()
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
