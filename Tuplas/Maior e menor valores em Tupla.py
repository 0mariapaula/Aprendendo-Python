# Crie um programa que vai gerar cinco números
# aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na
# tupla.

from random import randint

# Gera 5 números aleatórios de 0 a 10 e coloca em uma tupla
numeros = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)

# Mostra os números gerados
print('Números sorteados:', end=' ')
for n in numeros:
    print(n, end=' ')

# Mostra o maior e o menor número da tupla
print(f'\nMaior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')
