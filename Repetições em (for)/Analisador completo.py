somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('_____{}ª PESSOA_____'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()

    somaidade += idade

    # Verifica se é o primeiro homem ou se é o mais velho
    if sexo == 'm':
        if idade > maioridadehomem or p == 1:
            maioridadehomem = idade
            nomevelho = nome

    # Conta mulheres com menos de 20
    if sexo == 'f' and idade < 20:
        totmulher20 += 1

# Calcula a média
mediaidade = somaidade / 4

print('A média de idade do grupo é {:.1f} anos.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, maioridadehomem))
print('No total são {} mulheres com menos de 20 anos.'.format(totmulher20))
