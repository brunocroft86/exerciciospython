#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('pedra', 'papel' , 'tesoura')
computador = randint(0, 2)
print('''Sua opcões:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jog♠ador]))
print('-='*11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÀLIDA')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÀLIDA')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÀLIDA')
