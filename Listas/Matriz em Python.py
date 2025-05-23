# Criando a matriz vazia
matriz = [[], [], []]

# Preenchendo a matriz
for i in range(3):  # Para cada linha
    for j in range(3):  # Para cada coluna
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(valor)

# Mostrando a matriz formatada
print('\nMatriz 3x3:')
for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end=' ')  # ^5 centraliza em 5 espaços
    print()  # Pula para a próxima linha
