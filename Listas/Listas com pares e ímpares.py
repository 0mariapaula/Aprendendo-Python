# Criamos uma lista com duas sublistas: uma para pares e outra para ímpares
num = [[], []]  # num[0] = pares | num[1] = ímpares

# Loop para ler 7 valores
for i in range(7):
    valor = int(input(f'Digite o {i+1}º valor: '))

    # Se for par, adiciona na lista de pares (índice 0)
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)  # Se for ímpar, adiciona na lista de ímpares (índice 1)

# Ordena cada uma das sublistas
num[0].sort()
num[1].sort()

# Mostra os resultados
print(f'\nOs valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
