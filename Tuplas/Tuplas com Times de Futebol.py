# Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = (
    'Palmeiras', 'Flamengo','Red Bull Bragantino',
    'Cruzeiro','Fluminense','Ceará',
    'Atlético-MG','Bahia','Botafogo',
    'Corinthians','Fortaleza','Mirassol',
    'Internacional','Vitória','Grêmio',
    'São Paulo','Vasco da Gama','Juventude',
    'Santos','Sport')
print('-=' *15)
print(f'Lista d times: {times}')
print('-=' *15)

print(f' Os 5 primeiros times são {times[0:5]}')
print('-----------' *15)
print(f'Os últimos 4 colocados são {times[-4:]}') #ou print(f'Os últimos 4 colocados são {times[16:20]}')
print('-----------' *15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-----------' *15)
print(f'O Flamengo está na {times.index("Flamengo")+1} posição')