#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando
#o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

print('\033[1;31;35m{:💞^40}'.format(' LOJAS JUJUBINHA '))
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamentos
[1] à vista dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcão = int(input('Qual é a opcão? '))
if opcão == 1:
    total = preço - (preço * 10 / 100)
elif opcão == 2:
    total = preço - (preço * 5 / 100)
elif opcão == 3:
    total = preço
    parcela = preço/2
    print('Sua compra será percelada em 2x e o valor da parcela será de {:.2f}, sem juros'.format(parcela))
elif opcão == 4:
    total = preço + (preço * 20 /100 )
    totalparcela = int(input('Em quantas parcelas? '))
    parcela = total/totalparcela
    print('Sua compra será parcelada em {}x e o valor das parcelas será de {:.2f}, com juros '.format(totalparcela,parcela))
else:
    total = preço
    print('\033[1;31mOpcão inválida tente mais uma vez!')
print('Sua compre de R${:.2f}, vai custar R${:.2f} no final. '.format(preço,total))
2



