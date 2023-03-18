# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:

n1 = int (input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número:'))
if n1 < n2:
    print('O segundo número é maior: ')
elif n1 > n2:
    print('O primeiro número é maior: ')
elif n1 == n2:
    print('Os numeros sáo iguais: ')
