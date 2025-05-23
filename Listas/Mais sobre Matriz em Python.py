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
        print(f'[{elemento:^5}]', end=' ')
    print()

# A) Soma de todos os valores pares
soma_pares = 0
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            soma_pares += elemento

# B) Soma dos valores da terceira coluna (índice 2)
soma_terceira_coluna = 0
for i in range(3):
    soma_terceira_coluna += matriz[i][2]

# C) Maior valor da segunda linha (linha de índice 1)
maior_segunda_linha = max(matriz[1])

# Exibindo os resultados
print(f'\nA soma de todos os valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
