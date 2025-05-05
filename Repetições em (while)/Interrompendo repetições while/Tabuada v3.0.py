while True:  # Cria um laço infinito
    num = int(input('Quer ver a tabuada de qual número? '))

    if num < 0:  # Se o número for negativo, o programa para
        print('Programa de tabuada encerrado. Volte sempre!')
        break

    print('-' * 30)
    for i in range(1, 11):  # Mostra a tabuada de 1 até 10
        print('{} x {:2} = {}'.format(num, i, num * i))
    print('-' * 30)
