# Lista principal que vai conter todas as pessoas
pessoas = []

# Lista temporária para armazenar cada pessoa antes de adicionar na lista principal
temp = []

# Variáveis para controlar o maior e menor peso
maior = menor = 0

while True:
    # Lê os dados da pessoa
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    
    # Adiciona os dados na lista temporária
    temp.append(nome)
    temp.append(peso)
    
    # Faz uma cópia da lista temp e adiciona na lista principal
    pessoas.append(temp[:])  # Importante usar [:] para copiar a lista, e não a referência
    
    # Limpa a lista temporária para a próxima pessoa
    temp.clear()

    # Pergunta se quer continuar
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp != 'S':
        break

# Descobre o maior e o menor peso
for i, p in enumerate(pessoas):
    if i == 0:  # Primeiro registro define o maior e menor
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]

# Exibe o número de pessoas cadastradas
print(f'\nAo todo, você cadastrou {len(pessoas)} pessoas.')

# Exibe as pessoas mais pesadas
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print()

# Exibe as pessoas mais leves
print(f'O menor peso foi de {menor}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

print()
