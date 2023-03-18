#Crie um programa que leia dois valores e mostre um menu na tela:

'''[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Qual é a sua opcão? '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, produto))

    elif opção == 3:
        if n1 > n2:
            maior = n1
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))


    elif opção == 4:
        print('Informe o número novamente!')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))


    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inváda! Tente novamenmte. ')
    print('+-='*10)
    sleep(2)

print('Fim do programa! Volte sempre')

