# Criando o dicionário
aluno = {}

# Lendo os dados
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

# Determinando a situação com base na média
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

# Mostrando o conteúdo do dicionário
print('\n--- Resultado ---')
for k, v in aluno.items():
    print(f'{k}: {v}')
