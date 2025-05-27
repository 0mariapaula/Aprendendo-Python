# Criando o dicionário
jogador = {}

# Lendo o nome e quantidade de partidas
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Lista para guardar os gols
gols = []

# Lendo os gols de cada partida
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))

# Armazenando a lista de gols no dicionário
jogador['gols'] = gols

# Calculando o total de gols
jogador['total'] = sum(gols)

# Mostrando os dados do dicionário
print('\n--- Dados do jogador ---')
for k, v in jogador.items():
    print(f'{k}: {v}')

# Mostrando o desempenho detalhado
print('\n--- Detalhamento de partidas ---')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {g} gol(s).')

print(f'Foi um total de {jogador["total"]} gol(s).')
