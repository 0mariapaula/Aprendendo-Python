import random  # Importa o módulo random para gerar números aleatórios

vitorias = 0  # Contador de vitórias do jogador

while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)  # Computador escolhe um número aleatório de 0 a 10
    total = jogador + computador

    # Jogador escolhe par ou ímpar
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    # Verifica quem ganhou
    if (total % 2 == 0 and tipo == 'P') or (total % 2 == 1 and tipo == 'I'):
        print('Você VENCEU!\n')
        vitorias += 1  # Aumenta o número de vitórias
    else:
        print('Você PERDEU!')
        break  # Encerra o jogo se o jogador perder

print(f'GAME OVER! Você venceu {vitorias} vezes.')
