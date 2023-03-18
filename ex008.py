# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros.

nm = float (input('Digite em número em metros '))
cent = nm * 100
mil = nm * 1000
print('O valor de {}, em centimetros é {}, e em milimitros é {}'.format(nm,cent,mil))

