# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00
# por cada Km acima do limite.
vel = float (input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('\033[31m Multado! Você exedeu o limite de velocidade que é de 80Km/h')
    multa = (vel-80) * 7
    print("Você deve pagar a multa de {:.2f}!".format(multa))
else:
    print('\033[32mTenha um bom dia ! Dirija com segurança!')

