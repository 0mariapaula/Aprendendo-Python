print('==== CALCULADORA COM MENU ====')

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

opcao = 0  # Inicializa com algo diferente de 5 para entrar no loop

while opcao != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('A soma é:', n1 + n2)
    elif opcao == 2:
        print('O produto é:', n1 * n2)
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        n1 = float(input('Digite o novo primeiro valor: '))
        n2 = float(input('Digite o novo segundo valor: '))
    elif opcao == 5:
        print('Finalizando o programa... ✅')
    else:
        print('Opção inválida! Por favor, escolha entre 1 e 5.')

print('Fim do programa! 👋')
