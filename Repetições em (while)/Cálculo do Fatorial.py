# Solicita ao usuário um número inteiro
n = int(input('Digite um número para calcular seu fatorial: '))

# Variável que vai acumular o resultado do fatorial (começa com 1 porque 1 é o neutro da multiplicação)
fatorial = 1

# Mostra na tela o início da expressão fatorial (ex: 5! = ), mas não pula de linha
print(f'{n}! = ', end='')

# Laço for que vai de n até 1, voltando 1 a cada passo (ex: 5, 4, 3, 2, 1)
for c in range(n, 0, -1):
    print(c, end=' ')  # Mostra o número atual
    print('x' if c > 1 else '= ', end='')  # Mostra "x" se não for o último número, senão mostra "="

    fatorial *= c  # Multiplica o valor atual de fatorial pelo número (acumulando o produto)

# Após o laço, imprime o resultado final do fatorial
print(f'{fatorial}')
