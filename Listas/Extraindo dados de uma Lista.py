numeros = []  # Lista para armazenar os números digitados

# Loop para entrada de vários números
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)  # Adiciona o número à lista

    # Pergunta se o usuário deseja continuar
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

# A) Mostra a quantidade de números digitados
print('-' * 40)
print(f'A) Você digitou {len(numeros)} números.')

# B) Mostra os valores em ordem decrescente
numeros.sort(reverse=True)  # Ordena do maior para o menor
print(f'B) Os valores em ordem decrescente são: {numeros}')

# C) Verifica se o número 5 foi digitado
if 5 in numeros:
    print('C) O número 5 foi digitado e está na lista.')
else:
    print('C) O número 5 NÃO foi digitado.')
