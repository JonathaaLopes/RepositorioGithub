#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))