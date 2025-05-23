# Listas para armazenar os números, pares e ímpares
numeros = []
pares = []
impares = []

# Loop para ler os números
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)  # Adiciona o número à lista principal

    # Verifica se o número é par ou ímpar
    if num % 2 == 0:
        pares.append(num)  # Adiciona à lista de pares
    else:
        impares.append(num)  # Adiciona à lista de ímpares

    # Pergunta se o usuário quer continuar
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

# Exibe as três listas geradas
print('-' * 40)
print(f'Lista de números digitados: {numeros}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares: {impares}')
