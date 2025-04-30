# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número para conversão: '))

print('Digite uma numeração para escolher a conversão.')

print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')

conversao = int(input('Escolha a opção desejada: '))

if conversao == 1:
    binario = format(num, 'b')
    print(binario)
elif conversao == 2:
    octal = format(num, 'o')
    print(octal)
elif conversao == 3:
    hexadecimal = format(num, 'x')
    print(hexadecimal.upper())
else:
    print('\033[1:31mVocê não digitou nenhuma das opções!\033[m')