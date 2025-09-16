def area (largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')
# Exemplo de uso
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)