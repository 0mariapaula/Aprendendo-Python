def aumentar (preço = 0, taxa = 0, format=False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)
def diminuir (preço = 0, taxa = 0, format=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)

def dobro (preço= 0, format=False):
    res = preço * 2
    return res if format is False else moeda(res)

def metade (preço = 0, format=False):
    res = preço / 2
    return res if format is False else moeda(res)

def moeda (preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço=0, taxaaum=10, taxared=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaaum}% de aumento: \t{aumentar(preço, taxaaum, True)}')
    print(f'{taxared}% de redução: \t{diminuir(preço, taxared, True)}')
    print('-'*30)