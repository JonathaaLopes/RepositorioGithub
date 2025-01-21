#exemplo da aula

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
    print('FIM')   
    
#condicao simplificada * nao recomendado * pode complicar um pouco o entendimento*

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo <=3 else 'carro velho')
print('Fim')

#exemplo pratico

n1 = float(input('Digite a primeira nota: '))
n2 = float((input('Digite a segunda nota: ')))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media foi boa ! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')             
     
     