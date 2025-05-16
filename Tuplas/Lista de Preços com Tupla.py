# Crie um programa que tenha uma tupla única com
# nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    'Lápis', 1.50,
    'Caderno', 12.90,
    'Mochila', 120.00,
    'Borracha', 0.99,
    'Caneta', 2.00,
    'Livro', 45.00,
    'Estojo', 9.50,
    'Apontador', 3.25
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Percorre a tupla pulando de 2 em 2 (nome, preço)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:<30} R$ {preco:>7.2f}')

print('-' * 40)
