# Lista para guardar todos os dicionários
pessoas = []

# Variável para somar as idades
soma_idades = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip()
    
    # Validação do sexo
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    
    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']

    # Adicionando cópia do dicionário na lista
    pessoas.append(pessoa.copy())

    # Continuar?
    resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break

# Média de idade
media = soma_idades / len(pessoas)

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')

# C) Lista de mulheres
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

# D) Pessoas acima da média
print('D) Lista de pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
