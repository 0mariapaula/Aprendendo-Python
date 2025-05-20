valores = []

# Lê 5 valores numéricos e guarda na lista
for i in range(5):
    num = int(input(f'Digite um número para a posição {i}: '))
    valores.append(num)

print('-' * 40)
print(f'Você digitou os valores: {valores}')

# Descobre o maior e o menor valor
maior = max(valores)
menor = min(valores)

# Mostra o maior valor e suas posições
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} ', end='')

print()

# Mostra o menor valor e suas posições
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} ', end='')

print()
