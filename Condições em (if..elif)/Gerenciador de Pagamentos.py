# Solicita ao usuário o valor do produto
preco = float(input('Digite o preço do produto: R$ '))

# Mostra as opções de pagamento disponíveis
print('''Formas de pagamento:
[1] À vista no dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)''') # essas ''' permite que o voce escreva os textos com quebra de linha sme precisar do \n
# Usuário escolhe a forma de pagamento
opcao = int(input('Escolha a forma de pagamento (1/2/3/4): '))

# Verifica qual opção o usuário escolheu
if opcao == 1:
    # Desconto de 10% no valor original
    total = preco - (preco * 0.10)
    print('Você pagará R$ {:.2f} com 10% de desconto.'.format(total))

elif opcao == 2:
    # Desconto de 5% no valor original
    total = preco - (preco * 0.05)
    print('Você pagará R$ {:.2f} com 5% de desconto.'.format(total))

elif opcao == 3:
    # Preço sem desconto ou juros (preço normal)
    total = preco
    print('Você pagará R$ {:.2f} em até 2x no cartão (sem juros).'.format(total))

elif opcao == 4:
    # Solicita quantas parcelas o usuário quer
    parcelas = int(input('Quantas parcelas? '))
    
    if parcelas < 3:
        # Se o usuário escolheu menos de 3, a opção está errada
        print('Número de parcelas inválido para esta opção.')
    else:
        # Aplica 20% de juros ao valor original
        total = preco + (preco * 0.20)
        # Calcula quanto será cada parcela
        valor_parcela = total / parcelas
        print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(parcelas, valor_parcela))
        print('Total com juros: R$ {:.2f}'.format(total))

else:
    # Caso o usuário digite uma opção inválida
    print('Opção inválida. Tente novamente.')
