from random import randint
from time import sleep
from operator import itemgetter

# Criando o dicionário com os resultados aleatórios
jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

# Mostrando os resultados
print('Valores sorteados:')
for jogador, resultado in jogo.items():
    print(f'{jogador} tirou {resultado} no dado.')
    sleep(0.5)  # pausa para ficar mais legal de visualizar

# Ordenando o dicionário em ordem decrescente pelo resultado
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Mostrando o ranking
print('\nRanking dos jogadores:')
for i, (jogador, resultado) in enumerate(ranking, start=1):
    print(f'{i}º lugar: {jogador} com {resultado}')
    sleep(0.5)
