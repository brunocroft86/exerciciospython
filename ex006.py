# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int (input('Digite um número! '))
d = n+n
t = n *3
r = n **(1/2)
print('Analisando o numero {}\n o seu dobro é {} \n e seu triblo é {}\n e sua raiz quadrada é {:.2f}'.format(n,d,t,r))

