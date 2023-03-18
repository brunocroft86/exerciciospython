# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Salario do comprador? R$ '))
anos = float(input('Em quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print('A prestacão será de R${:.2f}'.format(prestação))

if prestação <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado!')


