jogadores = []  # Lista para armazenar todos os jogadores

while True:
    jogador = {}  # Dicionário para armazenar dados de um jogador
    jogador['nome'] = input('Nome do jogador: ')
    
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []  # Lista para armazenar gols por partida

    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))

    jogador['gols'] = gols[:]  # Armazena a lista de gols no dicionário
    jogador['total'] = sum(gols)  # Soma total de gols

    jogadores.append(jogador.copy())  # Adiciona cópia do dicionário na lista

    resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break

print('-=' * 30)
# Cabeçalho da tabela
print(f'{"cod":<4} {"nome":<15} {"gols":<20} {"total":<5}')
print('-' * 50)

# Exibe todos os jogadores em formato de tabela
for i, j in enumerate(jogadores):
    print(f'{i:<4} {j["nome"]:<15} {str(j["gols"]):<20} {j["total"]:<5}')

# Sistema de consulta
while True:
    print('-' * 50)
    consulta = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    
    if consulta == 999:
        break
    
    if consulta >= len(jogadores) or consulta < 0:
        print(f'ERRO! Não existe jogador com código {consulta}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[consulta]["nome"]}:')
        for i, g in enumerate(jogadores[consulta]['gols']):
            print(f'   No jogo {i + 1} fez {g} gol(s).')

print('<< VOLTE SEMPRE >')
