import random  # Importamos o módulo random para gerar números aleatórios

jogos = []  # Lista composta para armazenar todos os jogos

quant = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(quant):
    jogo = []  # Lista simples para armazenar um único jogo
    while len(jogo) < 6:  # Enquanto não tiver 6 números
        num = random.randint(1, 60)  # Sorteia um número entre 1 e 60
        if num not in jogo:  # Garante que o número não se repita no mesmo jogo
            jogo.append(num)
    jogo.sort()  # Ordena o jogo para ficar mais bonito
    jogos.append(jogo)  # Adiciona o jogo completo à lista composta

# Mostrando os palpites
print('\nSeus palpites para a MEGA SENA são:')
for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')
