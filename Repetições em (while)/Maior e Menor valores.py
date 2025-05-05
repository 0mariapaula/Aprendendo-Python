num = 0
lista = []
escolha = 'S'
while escolha == 'S':
    num = int(input('Escolha um número inteiro: '))
    lista.append(num)
    escolha = input('Quer continuar? Selecione SIM ou NÃO [S/N]: ').upper().strip()
lista.sort()
print('A média entre os valores selecionados foi: {:.2f};\nO maior valor selecionado foi: {};\nO menor valor selecionado foi: {}.'.format(sum(lista)/len(lista),lista[-1],lista[0]))

