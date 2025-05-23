# Lista composta para armazenar os dados de todos os alunos
alunos = []

# Coleta de dados
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])  # Armazenamos nome, lista de notas e média
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

# Mostrando o boletim
print('\nBoletim:')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

# Mostrando notas individualmente
while True:
    opc = int(input('\nMostrar notas de qual aluno? (999 para parar) '))
    if opc == 999:
        break
    if 0 <= opc < len(alunos):
        print(f'Notas de {alunos[opc][0]}: {alunos[opc][1]}')
