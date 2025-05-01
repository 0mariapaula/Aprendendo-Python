import random  # Importa o módulo para gerar escolhas aleatórias
import time    # Importa o módulo para dar "pausas" entre as mensagens

# Lista com as opções possíveis do jogo
opcoes = ['pedra', 'papel', 'tesoura']

# Computador escolhe aleatoriamente uma dessas opções
computador = random.choice(opcoes)

# Exibe opções para o jogador escolher
print('''Escolha uma opção:
[1] Pedra
[2] Papel
[3] Tesoura''')

# Lê a escolha do jogador
jogador = int(input('Sua jogada: '))

# Transforma o número digitado na palavra correspondente
if jogador == 1:
    jogador_escolha = 'pedra'
elif jogador == 2:
    jogador_escolha = 'papel'
elif jogador == 3:
    jogador_escolha = 'tesoura'
else:
    print('Jogada inválida!')
    exit()  # Encerra o programa se a escolha for inválida

# Faz uma contagem antes de mostrar o resultado (só para brincar)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ!!!')
time.sleep(0.5)

# Mostra o que cada um jogou
print('-=' * 15)
print('Você jogou: {}'.format(jogador_escolha))
print('Computador jogou: {}'.format(computador))
print('-=' * 15)

# Lógica para saber quem ganhou
if jogador_escolha == computador:
    print('EMPATE!')
elif (jogador_escolha == 'pedra' and computador == 'tesoura') or \
     (jogador_escolha == 'papel' and computador == 'pedra') or \
     (jogador_escolha == 'tesoura' and computador == 'papel'):
    print('VOCÊ VENCEU!')
else:
    print('COMPUTADOR VENCEU!')
