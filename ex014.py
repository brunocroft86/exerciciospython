# Exercício Python 14: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

c = float (input("Informe a temperatura em C: "))
f = (c * 1.8) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c,f))