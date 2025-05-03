sexo = input('Digite o sexo [M/F]: ').strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Valor inválido! Por favor, digite apenas M ou F.')
    sexo = input('Digite o sexo [M/F]: ').strip().upper()

print('Sexo registrado com sucesso:', sexo)
