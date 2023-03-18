# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já
# passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = atual - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas,idade,atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE! ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('você já deveria ter se alistado há {} anos'.format(saldo))




