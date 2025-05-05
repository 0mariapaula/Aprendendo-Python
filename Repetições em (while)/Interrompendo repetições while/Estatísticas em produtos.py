total_gasto = 0         # Soma total dos preços dos produtos
produtos_1000 = 0       # Quantidade de produtos com preço > R$1000
produto_mais_barato = ''
preco_mais_barato = 0
primeiro_produto = True  # Para identificar o primeiro produto cadastrado

while True:
    print('-' * 30)
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))

    total_gasto += preco  # Soma o preço ao total gasto

    if preco > 1000:
        produtos_1000 += 1  # Conta produtos acima de R$1000

    # Verifica se é o produto mais barato
    if primeiro_produto or preco < preco_mais_barato:
        produto_mais_barato = nome
        preco_mais_barato = preco
        primeiro_produto = False

    # Pergunta se o usuário quer continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

# Mostra os resultados finais
print('-' * 30)
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'{produtos_1000} produto(s) custam mais de R$1000.00')
print(f'O produto mais barato foi "{produto_mais_barato}" que custou R${preco_mais_barato:.2f}')
