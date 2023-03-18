#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:a)
# Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

times = ('Corinthians','Palmeiras','Santos','Gremio',
         'Cruzeiro','Flamengo',
         'Vasco','Chapecoense','Atlético','Botafogo',
         'Atléto-PR','Bahia')
print('='*30)
print(f'Lista de times do Brasileirão: {times}')

print('='*30)

print(f'os 5 primeiros times são:{times[0:5]}')

print('='*30)

print(f'Os ultimos 4 colocados saõ: {times[8:12]}')

print('='*30)

print(f'Os times em ordem alfabeticas sao:{sorted(times)}')

print('='*30)

print(f'O Chapecoense está na {times.index("Chapecoense") +1} posição:')


