Algoritmo CaixaEletronico
Var
    saldo, valor: real
    opcao: inteiro
 
Início
    saldo <- 1000.0  // Saldo inicial
    Repita
        Escreva("Escolha uma opção:")
        Escreva("1 - Sacar dinheiro")
        Escreva(2 - Depositar dinheiro)  ### Erro na linha 11 esta faltando as "" aspas
        Escreva("3 - Verificar saldo")
        Escreva("4 - Sair")
        Leia(op)  ### (opcao) seria o correto
       
        Se opcao = 1 Então
            Escreva("Digite o valor para sacar:")
            Leia(valor)
            Se valor <= saldo Então
                saldo <- saldo - valor
                Escreva("Saque realizado com sucesso.")
            Senão
                Escreva("Saldo insuficiente.")
            FimSe
        FimSe
       
        Se opcao = 2 Então
            Escreva("Digite o valor para depositar:")
            Leia(vl) ### seria (valor) o correto
            saldo <- saldo + valor
            Escreva("Depósito realizado com sucesso.")
        FimSe
       
        Se opcao = 3 Então
            Escreva("Seu saldo atual é: ", saldo)
        FimSe
    Até opcao < 4  ### = 4 seria o correto
   
    Escreva("Obrigado por usar nosso caixa eletrônico.")
Fim