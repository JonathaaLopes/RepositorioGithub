#modifique o programa anterior para que aceite respostas com letra maiuscula e minusculas em todas as questoes.

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Resposta da questao {questao}: ").lower().upper()
    if questao == 1 and resposta == "bB":
        pontos += 1
    if questao == 2 and resposta == "aA":
        pontos += 1
    if questao == 3 and resposta == "dD":
        pontos += 1

    questao += 1

print(f" O aluno fez {pontos} pontos")