# Inicialização dos contadores
maior18 = 0         # Pessoas com mais de 18 anos
homens = 0          # Homens cadastrados
mulheres_menor20 = 0  # Mulheres com menos de 20 anos

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))

    # Leitura do sexo com validação
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    # Verifica critérios para contagem
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor20 += 1

    # Verifica se o usuário quer continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

# Resultados finais
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menor20} mulheres com menos de 20 anos')
