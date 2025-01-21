#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Você pode usar um laço de repetição para verificar se o valor inserido corresponde a 'M' ou 'F'. Dentro do laço, verifique a entrada do usuário e, se estiver errada, peça para que ele digite novamente. Dica: as estruturas de repetição como while podem ser úteis aqui, junto com uma condição que só será quebrada quando o valor correto for fornecido.


sexo = str(input("Informe seu sexo (M/F): ").upper())

while sexo != 'M' and sexo != 'F':
    print("Valor inválido! Por favor, digite 'M' para masculino ou 'F' para feminino.")
    sexo = input("Informe seu sexo (M/F): ").upper()

print(f"Sexo {sexo} registrado com sucesso.")

    
    #Guanabara
    
    
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper([0])
print(f'Sexo{sexo} registrado com sucesso')

  



