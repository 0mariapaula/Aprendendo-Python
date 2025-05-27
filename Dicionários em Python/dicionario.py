# Criando o dicionário
pessoa = {
    'nome': 'Carlos',
    'idade': 30,
    'cidade': 'Rio de Janeiro'
}

# Acessando um valor
print('Acessando o nome:', pessoa['nome'])  # Carlos

# Adicionando um novo par chave:valor
pessoa['profissao'] = 'Professor'
print('Adicionando a profissão:', pessoa)

# Modificando um valor existente
pessoa['idade'] = 31
print('Modificando a idade:', pessoa)

# Removendo um par
del pessoa['cidade']
print('Removendo a cidade:', pessoa)

# Percorrendo o dicionário com items()
print('\nPercorrendo com items():')
for k, v in pessoa.items():
    print(f'{k}: {v}')

# Agora criando outro dicionário
pessoa = {'nome': 'Maria', 'idade': 25, 'cidade': 'São Paulo'}

# Mostrando todas as chaves com keys()
print('\nMostrando as chaves:')
print(pessoa.keys())   # dict_keys(['nome', 'idade', 'cidade'])

for k in pessoa.keys():
    print(k)  # nome, idade, cidade

# Mostrando todos os valores com values()
print('\nMostrando os valores:')
print(pessoa.values())  # dict_values(['Maria', 25, 'São Paulo'])

for v in pessoa.values():
    print(v)  # Maria, 25, São Paulo

# Mostrando os pares chave-valor com items()
print('\nMostrando chave-valor com items():')
print(pessoa.items())  
# dict_items([('nome', 'Maria'), ('idade', 25), ('cidade', 'São Paulo')])

for chave, valor in pessoa.items():
    print(f'{chave} = {valor}')
