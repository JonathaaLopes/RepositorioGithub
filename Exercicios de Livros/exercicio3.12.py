#escreva um programa em python que calcule o tempo de um viagem de carro. Pergunte a distancia a percorrer e a velocidade media esperada para a viagem

distancia_viagem = float(input('Qual a distancia da viagem em km: '))

velocidade_media = float(input('Qual a velocidade media em k/h: '))

tempo = distancia_viagem / velocidade_media

print(f'sua distancia foi de {distancia_viagem}km e a velocidade media foi de {velocidade_media}em k/h e o tempo da viagem foi de {tempo:.2f} horas')