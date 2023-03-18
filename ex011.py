# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da parede? '))
altura = float(input('qual a altura da parede? '))
area = largura * altura
tinta = area/2
print('Sua parede tem a dimensão {}x{} e sua area é de {}m²\npara pintar está parede você precisara de {} litros de tintas ' .format(largura,altura,area,tinta))

